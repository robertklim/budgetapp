(function(){
    document.querySelector('#categoryInput').addEventListener('keydown', function(e){
        if (e.keyCode != 13) {
            return;
        }

        e.preventDefault();

        let categoryName = this.value;
        this.value = '';
        addNewCategory(categoryName);
        updateCategoryString();
    })

    function addNewCategory(name) {
        document.querySelector('#categoriesContainer').insertAdjacentHTML('beforeend', `
            <li class="category">
                <div class="card-panel category-list-element">
                    <span class="name">${name}</span>
                    <span onclick="removeCategory(this)" class="btnRemove">
                        <i class="material-icons red-text right">close</i>
                    </span>
                </div>
            </li>
        `);
    }

})()

function fetchCategoryArray() {
    let categories = [];
    document.querySelectorAll('.category').forEach(function (e) {
        name = e.querySelector('.name').innerHTML;
        if (name == '') return;

        categories.push(name);
    });
    return categories;
}

function updateCategoryString() {
    categories = fetchCategoryArray();
    document.querySelector('input[name="categoriesString"]').value = categories.join(',');
}

function removeCategory(e) {
    e.parentElement.parentElement.remove();
    updateCategoryString();
}