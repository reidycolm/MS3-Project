# Recipe Cookbook

![Device Showcase](/images/amiresponsive.png "Recipe Cookbook Responsive")

### View the live project [here.](https://ms3-project-recipe-cookbook.herokuapp.com/)

For my third project of the Code Institute course, I chose to make a recipe cookbook. I wanted a website that would be easy to navigate and welcoming to new users of any age. I really enjoyed my time devolping it and definitely see myself using it to store recipes that I randomly come accross on the internet. I feel like it's a much more interactive and fun way of storing meal plans compared to just bookmarking them. I'm happy with how it turned out and look forward to adding more to it as I continue my journey learning to code.

## User Experience (UX)

- #### User Goals

    1. I want the cookbook to be easy to use. I would very much like if there was a search feature availible on the website as it would make it so much easier to find a recipe that contains ingrediants I need to use up.

    1. I want to be able to add my own recipe. It would be cool to be allowed contribute to the contents of the cookbook and share my own recipes with other people.

    1. I would like a profile type feature on the website so I could keep track of who was posting what. If I'm sharing my own recipes, it's important to be given credit.


- #### Developers Goals

    1. I want to be able to add/remove cuisine types in the cookbook. It's important to have a wid

    1. I want to be able to edit recipes. Some users may need to use other ingrediants because of family dietry needs. I don't want any user who decided to use the cookbook to be left out

    1.  I want my site to be secure. As an admin this is important. There needs to be functionality in place that will stop unwated changes to the cookbook. Users shouldn't be able to edit something they didn't submit.
  

- #### Design

    * **Colour Scheme:** I chose a white background for the majority of the website as I wanted the contents of the recipes and all other information to be as easy to read as possible. I used a lot of the same colours on each of the buttons so that the user would be familiar with them. For example, the red buttons are generally for reseting or deleting information where as the green ones are for editing or submiting new information.

   * **Icons:** The icons used in this project help guide the user throughout the cookbook. On the form to add new recipes, they greatly improve the experience and show what information needs to be added in each of the input fields.

    * **Images:** On the main landing page of the project, I used a card-panel containing an image of the finished recipe to help the user decide what they would like to try. For me I felt adding images was essential as they play an important role in user experience. Everyone likes to see what they're going to be making! 


- #### Wireframes

    * [Large screen](/images/largescreenwireframe.png)
    
    * [Small screen](/images/smallscreenwireframe.png)

## Features

-    **Search Function**
        - Alows user the filter recipie list and will only shows results that match with user input. This feature allows for instant results and will also show flash messages when no results are found. Reset button brings the user quickly back to the main page.

-    **User Registration**
        - Provides functionality for user to create a profile and his/hers information stored on a linked database. User will be given feedback during sign up if the username they are trying to take is already is use and/or their passwords don't match. This ensures the user doesn't spell their passsord incorrecly and can't remember login details. This also allows for a users name to show on the recipe info card so it's users are given credit for adding new recipes to the site.

-    **New/Edit/Delete Recipe**
        - User is able to add a new recipe to the database when they have successfully registered in the form of input fields. This allows for the user to customize what will appear on the cookbook for others. In addition the this, the edit recipie button ensures recipies can be updated at any time. Users are only able to edit the recipes that they have entered themsevles thanks to the profile feature. Delete button ensure all recipe information is removed from database if user so wishes.

-    **Navigation Bar**
        - The nav bar was created using the materialize framework and shows differnt links depending on the user being signed in or now. On smaller screen, navigation will be present in the form of a hamburger icon. When selected, the nav links will appear on screen sliding in from the left hand side.


-    **Add/Edit/Delete Cuisines** 
        - This feature is only visible to the admin of the website. This was done using custom python code in the app.py file. Admin is able to add cusines to the cookbooks databse and this will then be immediately reflected throughout the application. Same applies for editing or deleting if the admin so chooses.


## Technologies Used

