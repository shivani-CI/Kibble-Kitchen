const deleteRecipeButton = document.querySelector('#delete-recipe-btn');
const recipeId = deleteRecipeButton.getAttribute('data-recipe-id');
const addToMealPlanButton = document.querySelector('#add-recipe-to-meal-plan-btn');
const mealPlanModal = new bootstrap.Modal(document.getElementById("mealPlanModal"));
const mealPlanDropdown = document.getElementById("meal_plan_dropdown");
const confirmAddToMealPlanButton = document.getElementById("confirm_add_to_meal_plan_btn");


function displayMessage(message, type) {
    const messageContainer = document.getElementById('message-container');
    messageContainer.innerHTML = `
        <div class="alert alert-${type} alert-dismissible fade show" id="msg" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    `;
}

deleteRecipeButton.addEventListener("click", function() {
    deleteConfirm.href = `/delete_recipe/${recipeId}`;
    deleteModal.show();
});

addToMealPlanButton.addEventListener("click", function() {
    mealPlanModal.show();
});

confirmAddToMealPlanButton.addEventListener("click", function() {
    const mealPlanId = mealPlanDropdown.value;

    fetch(`/meal_plan-add_recipe`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({
            'meal_plan_id': mealPlanId,
            'recipe_id': recipeId
        })
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Failed to add recipe to meal plan.');
        }
    }).then(data => {
        mealPlanModal.hide();
        if (data.success) {
            displayMessage(data.message, 'success');
        } else {
            displayMessage(data.message, 'error');
        }
    });
});