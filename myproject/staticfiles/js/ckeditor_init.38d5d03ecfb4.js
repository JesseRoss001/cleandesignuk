// static/js/ckeditor_init.js

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.django-admin-textarea').forEach(function(element) {
        ClassicEditor.create(element)
            .catch(error => {
                console.error(error);
            });
    });
});