- #### Languages

    * [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    * [CSS3](https://en.wikipedia.org/wiki/CSS)
    * [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    * [Python](https://www.python.org/)

  

- #### Frameworks, Libraries and Other Tools

    * [MongoDB](https://www.mongodb.com/)
        -   Database I used to store and retrieve input field information for the website.

    * [Heroku](https://www.heroku.com/)
        -   Used to deploy the application.

    * [Balsamiq](https://balsamiq.com/)
        -   Used to orginally design the recipe book and make custom wireframes.

    * [Materialize](https://materializecss.com/)
        -   Front End Framework that was used to style the majority of the application.

    * [jQuery](https://jquery.com/)
        -   Used to provide interactive design and form validation

    * [Jinja](https://jinja.palletsprojects.com/)
        -   Used to provide logic based design templates.

    * [Gitpod](https://gitpod.io/)
        -   Gitpod was the IDE I used when making this project

    * [Git](https://git-scm.com/)
        - Used for version control and allowed me to save my changes externally by committing to GitHub

    * [Github](https://github.com/)
        -  Was used to store files of the project that I had pushed using Git & Gitpod

    * [Font Awesome](https://fontawesome.com/)   
        - Site used to soruce icons for the webpage.

    * [Lighthouse](https://developers.google.com/web/tools/lighthouse)   
        - Lighthouse is an open-source, automated tool for improving the quality of web pages. You can run it against any web page, public or requiring authentication. It has audits for performance, accessibility, progressive web apps, SEO and more.        

## Testing

- #### Validators

    * **HTML**
        - [The W3C Markup Validator](/images/htmlvalidate.png) was used to validate the HTML files of this project. No errors were found.
        
    * **CSS**
        - [The W3C CSS Validator](/images/cssvalidate.png) was used to validate the CSS file of this project. No errors were found.

    * **JavaScript**
        - [JsHint](/images/jshintvalidate.png) was used to validate the JavaScipt file of this project. No errors were found. 

    * **Python**
        - [PEP8](/images/pythonvalidate.png) was used to validate the Python file of this project. No errors were found.


- #### User Stories Testing    


- #### Manual Testing (Repeated on various devices and browsers)


- #### Bugs

   
## Deployment

The website was developed using Gitpod workspace to commit and push to GitHub. The project uses GitHub for hosting and has been deployed using Heroku.
To access to my page please follow these steps:

### Download

1. Navigate to my repository [GitHub Repository](https://github.com/reidycolm/MS3-Project) 
2. Click the **Code** button.
3. Click the **Download Zip**.
4. Extract where you want to keep all files.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/reidycolm/MS3-Project)
2. Under the repository name, click the "Code" button and a dropdown menu will appear.
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

### Creating an Environment File

Install Flask, in your terminal type `pip3 install Flask` , that sets up Flask functionality. Next you will need to create **env.py** file for storing sensitive data, 
type `touch env.py` in terminal. This file should never be pushed to GitHub, so type `touch .gitignore` to be able to ignore it. Than open the **.gitignore** file and lets 
ignore your **env.py** file typed:
```
env.py
__pycache__/ 

```
save and close it.

In the env.py file we need to hide several bits of data. Open env.py file and type:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "********")
os.environ.setdefault("MONGO_URI", "********")
os.environ.setdefault("MONGO_DBNAME", "recipe_cookbook")
```
Make sure that your env.py file isn't being tracked, type  `git status` and make sure that you can not see it listed.

### MongoDB schema

To create the data schema in your MongoDB Atlas, create a new database called **recipe_cookbook**, add three collections **cuisines**, **recipes**, **users**.
* recipe_cookbook
    * cuisines 
        * _id:ObjectId
        * cuisine_name
    * recipes
        * _id:ObjectId
        * recipe_name 
        * image_url
        * preperation_time
        * cooking_time
        * serves
        * ingredients
        * method
        * created_by
    * users
        * _id:ObjectId
        * username
        * password    

### Heroku Deployment

1. Before deploying your project create a requirements.txt file by running the following command in the CLI;

    `pip3 freeze > requirements.txt`

2. Create a Procfile file by running the following command in the CLI;

    `echo web: python app.py > Procfile`

3. git add and git commit the new requirements and Procfile and then git push the project to GitHub.
3. Log in to [Heroku](https://dashboard.heroku.com/apps).
4. Select "New" on your dashboard and then select "Create new app".
5. Choose a name for your application, select your region, and then click "Create app".
6. From the app dashboard, navigate to "Deploy" tab.
7. From Deployment method select "Github" and confirm the linking of the Heroku app by clicking "Search" then select your repository name.
8. Once you select your repository, click on "Connect".
9. After you connected to your repository, click on "Settings" tab on your app dashboard, and click on "Reveal Config Vars" and add your configuration variables to Heroku.
10. Navigate to "Deploy" tab, and from Manual deploy choose your master branch, and click "Deploy Branch".
11. After you deployed your branch "Enable Automatic Deploys".
12. Site is successfully deployed, any further changes will automatically be updated everytime they are commited and pushed on Github.

## Credits

### Code

- The content I studied on the course during the Backend Development module was extremely helpful when creating this recipe application as it helped with getting all the functionality of the cookbook up and running.

- The "validateMaterializeSelect()" function in the script.js file was taken from the mini project directly to help validate the choose cuisine dropdown fields.

- [Materialize](https://materializecss.com/) Library and Documentation was used throughout the html files to make site responsive on all devices as well as providing styling.


### Content & Media

-   All recipes and images were obtained from the [BBC Food](https://www.bbc.co.uk/food/recipes) website.

-   All icons used were found through font awesome.

-   This website was built for educational purpose only
