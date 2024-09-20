# Kibble-Kitchen (Capstone Project)


Kibble Kitchen is an online platform designed to help dog owners plan nutritious meals for their furry companions. The site offers a collection of healthy, homemade dog food recipes along with a meal planning tool to ensure a balanced diet tailored to your dog's needs. Targetting dog owners who want to move beyond store-bought kibble, Kibble Kitchen is perfect for those seeking to provide wholesome, natural meals for their pets while managing meal prep and tracking dietary preferences. Users can create, manage, and share their own recipes while building custom meal plans.
Kibble Kitchen goes beyond just offering recipes; it empowers dog owners to take control of their pet's nutrition with easy-to-follow meal plans, detailed ingredient lists, and portion guides based on breed, size, and dietary requirements. Users can save favourite recipes, create custom meal plans and even track their dog's nutritional intake over time. With a focus on natural, balanced meals, Kibble Kitchen is the go-to resource for pet parents dedicated to giving their dogs the best possible care through thoughtfull, personalised feeding.

## Table of Contents ##

- Features
  
- Wireframes

- User Stories

- Design
  
- UX/UI - List of features

- Agile methodology

- Testing and Responsiveness

- Deployment

- Technologies Used

- Credits

- Known Bugs

- Future features

  <br>

## Features ##

  This web application will let users create, read, update and delete (CRUD) recipes, meal plans, and ingrdients. The admin user will have the ability to manage users, recipes, and other data.

  <span id="features">1.</span> Recipe CRUD Functionality:
    - Users can create, view, update and delete their recipes, complete with ingredients and cooking instructions.
    - Users can provide feedback or rate recipes.
 
  <span id="features">2.</span> User Authentication:
    - Users can register, log in, and log out. Password management features such as reset and change are also available.

  <span id="features">3.</span> Recipe Management(CRUD Functionality):
    - Authenticated users can create, read, update, delete and search for recipes based on keywords, ingredients, or titles. Authenticated users can create recipes by submitting a form with ingredients and instructions.  
 
  <span id="features">4.</span> Meal Plan management(CRUD Functionality):
    - Authenticated users can create, read, update, delete and search recipes. Users can create meal plans by selecting recipes and setting a name,description, and date for the meal.
 
  <span id="features">5.</span> User feedback(Comment on Recipes):
    - Authenticated users can comment on individual recipes. This allows for interaction between users and provides feedback on recipes.
 
  <span id="features">6.</span> Responsive UI and Enhanced User Experience:
    - Crispy Forms: All forms are styled using Bootstrap with Crispy Forms to ensure a clean, responsive design.
    - Navigation Bar: The Top navigation bar includes login/logout links and allow easy access to all sections of the website.
 
  <span id="features">7.</span> Recipe Favourites:
    - Save Favourite Recipes: Users can add recipes to their list of favorites for easy access later.
 
  <span id="features">8.</span> Admin Dashboard:
    - Admin Control: Admin users can access the default Django admin panel to manage users, recipes, meal plans, comments and they can approve or reject recipes.
 
  <span id="features">9.</span> Data Validation & Error Handling:
    - All forms (recipe creation, meal plans and comments) are validated to ensure valid data input from users.
 
  <span id="features">10.</span> API Handling:
    - Integration with external recipe APIs to provide nutritional value of recipes.

## Wireframes ##
To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used Balsamiq to design my site wireframes

