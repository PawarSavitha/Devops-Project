// script.js

// Just a basic alert when adding to cart
document.addEventListener('DOMContentLoaded', () => {
    const addButtons = document.querySelectorAll('.add-to-cart');

    addButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            alert('Item added to cart!');
        });
    });
});
