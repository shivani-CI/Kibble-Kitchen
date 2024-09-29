const editButtons = document.getElementsByClassName("btn-edit");
const recipeText = document.getElementById("id_description");
const recipeForm = document.getElementById("RecipeForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated recipe's ID upon click.
* - Fetches the description of the corresponding recipe.
* - Populates the `recipeText` input/textarea with the recipe's description for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_recipe/{recipeId}` endpoint.
*/
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let recipe_Id = e.target.getAttribute("data-recipe_id");
        let recipeContent = document.getElementById(`recipe${recipeId}`).innerText;
        recipeText.value = recipeContent;
        submitButton.innerText = "Update";
        recipeForm.setAttribute("action", `edit_recipe/${recipeId}`);
    });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let recipeId = e.target.getAttribute("data-recipe_id");
        deleteConfirm.href = `delete_recipe/${recipeId}`;
        deleteModal.show();
    });
}