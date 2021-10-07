import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# configuration
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# recipes
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# search
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# user registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username").lower()
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")
        existing_user = mongo.db.users.find_one(
            {"username": username})

        # checks if username already exists in db
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if password == confirm_password:
            register = {
                "username": username,
                "password": generate_password_hash(password)
                        }
            mongo.db.users.insert_one(register)

            # put the new user into 'session' cookie
            session["user"] = username
            flash("Registration Successful!")
            return redirect(url_for("profile", username=session["user"]))
        else:
            flash("Passwords do not match")

    return render_template("register.html")


# login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# logout
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# add recipe
@app.route("/new_recipe", methods=["GET", "POST"])
def new_recipe():
    if request.method == "POST":
        recipe = {
            "cuisine_type": request.form.get("cuisine_type"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "preperation_time": request.form.get("preperation_time"),
            "cooking_time": request.form.get("cooking_time"),
            "serves": request.form.get("serves"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your Recipe Was Successfully Added")
        return redirect(url_for("get_recipes"))

    cuisines = mongo.db.cuisines.find().sort("cuisine_type", 1)
    return render_template("new_recipe.html", cuisines=cuisines)


# edit recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "cuisine_type": request.form.get("cuisine_type"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "preperation_time": request.form.get("preperation_time"),
            "cooking_time": request.form.get("cooking_time"),
            "serves": request.form.get("serves"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Your Recipe Was Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines = mongo.db.cuisines.find().sort("cuisine_type", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, cuisines=cuisines)


# view single recipe on seperate page
@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe=recipe)


# delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Succesfully Deleted")
    return redirect(url_for("get_recipes"))


# cuisines page that only appears for admin user
@app.route("/get_cuisines")
def get_cuisines():
    if "user" not in session:
        return redirect(url_for("login"))

    cuisines = list(mongo.db.cuisines.find().sort("cuisine_type", 1))

    if session["user"] == "admin":
        return render_template(
            "cuisines.html", cuisines=cuisines, page_title="Cuisines")

    flash("You do not have permission")
    return redirect(url_for('login'))


# add cuisine
@app.route("/new_cuisine", methods=["GET", "POST"])
def new_cuisine():
    if request.method == "POST":
        cuisine = {
            "cuisine_type": request.form.get("cuisine_type")
        }
        mongo.db.cuisines.insert_one(cuisine)
        flash("New Cusine Added")
        return redirect(url_for("get_cuisines"))
    return render_template("new_cuisine.html")


# edit cuisine
@app.route("/edit_cuisine/<cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    if request.method == "POST":
        submit = {
            "cuisine_type": request.form.get("cuisine_type")
        }
        mongo.db.cuisines.update({"_id": ObjectId(cuisine_id)}, submit)
        flash("Cuisine Successfully Updated")
        return redirect(url_for("get_cuisines"))

    cuisine = mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("edit_cuisine.html", cuisine=cuisine)


# delete cuisine
@app.route("/delete_cuisine/<cuisine_id>")
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({"_id": ObjectId(cuisine_id)})
    flash("Cuisine Successfully Deleted")
    return redirect(url_for("get_cuisines"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