[Balsamiq](https://balsamiq.com/wireframes) 


### Mobile Wireframes

<details>

<summary>
Click here to see the Mobile Wireframes
</summary>
  
![image](https://github.com/user-attachments/assets/79f275a4-a466-4f54-8a23-beece207ce09)

![image](https://github.com/user-attachments/assets/1b30046f-f307-4b15-a950-ea487a37d800)




</details>


### Desktop Wireframes

<details>

<summary>
Click here to see the Desktop Wireframes
</summary>

![image](https://github.com/user-attachments/assets/f9ba2ceb-5f43-4846-a279-3a43471d9098)

![image](https://github.com/user-attachments/assets/563154b6-9729-4ed3-a863-fd22fa087bb9)



 </details>

### Tablet Wireframes

<details>

<summary>
Click here to see the Tablet Wireframes
</summary>

![image](https://github.com/user-attachments/assets/241cd8c2-f03c-4adc-9bcf-273e839d92a9)

![image](https://github.com/user-attachments/assets/88b54bc8-82ea-4315-a879-08db30c201bf)



 </details>

## ERD ##

<details>

<summary>
Click here to see the ERD
</summary>

![image](https://github.com/user-attachments/assets/5b7183ce-765e-4989-bd43-9678c3b35d42)



</details>


## UX - User stories ##

![image](https://github.com/user-attachments/assets/14fee6ab-66fc-40d3-94a8-ed2654a4f26c)

1. As a site user I can sign up for an account so that I can create, save, and manage my own recipes and meal plans.

        AC1 A sign-up form with fields for email, username and password.

        AC2 Error message display if any form validation fails (e.g., email already taken, password too weak). Successful account creation redirects to the login page.

        AC3 User data is stored securely in the database (except password).

2. As a site user I can view all available recipes when I click so that I can discover new meal ideas.

        AC1 A page display all available recipes with titles and brief descriptions. Each recipe item includes a detailed view.

        AC2 Pagination is implemented is there are many recipes.

        AC3 Users can filter or search recipes by title or ingredient.

3. As a site admin I can manage all users, recipes, and comments so that I can ensure the platform runs smoothly and maintain content quality.

        AC1 Admin dashboard accessible through Django's admin interface.

        AC2 Admin can view, edit, delete users, recipes, and comments.

        AC3 Admin can filter and search through users, recipes, and comments.

4. As a site user I can create new recipes so that I can store, and manage my favourite meals.

        AC1 Authenticated users can access a recipe creation form, which includes fields for title, ingredients, and instructions.

        AC2 Required fields must be validated (e.g., title and ingredients cannot be blank). Error message display if any of required fields are missing.

        AC3 Users are redirected to the recipe details page upon successful creation.

5. As a site user I can comment on recipes and leave feedback so that I can share my thoughts or improvements with the community.

        AC1 Authenticate users can leave comments on individual recipe pages, which will be displayed below each recipe.

        AC2 Upon submission, the comment is saved and displayed under the recipe. Users can see a list of comments, including who posted them and when.

        AC3 Only the user who posted the comment can delete or edit their own comment.

6. As a site admin I can approve or disapprove comments so that I can filter out objectionable comments

        AC1 Given a logged in user, they can approve a comment.

        AC2 Given a logged in user, they can disapprove a comment.

7. As a site admin I can create draft recipes so that I can finish writing the instructions later

        AC1 Given a logged user, they can save a draft recipe, which they can finish at a later time.

8. As a site user I can read the "About" page so that I can learn more about the purpose of the website and the team behind it.

        AC1 An "About" page that describes the website's purpose and goals.

        AC2 Accessible from the main navigation bar.

9. As a Potential Collaborator I can fill in a contact form so that I can submit a request for collaboration

        AC1 Contact form should be easily accessible from the "About" page.
        
        AC2 A "Submit" button should be present and clearly labelled.

10. As a site user I can search for recipes based on ingredients or titles so that I can quickly find relevant meal ideas.

        AC1 A search bar is present on the recipe list page.
        
        AC2 Search results are dynamically based on the input.

11. As a Site User I can save favourite recipes so that I can access them easily later.

        AC1 Authenticated users can click a "Favourite" button on each recipe page.
        
        AC2 Favourite recipes are saved to a "Favourites" list in the user's profile.
        
        AC3 users can view, manage, and remove recipes from their favourite list.
    

##  Design ##

 ### Colour Scheme ###



 ### Typography ###




 ### Imagery ###




## UX/UI - Features ##



## Agile Methodology ##
https://github.com/users/shivani-CI/projects/9




## Testing and Responsiveness ##





## Manual testing ##





## Deployment ##





## Technologies Used ##


 ### Front-End Technologies ###


 ### Back-End Technologies ###



## Credits ##



## Known bugs ##



### Important Notice - 20 September 2024

- I recently discovered that a sensitive secret key was unintentionally left exposed in the "settings.py" file. This has been rectified by newly created secret key added to environment variables. The exposed secret key has been removed from the settings.py. 


## Future features ##
 
  
