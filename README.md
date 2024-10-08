<h1 align="center">Kibble-Kitchen (Capstone Project)</h1>

[View the live project here](https://kibble-kitchen-8aaad6eac024.herokuapp.com/)

<br>

Kibble Kitchen is an online platform designed to help dog owners plan nutritious meals for their furry companions. The site offers a collection of healthy, homemade dog food recipes along with a meal planning tool to ensure a balanced diet tailored to your dog's needs. Targetting dog owners who want to move beyond store-bought kibble, Kibble Kitchen is perfect for those seeking to provide wholesome, natural meals for their pets while managing meal prep and tracking dietary preferences. Users can create, manage, and share their own recipes while building custom meal plans.

Kibble Kitchen goes beyond just offering recipes; it empowers dog owners to take control of their pet's nutrition with easy-to-follow meal plans, and detailed ingredient lists. Users can share recipes, create custom meal plans and even track their dog's nutritional intake over time. With a focus on natural, balanced meals, Kibble Kitchen is the go-to resource for pet parents dedicated to giving their dogs the best possible care through thoughtfull, personalised feeding.

<br>

![image](https://github.com/user-attachments/assets/21129ac5-2dd3-44c1-a752-d84ff63543ae)

<br>

## Important Notice - Nutritional Information

In this project I have used an API to retrieve nuturtional information for recipes. Currently the API is not being used due to free tier rate limits (400 per month) and how I have implement it (API is called each time the get recipe detail page is refreshed). Usuage above this limit could result in charges or an retrieval error. It has been tested and it is working as expected.

In the next iteration of Kibble Kitchen this can be improved to store the nuturtional information in the database when a recipe is created or edited.

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

<details>

<summary>
  <span id="features">1.</span> Navigation Bar:
  
    - The navigation bar is positioned at the top of every page, ensuring easy access to key features like home, browse recipes, add recipes, create meal plan and my meal plan. Depending on the user’s login status, the navbar will adapt to show links for login/signup and my meal plan.
</summary>
  
  ### Navigation bar for all users:

![image](https://github.com/user-attachments/assets/3f0f2ff3-5728-48f5-8cfb-c3df9ecfe1a8)

<br>

  ### Navigation bar for authenticated user:

![image](https://github.com/user-attachments/assets/66872442-f198-4986-8392-adf9ef572b8e)


</details>

<details>

<summary>
  <span id="features">2.</span> User Authentication:
  
    - Users can register, log in, and log out. Password management features such as reset and change are also available. Users can create account and log in to access additional features, such as my meal plans.
</summary>


  ### Dropdown signup navigation for user:

![image](https://github.com/user-attachments/assets/8a7f7bf1-c616-4b3c-bba4-cd0fcd46c66b)

<br> 

  ### Signup form for user to complete:

![image](https://github.com/user-attachments/assets/3ba65f16-756f-496d-aad9-9cbead10345e)

<br> 

  ### Message confirming user signed in:

![image](https://github.com/user-attachments/assets/acfe5e51-ec47-4aaa-aa8d-7c2e5cf427db)

<br> 

  ### Login form for returning user to complete:

![image](https://github.com/user-attachments/assets/2bc96a1a-a0b8-4e37-9e8f-cb0af47abdd3)

<br> 

  ### Message confirming user signed out:

![image](https://github.com/user-attachments/assets/3f00dc68-74c5-4a80-800c-e653d75f9ae3)

<br>

</details>

<details>

<summary>
  <span id="features">3.</span> Home Page:
  
    - The home page offers an inviting interface for users to explore. It display hero image and highlights key features about us, making it easy for users to navigate. The page is designed with a user-friendly layout that integrates a consistent color scheme.
</summary>
    
<br> 

  ### Home Page:
  
![image](https://github.com/user-attachments/assets/2e44b40d-7a94-4048-9f17-73427ac46898)
![image](https://github.com/user-attachments/assets/ae6b851e-06fb-4e4a-83aa-5cda786b4266)

<br> 

</details>

<details>

<summary>
  <span id="features">4.</span> Recipe Management:

    - Add Recipes: Users can create new dog food recipes, specifying details like recipe title, description, prep time, cook time, difficulty, and status. The form allows users to dynamically add ingredients if they don't already exist in the database, ensuring flexibility.

    - Browse Recipes: The recipe browsing page lists all available recipes. Users can view recipes image, title, cook time, created date and a button to view recipe detail. 

    - Recipe Detail View: Each recipe has a detailed view that displays all recipe-related information, including the list of ingredients, quantities, preparation instructions and nutritional information. Users can leave comments and feedback on recipes. On recipe detail page authenticated user will have option to add recipe to meal plan, edit recipe and delete recipe.
</summary>
     
<br> 

   ### Add Recipe Page:
 
![image](https://github.com/user-attachments/assets/26204993-98f7-461e-a6d5-9cf50bc9d42f)
![image](https://github.com/user-attachments/assets/4d217a4d-1990-4553-8696-91388139acfd)
![image](https://github.com/user-attachments/assets/778fd200-65a9-4190-aa54-c3609b5f816e)

<br> 

  ### Browse Recipe Page:

![image](https://github.com/user-attachments/assets/313b1d86-6ecb-41ca-94d3-6b08b6b94aad)
![image](https://github.com/user-attachments/assets/9c9dd030-2c3f-4a0d-8998-c7c96e762b48)

<br> 

  ### Recipe Detail Page:
![image](https://github.com/user-attachments/assets/e44f9aa2-2e7a-4fe3-bdbb-b605a6df72e5)
![image](https://github.com/user-attachments/assets/22dca8a0-0a26-4f27-a4e0-07f8633ed446)

<br>

   ### Add Recipe Page/ Form: 
 
![image](https://github.com/user-attachments/assets/26204993-98f7-461e-a6d5-9cf50bc9d42f)
![image](https://github.com/user-attachments/assets/4d217a4d-1990-4553-8696-91388139acfd)
![image](https://github.com/user-attachments/assets/778fd200-65a9-4190-aa54-c3609b5f816e)

<br>

</details>

<details>

<summary>
  <span id="features">5.</span> Ingredient Management:
  
    - Ingredient Form: Ingredients in the recipe are linked through a Many-to-Many relationship via the RecipeIngredient model. This relationship allows users to specify ingredient quantities and units in each recipe. If a required ingredient isn't listed, users can add new ingredients dynamically without leaving the form.
    
    - Dynamic Formset for Ingredients: Users can add and remove ingredient fields dynamically while creating a recipe. This makes the recipe creation process seamless and user-friendly.
    
    - Create Meal Plans: Authenticated users can plan meals for their dogs by selecting from existing recipes. The meal planner feature helps users schedule meals based on their dog's dietary needs.
</summary>

<br> 

  ### Add Recipe Page - Ingredient Input Section:
  
![image](https://github.com/user-attachments/assets/f696b715-cc2c-44ef-abb1-c90175517911)

<br>
</details>

<details>

<summary>
  <span id="features">6.</span> Meal Plan management:
  
    - Browse Meal Plans: Users can view a list of all their previously created meal plans. Each meal plan displays mealplan title, recipe count, meal plan length, dates and a button to view meal plan detail.

    - Meal Plan Detail View: Each meal plan contains a detailed view where users can see which recipes are included, along with the recipe details and the meal plan title.
</summary>

<br> 

   ### Create Meal Plan Page:
   
![image](https://github.com/user-attachments/assets/9697e573-bc45-4fda-93c3-e985d553b099)

<br> 
    
   ### Browse Meal Plan Page:

![image](https://github.com/user-attachments/assets/f13a140d-3eb1-4f00-a959-0becb9bf975a)
![image](https://github.com/user-attachments/assets/f1444b37-cac7-482c-afdc-6663188613fd)

<br> 
  
  ### Meal Plan Recipes Page:

![image](https://github.com/user-attachments/assets/c92f99bf-b748-40b4-bfac-a292b66b9e74)

 <br>

</details>

<details>

<summary>
  <span id="features">7.</span> User feedback(Comment on Recipes):

    - At the bottom of each recipe detail page, authenticated users can leave comments about the recipe. This feature promotes community interaction by allowing users to share their thoughts and feedback.
</summary>

<br> 

  ### Recipe Detail Page - Comment Section:

![image](https://github.com/user-attachments/assets/41d12cdb-e884-4b4c-93cf-e7ee2c312ecb)

<br>

</details>

<details>

<summary>
  <span id="features">8.</span> Responsive UI and Enhanced User Experience:
  
    - Crispy Forms: All forms are styled using Bootstrap with Crispy Forms to ensure a clean, responsive design.
    
    - Mobile & Tablet Friendly: The entire project is designed to be responsive across all screen sizes. Whether on a desktop, tablet, or mobile device, the layout adjusts accordingly. Forms, recipe details, meal plans, and navigation elements are all optimised for smaller screens, ensuring a smooth user experience.
</summary>

<br>

![image](https://github.com/user-attachments/assets/caa2a4e2-6a8c-4789-a8dd-afc0102855ab)

![image](https://github.com/user-attachments/assets/56e26612-d664-4658-9563-ed49a6a99679)

![image](https://github.com/user-attachments/assets/3bfc36db-7b10-4833-8d08-daa2b5fc71c6)

![image](https://github.com/user-attachments/assets/c580d1b1-0b11-4570-a672-f136cc487cb0)

![image](https://github.com/user-attachments/assets/22d98b1f-d5f2-40c4-a800-c24a040ebf57)

![image](https://github.com/user-attachments/assets/76e1c9ac-b27e-4845-887c-09c04fd7f8f7)

![image](https://github.com/user-attachments/assets/aa829b00-99e6-4af0-8a47-f5065c1083fd)

![image](https://github.com/user-attachments/assets/3dc947eb-02c2-4bbe-8592-04b28d4eb917)

![image](https://github.com/user-attachments/assets/1a69d3ec-74f1-4a64-bdaf-0565836e7be9)

![image](https://github.com/user-attachments/assets/4e3c255c-1598-4b5c-a609-16dd1f9dd9ca)

![image](https://github.com/user-attachments/assets/43fc543b-c810-4cc5-a2bc-b758f53fa60f)

![image](https://github.com/user-attachments/assets/9b7c53a3-7141-4341-afca-cddd91a772d6)

![image](https://github.com/user-attachments/assets/b86e98dc-9bf6-4a97-bac2-d01d96c2d5d7)

![image](https://github.com/user-attachments/assets/ec249258-ff06-4c5b-97da-67d69bfc1ecb)

</details>

<details>

<summary>
  <span id="features">9.</span> Admin Dashboard:
  
    - Admin users have full control over the site content. The Django admin panel allows managing users, recipes, meal plans, and more. Admins can easily add, delete, or update any information stored in the database.
<br>

</summary>

  ### Admin Dashboard:

![image](https://github.com/user-attachments/assets/f2252346-1161-4229-b4e1-7687ef580834)

<br>

</details>

  <span id="features">10.</span> Data Validation & Error Handling:
  
    - All forms (recipe creation, meal plans and comments) are validated to ensure valid data input from users.

 <br>

 <details>

 <summary>
  <span id="features">11.</span> API Handling:
  
    - Integration with external recipe APIs to provide nutritional information of recipes.
  <br>
  </summary>

   ### Recipe Detail Page - Nutritional Information Section:

![image](https://github.com/user-attachments/assets/cce94e7a-3dc4-467b-a1c8-7edb8bd78923)
![image](https://github.com/user-attachments/assets/d4371c1f-e0cd-49a3-af4d-bb6a59ed5939)

   <br>

</details>
   
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

<details>

<summary>
  User stories worked on  
</summary>
  
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
</details>

 ### Please note that due to time constraint user story 9 and 10 are moved to iteration 2

 <br>

 ##  Design

  <br>

 ### Colour Scheme

The color scheme for Kibble Kitchen incorporates red, gold, white, and black, creating a vibrant and energetic aesthetic that aligns with the playful yet practical nature of the app. Red symbolises passion and love, representing the care that pet owners put into creating healthy meals for their dogs. Gold adds a touch of warmth and quality, reflecting the premium experience and the idea of providing the best nutrition. White brings a clean and simple look, emphasising the app's user-friendliness and focus on health. Black offers balance and sophistication, grounding the design and ensuring readability, especially in the navigation and content areas. Together, these colors make Kibble Kitchen a fun and inviting platform for sharing dog food recipes and planning balanced meals.

<br>

  ![image](https://github.com/user-attachments/assets/1efe4cd0-09e0-4226-82d2-e3ac74b74fad)

<br>

 ### Typography

Google Fonts is used to import the chosen fonts for use in the site. I have chosen to use Georgia and serif fonts.

 <br>

 ### Imagery

The imagery on Kibble Kitchen is generated using DeepAI to create visually appealing hero images and recipe visuals, adding a dynamic and modern touch to the app. These custom-generated images enhance the user experience by showcasing the delicious and healthy dog food recipes in an eye-catching way. The consistent use of red and gold throughout all pages reinforces the brand identity, creating a cohesive look and feel. This color palette, along with the dynamic imagery, ensures that users enjoy a visually engaging and seamless experience across the entire app.

 <br>
 
## Agile Methodology

I used GitHub projects to manage my project. Before starting the project I created several user stories showing how users will interact with the web app. I then assigned them to different catorgies (MOSCOW) so I could prioritise them making sure all the stories I was working on could be completed with the project timeline. This is the link to my project Kanban board: https://github.com/users/shivani-CI/projects/9.

 <br>

## Testing
<details>

<summary>
  HTML Validation results
</summary>

Home page

![image](https://github.com/user-attachments/assets/f690761d-f1ef-4efc-bbdc-1c637392f853)

Browse recipes

![image](https://github.com/user-attachments/assets/24d5ca9c-6eaa-4933-855c-5de13258849e)

Recipe detail

![image](https://github.com/user-attachments/assets/3eacfa73-3914-41b2-a4b4-3ded35f4d580)

Add recipe

![image](https://github.com/user-attachments/assets/34dd21f2-fcb1-4eca-89da-4719a55b5996)

There are errors on this page due to SummerNote. There is also a bug being caused by the recipe ingredient formset.

Create Meal Plan

![image](https://github.com/user-attachments/assets/7225dd83-f54d-4242-bea0-8848db914419)

My Meal Plans

![image](https://github.com/user-attachments/assets/cf63b8e5-6e1f-44d1-b5a3-02d95db585e4)

Meal Plan detail

![image](https://github.com/user-attachments/assets/d65f5eed-0a24-4454-b7c5-1eb0a8904633)

</details>

<details>

<summary>
  CSS Validation results
</summary>

![image](https://github.com/user-attachments/assets/7550643d-f133-4fa1-9c4a-1538cd949c0f)

</details>

<details>

<summary>
  Javascript Validation results
</summary>

comments.js

![image](https://github.com/user-attachments/assets/286344a3-3911-4715-963b-aa1a6abfa4e9)

recipe.js

![image](https://github.com/user-attachments/assets/95372341-18a4-4ff8-8d13-8f1ad2d4676a)

ingredient.js

![image](https://github.com/user-attachments/assets/8bdd57f5-efd2-4c16-a47e-dba1b14c61bb)

</details>

<details>

<summary>
  Python validation results (using pylint python package)
  - I installed pylint-django plugin however it was not loading properly so there are some extra errors in the below validations.
</summary>

admin.py

![image](https://github.com/user-attachments/assets/51249a64-e110-4456-9c4f-37c587c1feb4)

apps.py

![image](https://github.com/user-attachments/assets/22bdac18-fa95-41c1-a827-20aaa8dd756a)

forms.py

![image](https://github.com/user-attachments/assets/24137cef-1629-4a2a-b0e7-45409685df13)

models.py

![image](https://github.com/user-attachments/assets/77c0c146-2a84-4f9b-aedc-c961aa551979)

tests.py (empty file)

![image](https://github.com/user-attachments/assets/be9a8e36-e36d-481d-b1a0-0e6e651b1130)

application urls.py

![image](https://github.com/user-attachments/assets/27c96e57-f43e-4302-a2cc-8ff4a47d2e77)

project urls.py

![image](https://github.com/user-attachments/assets/2b3eb349-7dd4-4406-abe2-4c37340fc4b7)

utils.py

![image](https://github.com/user-attachments/assets/ad8f060f-d1b6-4e21-a664-dad9a0bc9974)

views.py

![image](https://github.com/user-attachments/assets/9f86e2cf-ec23-42bc-a4f6-a2e2d264840e)

project settings.py

![image](https://github.com/user-attachments/assets/58d3c370-f2fc-4114-b45e-392e116bd606)

</details>

 <br>

 ### Manual testing
 
[View manual testing information here](https://docs.google.com/spreadsheets/d/17eki5aLwpNXDlhZGnxaR6NBz9wlyCZT5G-DFvnarZbk/edit?usp=sharing)


 <br>

## Deployment

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next select your region.
- Click on the Create App button.

### Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file:
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py
- Add Edamam ID and Key Id to env.py
- Add the cloudinary libraries to the list of installed apps.
- Add the STATIC filepath
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost'] (or if using gitpod change localhost to gitpod host)

### Create files / directories
- Create requirements.txt file
- Create two directories in the main directory; static, and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi

### Update Heroku Config Vars
- Add all your environment variables from your env.py file as Heroku config vars

### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and click Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click Open App at top of page to view the deployed site. (You can also access this link directly from GitHub.)

The site is now live and operational.

 <br>

## Technologies Used

 <br>
 
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Jquery](https://jquery.com/)
-   [Python](https://www.python.org/)
-   [Google Fonts:](https://fonts.google.com/) used for the Lato font
-   [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
-   [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) is used as the respository for the project code after being pushed from Git. In addition, for this project GitHub was used for the agile development aspect through the use of User Stories (GitHub Issues) and tracking them on a Kanban board.
-   [Lucid app](https://lucid.app) was used to create the Entity Relationship Diagrams for the application data model
-   [Balsamiq:](https://balsamiq.com/) was used to create the wireframes during the design process.
-   [Django](https://www.djangoproject.com/) was used as the framework to support rapid and secure development of the application
-   [Bootstrap](https://getbootstrap.com/) was used to build responsive web pages
-   [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku
-   [Postgres database] Postgres database used for storing data
-   [psycopg2](https://pypi.org/project/psycopg2/) database adapter used to support the connection to the postgres db
-   [Cloudinary](https://cloudinary.com/) used to store the images used by the application
-   [Summernote](https://pypi.org/project/django-summernote/) used to provide WYSIWYG editing on the Hike editing screen
-   [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) used for account registration and authentication
-   [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to simplify form rendering
-   [jquery library](https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js) used to fade out alert messages
  
 <br>
 
## Credits

- Massive thanks to Elaine Roche at the Code Institute
- I followed the 'I Think Therefore I Blog' walkthrough from Code Institute
- Thanks to my son Prabhat for his help with python
- To a prior Code Institute student AliOKeeffe for inspiration
- Stack Overflow for helping with code errors and solutions
- ChatGPT for helping to understand code
- DeepAi for generating images

 <br>

## Known bugs
- Recipe description is not being cleaned at the moment prior to saving. I have assumed the recipe description will be safe when I present it but I should explictly cleaning it to prevent HTML injection into my app.
- Ingredient formset in add recipe page does not appear correctly when adding new ingredients (more than 3 box's available). Further investigation is required to figure out what is causing this.

 <br>

### Important Notice - 20 September 2024

- I recently discovered that a sensitive secret key was unintentionally left exposed in the "settings.py" file. This has been rectified by newly created secret key added to environment variables. The exposed secret key has been removed from the settings.py. 

 <br>
 
## Future features ##
 - Clean recipe description prior to saving in the database.
 - Save nutritional information in the database when recipe is created or edited rather than when the page is refreshed to save on external API calls.
 - Search functionality could be added, allowing users to find recipes based on specific ingredients or recipe names.
 - Give users the option to save recipes to their favourities for quicker access in the future.
 - Implement an auto-complete feature for ingredients within the recipe form. Also enforce better uniqueness of ingredients to prevent mis-spelt ingredients being saved.
 - Change the recipe field in the create meal plan form to a dropdown menu with checkboxes.
  
