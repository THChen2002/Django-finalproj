var editButton = document.getElementById("edit-button");
var saveButton = document.getElementById("save-button");
var emailInput = document.getElementById("email");
var firstNameInput = document.getElementById("first_name");
var lastNameInput = document.getElementById("last_name");
var addressInput = document.getElementById("address");
var genderInput = document.getElementById("gender");
var genderTextMInput = document.getElementById("gender_textM");
var genderTextFInput = document.getElementById("gender_textF");
var genderMInput = document.getElementById("gender_M");
var genderFInput = document.getElementById("gender_F");
var birthdateInput = document.getElementById("birth_date")
var phoneInput = document.getElementById("phone_number");

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
        alert("上傳成功!")
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
    addressInput.readOnly = false;
    genderInput.readOnly = false;
    genderTextMInput.style.display = "inline-block";
    genderTextFInput.style.display = "inline-block";
    genderMInput.disabled = false;
    genderInput.style.display = "none";
    genderMInput.style.display = "inline-block";
    genderFInput.disabled = false;
    genderFInput.style.display = "inline-block";
    birthdateInput.readOnly = false;
    phoneInput.readOnly = false;
}

function toggleViewMode() {
    editButton.style.display = "block";
    saveButton.style.display = "none";
    emailInput.readOnly = true;
    firstNameInput.readOnly = true;
    lastNameInput.readOnly = true;
    addressInput.readOnly = true;
    genderInput.readOnly = true;
    genderTextMInput.style.display = "none";
    genderTextFInput.style.display = "none";
    genderMInput.disabled = true;
    genderInput.style.display = "block";
    genderMInput.style.display = "none";
    genderFInput.disabled = true;
    genderFInput.style.display = "none";
    birthdateInput.readOnly = true;
    phoneInput.readOnly = true;
}

function submitData() {
    var email = document.getElementById("email").value;
    var firstName = document.getElementById("first_name").value;
    var lastName = document.getElementById("last_name").value;
    var address = document.getElementById("address").value;
    var gender = document.getElementById("gender");
    var genderM = document.getElementById("gender_M");
    var genderF = document.getElementById("gender_F");
    var birthdate = document.getElementById("birth_date").value;
    var phone = document.getElementById("phone_number").value;
    if(genderM.checked){
        gender.value = 'M';
    }else if(genderF.checked){
        gender.value = 'F';
    }else{
        gender.value = '';
    }
    alert("edit success!")
    var dataToSend = {'email': email, 'first_name': firstName, 'last_name': lastName, 'address': address, 'gender': gender.value, 'birth_date': birthdate, 'phone_number': phone};
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
        addressInput.value = data.address;
        genderInput.value = data.gender;
        birthdateInput.value = data.birthdate;
        phoneInput.value = data.phone_number;
    })
    .catch(error => console.error(error));
    
}