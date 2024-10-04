<h1 align="center">Kibble-Kitchen (Capstone Project)</h1>

[View the live project here](https://kibble-kitchen-8aaad6eac024.herokuapp.com/)

<br>

Kibble Kitchen is an online platform designed to help dog owners plan nutritious meals for their furry companions. The site offers a collection of healthy, homemade dog food recipes along with a meal planning tool to ensure a balanced diet tailored to your dog's needs. Targetting dog owners who want to move beyond store-bought kibble, Kibble Kitchen is perfect for those seeking to provide wholesome, natural meals for their pets while managing meal prep and tracking dietary preferences. Users can create, manage, and share their own recipes while building custom meal plans.

Kibble Kitchen goes beyond just offering recipes; it empowers dog owners to take control of their pet's nutrition with easy-to-follow meal plans, and detailed ingredient lists. Users can share recipes, create custom meal plans and even track their dog's nutritional intake over time. With a focus on natural, balanced meals, Kibble Kitchen is the go-to resource for pet parents dedicated to giving their dogs the best possible care through thoughtfull, personalised feeding.

<br>

![image](https://github.com/user-attachments/assets/21129ac5-2dd3-44c1-a752-d84ff63543ae)

<br>

## Table of Contents

* [Features](#features)  
* [Wireframes](#wireframes)
* [ERD](#erd)
* [User stories (UX)](#user-stories-ux)
* [Design](#design)  
* [Agile methodology](#agile-methodology)
* [Testing](#testing)
* [Deployment](#deployment)
* [Technologies Used](#technologies-used)
* [Credits](#credits)
* [Known Bugs](#known-bugs)
* [Future features](#future-features)

  <br>

## Features

  This web application will let users create, read, update and delete (CRUD) recipes, share recipe, create meal plan, and comment on recipe. The admin user will have the ability to manage users, recipes, meal plan and comment.

    <span id="features">1.</span> Navigation Bar:
   
    - The navigation bar is positioned at the top of every page, ensuring easy access to key features like home, browse recipes, add recipes, create meal plan and my meal plan. Depending on the user’s login status, the navbar will adapt to show links for login/signup and my meal plan.

<br>

### Navigation bar for all users:

![image](https://github.com/user-attachments/assets/3f0f2ff3-5728-48f5-8cfb-c3df9ecfe1a8)

<br> 

### Navigation bar for authenticated users:

![image](https://github.com/user-attachments/assets/66872442-f198-4986-8392-adf9ef572b8e)

<br> 
 
  <span id="features">2.</span> User Authentication:
  
    - Users can register, log in, and log out. Password management features such as reset and change are also available. Users can create account and log in to access additional features, such as my meal plans.

<br> 

### Dropdown signup navigation:

![image](https://github.com/user-attachments/assets/8a7f7bf1-c616-4b3c-bba4-cd0fcd46c66b)



![image](https://github.com/user-attachments/assets/3ba65f16-756f-496d-aad9-9cbead10345e)

![image](https://github.com/user-attachments/assets/acfe5e51-ec47-4aaa-aa8d-7c2e5cf427db)

  


![image](https://github.com/user-attachments/assets/3f00dc68-74c5-4a80-800c-e653d75f9ae3)

<br> 
    
  <span id="features">3.</span> Home Page:
  
    - The home page offers an inviting interface for users to explore. It display hero image and highlights key features about us, making it easy for users to navigate. The page is designed with a user-friendly layout that integrates a consistent color scheme.
    


  <span id="features">4.</span> Recipe Management:
  
    - Add Recipes: Users can create new dog food recipes, specifying details like recipe title, description, prep time, cook time, difficulty, and status. The form allows users to dynamically add ingredients if they don't already exist in the database, ensuring flexibility.
    
    - Browse Recipes: The recipe browsing page lists all available recipes. Users can view recipes image, title, cook time, created date and a button to view recipe detail. 
    
    - Recipe Detail View: Each recipe has a detailed view that displays all recipe-related information, including the list of ingredients, quantities, preparation instructions and nutritional information. Users can leave comments and feedback on recipes. On recipe detail page authenticated user will have option to add recipe to meal plan, edit recipe and delete recipe.


  <span id="features">5.</span> Ingredient Management:
  
    - Ingredient Form: Ingredients in the recipe are linked through a Many-to-Many relationship via the RecipeIngredient model. This relationship allows users to specify ingredient quantities and units in each recipe. If a required ingredient isn't listed, users can add new ingredients dynamically without leaving the form.

    - Dynamic Formset for Ingredients: Users can add and remove ingredient fields dynamically while creating a recipe. This makes the recipe creation process seamless and user-friendly.
  
 
  <span id="features">6.</span> Meal Plan management:
  
    - Create Meal Plans: Authenticated users can plan meals for their dogs by selecting from existing recipes. The meal planner feature helps users schedule meals based on their dog's dietary needs.
    
    - Browse Meal Plans: Users can view a list of all their previously created meal plans. Each meal plan displays mealplan title, recipe count, meal plan length, dates and a button to view meal plan detail.

    - Meal Plan Detail View: Each meal plan contains a detailed view where users can see which recipes are included, along with the recipe details and the meal plan title.
 
  <span id="features">7.</span> User feedback(Comment on Recipes):
  
    - At the bottom of each recipe detail page, authenticated users can leave comments about the recipe. This feature promotes community interaction by allowing users to share their thoughts and feedback.
 
  <span id="features">8.</span> Responsive UI and Enhanced User Experience:
  
    - Crispy Forms: All forms are styled using Bootstrap with Crispy Forms to ensure a clean, responsive design.
    
    - Mobile & Tablet Friendly: The entire project is designed to be responsive across all screen sizes. Whether on a desktop, tablet, or mobile device, the layout adjusts accordingly. Forms, recipe details, meal plans, and navigation elements are all optimised for smaller screens, ensuring a smooth user experience.
    
  <span id="features">9.</span> Admin Dashboard:
  
    - Admin users have full control over the site content. The Django admin panel allows managing users, recipes, meal plans, and more. Admins can easily add, delete, or update any information stored in the database.
 
  <span id="features">10.</span> Data Validation & Error Handling:
  
    - All forms (recipe creation, meal plans and comments) are validated to ensure valid data input from users.
 
  <span id="features">11.</span> API Handling:
  
    - Integration with external recipe APIs to provide nutritional information of recipes.

   <br>
   
## Wireframes
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
 
## ERD


<details>

<summary>
Click here to see the ERD
</summary>

![image](https://github.com/user-attachments/assets/c3fe63e3-7c7f-42be-ba34-669641b7bcc7)

</details>

 <br>
 
## User stories UX

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

 ##  Design


  <br>

 ### Colour Scheme

  <br>

 ### Typography


 <br>

 ### Imagery

 <br>
 
## Agile Methodology

https://github.com/users/shivani-CI/projects/9

 <br>

## Testing



 <br>

 ### Manual testing



 <br>

## Deployment



 <br>

## Technologies Used

 <br>
 
### Front-End Technologies

 <br>
 
### Back-End Technologies

 <br>

## Credits

 <br>

## Known bugs

 <br>

### Important Notice - 20 September 2024

- I recently discovered that a sensitive secret key was unintentionally left exposed in the "settings.py" file. This has been rectified by newly created secret key added to environment variables. The exposed secret key has been removed from the settings.py. 

 <br>
 
## Future features ##
 
  
