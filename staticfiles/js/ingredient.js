const addIngredientBtn = document.getElementById("add_ingredient");
const ingredientFormsetTable = document.getElementById("ingredient_formset_tbl");
const totalForms = document.getElementById("id_form-TOTAL_FORMS");
let formCount = parseInt(totalForms.value);


// Add a new ingredient form (row) if the button is clicked
addIngredientBtn.addEventListener("click", function() {
    const newForm = document.querySelector('.ingredient-form').cloneNode(true);
    const regex = new RegExp(`form-(\\d)-`, 'g');
    newForm.innerHTML = newForm.innerHTML.replace(regex, `form-${formCount}-`);
    newForm.querySelectorAll('input').forEach(input => input.value = '');
    ingredientFormsetTable.appendChild(newForm);
    formCount++;
    totalForms.value = formCount;
});

// Function to remove an ingredient form
ingredientFormsetTable.addEventListener("click", function(e) {
    if (e.target && e.target.classList.contains("remove-ingredient-btn")) {
        e.target.closest('tr.ingredient-form').remove();
        formCount--;
        totalForms.value = formCount;
    }
});