var editButton = document.getElementById("edit-button");
var saveButton = document.getElementById("save-button");
var emailInput = document.getElementById("email");
var firstNameInput = document.getElementById("first-name");
var lastNameInput = document.getElementById("last-name");

const photoForm = document.querySelector('#photo-form');
const photoInput = document.querySelector('#photo');

photoInput.addEventListener('change', () => {
    const maxSize = 2 * 1024 * 1024; // 5MB (以位元組為單位)
    const file = photoInput.files[0];
    if (file.size > maxSize) {
        alert('上傳的檔案大小超過2MB，請選擇更小的檔案!');
        fileInput.value = ''; // 清除選擇的檔案
        return;
    }
    const dataToSend = new FormData();
    dataToSend.append('photo', file);
    dataToSend.append('form_id', 'photo-form');
    const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    fetch(photoUrl, {
        method: 'POST',
        headers: {'X-CSRFToken': csrfToken},
        body: dataToSend
    }).then(response => {
        console.log(response);
        // Handle response from server
    }).catch(error => {
        console.error(error);
    });
});

function toggleEditMode() {
    editButton.style.display = "none";
    saveButton.style.display = "block";
    emailInput.readOnly = false;
    firstNameInput.readOnly = false;
    lastNameInput.readOnly = false;
}

function toggleViewMode() {
    editButton.style.display = "block";
    saveButton.style.display = "none";
    emailInput.readOnly = true;
    firstNameInput.readOnly = true;
    lastNameInput.readOnly = true;
}

function submitData(form_id) {
    if (form_id == 'profile-form'){
        alert('profile');
        var email = document.getElementById("email").value;
        var firstName = document.getElementById("first-name").value;
        var lastName = document.getElementById("last-name").value;
        var dataToSend = {'email': email, 'first_name': firstName, 'last_name': lastName};
        var csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

        fetch(profileUrl, {
            method: 'POST',
            headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken},
            body: JSON.stringify({'data': dataToSend})
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            toggleViewMode();
            emailInput.value = data.email;
            firstNameInput.value = data.first_name;
            lastNameInput.value = data.last_name;
        })
        .catch(error => console.error(error));
    }
}