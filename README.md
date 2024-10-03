# Kibble-Kitchen (Capstone Project)


Kibble Kitchen is an online platform designed to help dog owners plan nutritious meals for their furry companions. The site offers a collection of healthy, homemade dog food recipes along with a meal planning tool to ensure a balanced diet tailored to your dog's needs. Targetting dog owners who want to move beyond store-bought kibble, Kibble Kitchen is perfect for those seeking to provide wholesome, natural meals for their pets while managing meal prep and tracking dietary preferences. Users can create, manage, and share their own recipes while building custom meal plans.
Kibble Kitchen goes beyond just offering recipes; it empowers dog owners to take control of their pet's nutrition with easy-to-follow meal plans, detailed ingredient lists, and portion guides based on breed, size, and dietary requirements. Users can save favourite recipes, create custom meal plans and even track their dog's nutritional intake over time. With a focus on natural, balanced meals, Kibble Kitchen is the go-to resource for pet parents dedicated to giving their dogs the best possible care through thoughtfull, personalised feeding.

![image](https://github.com/user-attachments/assets/21129ac5-2dd3-44c1-a752-d84ff63543ae)


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
    - Users can provide feedback on recipes.

    
 
  <span id="features">2.</span> User Authentication:
    - Users can register, log in, and log out. Password management features such as reset and change are also available.

  <span id="features">3.</span> Recipe Management(CRUD Functionality):
    - Authenticated users can create, read, update, delete recipes. Authenticated users can create recipes by submitting a form with ingredients and instructions.  
 
  <span id="features">4.</span> Meal Plan management:
    - Authenticated users can create and view Meal Plans. Users can create meal plans by selecting recipes and setting a name, title, and dates for the meal.
 
  <span id="features">5.</span> User feedback(Comment on Recipes):
    - Authenticated users can comment on individual recipes. This allows for interaction between users and provides feedback on recipes.
 
  <span id="features">6.</span> Responsive UI and Enhanced User Experience:
    - Crispy Forms: All forms are styled using Bootstrap with Crispy Forms to ensure a clean, responsive design.
    - Navigation Bar: The Top navigation bar includes login/logout links and allow easy access to all sections of the website.
 
  <span id="features">8.</span> Admin Dashboard:
    - Admin Control: Admin users can access the default Django admin panel to manage users, recipes, meal plans, comments and they can approve or reject recipes, comments, meal plans and users.
 
  <span id="features">9.</span> Data Validation & Error Handling:
    - All forms (recipe creation, meal plans and comments) are validated to ensure valid data input from users.
 
  <span id="features">10.</span> API Handling:
    - Integration with external recipe APIs to provide nutritional value of recipes.

   <br>
   
## Wireframes ##
To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used Balsamiq to design my site wireframes

[Balsamiq](https://balsamiq.com/wireframes) 

### Mobile Wireframes

<details>

<summary>
Click here to see the Mobile Wireframes
</summary>

Home Page

![image](https://github.com/user-attachments/assets/eddd9e59-d6e7-4da7-a30a-673bb8f58611)

Browse Recipe

![image](https://github.com/user-attachments/assets/6a732590-2851-4b83-a414-672ce7b98fcb)

Recipe Detail

![image](https://github.com/user-attachments/assets/3553ca38-f1b0-4574-a841-f046f1d62d1d)

Add Recipe

![image](https://github.com/user-attachments/assets/531ef0bb-8bdd-4e38-8fdc-3e5d8a752b5a)

Create Meal Plan

![image](https://github.com/user-attachments/assets/56010ea2-1f9d-4f4a-a3ad-564b6c786cad)

My Meal Plans

![image](https://github.com/user-attachments/assets/c83c68eb-387c-4211-bbe3-17df3e2941ea)

Meal Plan Detail

![image](https://github.com/user-attachments/assets/3ea39f2c-188e-4b3a-89cc-c0edbff3bbec)


</details>


### Desktop Wireframes

<details>

<summary>
Click here to see the Desktop Wireframes
</summary>

Home Page

![image](https://github.com/user-attachments/assets/554dc406-117b-4be9-b4f2-3e7279d460f9)

Browse Recipe

![image](https://github.com/user-attachments/assets/1378ce9d-b6d0-4b8f-8d80-acead1741257)

Recipe Detail

![image](https://github.com/user-attachments/assets/912141ec-7395-4212-b807-e920e2381e11)

Add Recipe

![image](https://github.com/user-attachments/assets/77adf5e4-864a-4045-b288-b4fe793e8524)

Create Meal Plan

![image](https://github.com/user-attachments/assets/b761b658-4a50-4dd5-87ab-11602a1b55ec)

My Meal Plans

![image](https://github.com/user-attachments/assets/81a9f425-e4ef-4994-9b1b-5057039d382e)

Meal Plan Detail

![image](https://github.com/user-attachments/assets/cfef94d6-322c-41a5-afff-02f2c62b178d)


 </details>

### Tablet Wireframes

<details>

<summary>
Click here to see the Tablet Wireframes
</summary>

Home Page

![image](https://github.com/user-attachments/assets/91767d76-fe1e-43b4-af00-070845607714)

Browse Recipes

![image](https://github.com/user-attachments/assets/d70198c3-a721-414c-8504-968eb728fcf4)

Recipe Detail

![image](https://github.com/user-attachments/assets/516819d5-01ae-4cfa-91c1-1a276ea83f24)

Add Recipe

![image](https://github.com/user-attachments/assets/5cebfca7-7ae8-4a0b-a8d4-2907b37b96e7)

Create Meal Plan

![image](https://github.com/user-attachments/assets/63e7045c-bb1e-4d2d-9fad-60bf665d944c)

My Meal Plans

![image](https://github.com/user-attachments/assets/2386cc4e-a14e-43f3-8875-68caeab15e5b)

Meal Plan Detail

![image](https://github.com/user-attachments/assets/1fe3992a-1af4-43cf-a70a-862ac2fc26c4)


 </details>

 <br>
 
## ERD ##


<details>

<summary>
Click here to see the ERD
</summary>

![image](https://github.com/user-attachments/assets/c3fe63e3-7c7f-42be-ba34-669641b7bcc7)

</details>

 <br>
 
## UX - User stories for iteration 1 ##

<details>

<summary>
Click here to see kanban board at the beginning of iteration 1
</summary>

This is at the beginning of iteration 1:

![image](https://github.com/user-attachments/assets/14fee6ab-66fc-40d3-94a8-ed2654a4f26c)

</details>

<details>

<summary>
Click here to see kanban board at the end of iteration 1 
</summary>

This is at the end of iteration 1:

![image](https://github.com/user-attachments/assets/3eebf68a-9821-4954-a39e-d38ae007974c)

</details>

1. As a site user I can sign up for an account so that I can create, save, and manage my own recipes and meal plans.

        AC1 A sign-up form with fields for email, username and password.

        AC2 Error message display if any form validation fails (e.g. password too weak). Successful account creation redirects to the login page.

        AC3 User data is stored securely in the database (except password).

2. As a site user I can view all available recipes when I click so that I can discover new meal ideas.

        AC1 A page display all available recipes with titles and brief descriptions. Each recipe item includes a detailed view.

        AC2 Pagination is implemented is there are many recipes.

3. As a site admin I can manage all users, recipes, and comments so that I can ensure the platform runs smoothly and maintain content quality.

        AC1 Admin dashboard accessible through Django's admin interface.

        AC2 Admin can view, edit, delete users, recipes, and comments.

        AC3 Admin can filter and search through users, recipes, meal plans and comments.

4. As a site user I can create new recipes so that I can store, and manage my recipes.

        AC1 Authenticated users can access a recipe creation form, which includes fields for title, ingredients, prep time, cook time, difficulty levels, image and instructions.

        AC2 Required fields must be validated (e.g., title and ingredients cannot be blank). Error message display if any of required fields are missing.

        AC3 Users are redirected to the recipe details page upon successful creation.

5. As a site user I can comment on recipes and leave feedback so that I can share my thoughts or improvements with the community.

        AC1 Authenticated users can leave comments on individual recipe pages, which will be displayed below each recipe.

        AC2 Upon submission, the comment is saved and displayed under the recipe. Users can see a list of comments, including who posted them and when.

        AC3 Only the user who posted the comment can delete or edit their own comment.

6. As a site admin I can approve or disapprove comments so that I can filter out objectionable comments

        AC1 Given a logged in user, they can approve a comment.

        AC2 Given a logged in user, they can disapprove a comment.

7. As a site admin I can create draft recipes so that I can finish writing the instructions later

        AC1 Given a logged user, they can save a draft recipe, which they can finish at a later time.

8. As a site user I can read the "Home" page so that I can learn more about the purpose of the website.

        AC1 An "Home" page that describes the website's purpose and goals.

        AC2 Accessible from the main navigation bar.

10. As a site user I can search for recipes based on ingredients or titles so that I can quickly find relevant meal ideas.

        AC1 A search bar is present on the recipe list page.
        
        AC2 Search results are dynamically based on the input.

11. As a Site User I can save favourite recipes so that I can access them easily later.

        AC1 Authenticated users can click a "Favourite" button on each recipe page.
        
        AC2 Favourite recipes are saved to a "Favourites" list in the user's profile.
        
        AC3 users can view, manage, and remove recipes from their favourite list.

12. As a site user I can create meal plans by adding selected recipes for specific dates so that I can organise my dog's meals for my chosen dates

        AC1 Authenticated users can access a meal plan creation form.
    
        AC2 Users can select multiple recipes and associate them with a meal plan.
    
        AC3 Meal plans includes a title, start date, end date field and a list of recipes to select from.

13. As a site user I can view my meal plans so that I can easily manage my dog's meals.

        AC1 Users can view a list of their own meal plans, which displays recipe counts, meal plan length, start date and end date field.
    
        AC2 Users can view meal plan details by clicking on the meal plan view button.
        
        AC3 Users can view individual meal plan details that will show all the recipes and related images which were in that specific meal plan. They can also view the recipe detail by clicking on the recipe title.

16. As a site user I can see nutritional information for recipe so that I can control my dogs diet.

        AC1 Integrate third-party API to fetch nutritional information for all the ingredients in a recipe.

- Please note that due to time constraint user story 9 and 10 are moved to iteration 2

 <br>

 ##  Design ##


  <br>

 ### Colour Scheme ###

  <br>

 ### Typography ###


 <br>

 ### Imagery ###


 <br>

## UX/UI - Features ##

 <br>

## Agile Methodology ##

https://github.com/users/shivani-CI/projects/9

 <br>

## Testing and Responsiveness ##



 <br>

## Manual testing ##



 <br>

## Deployment ##



 <br>

## Technologies Used ##

 <br>
 
### Front-End Technologies ###

 <br>
 
### Back-End Technologies ###

 <br>

## Credits ##

 <br>

## Known bugs ##

 <br>

### Important Notice - 20 September 2024

- I recently discovered that a sensitive secret key was unintentionally left exposed in the "settings.py" file. This has been rectified by newly created secret key added to environment variables. The exposed secret key has been removed from the settings.py. 

 <br>
 
## Future features ##
 
  
