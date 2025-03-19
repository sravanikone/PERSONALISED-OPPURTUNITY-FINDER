document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        const name = document.getElementById('name').value.trim();
        const skills = document.getElementById('skills').value.trim();
        const interests = document.getElementById('interests').value.trim();
        const location = document.getElementById('location').value.trim();

        if (!name || !skills || !interests || !location) {
            alert('Please fill in all the required fields.');
            event.preventDefault();
        }
    });
});