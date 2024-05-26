document.getElementById("donorForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var name = document.getElementById("name").value;
    var age = document.getElementById("age").value;
    var gender = document.getElementById("gender").value;
    var bloodType = document.getElementById("bloodType").value;
    var contactInfo = document.getElementById("contactInfo").value;
    var lastDonationDate = document.getElementById("lastDonationDate").value;
    var medicalHistory = document.getElementById("medicalHistory").value;

    var donorData = {
        name: name,
        age: age,
        gender: gender,
        bloodType: bloodType,
        contactInfo: contactInfo,
        lastDonationDate: lastDonationDate,
        medicalHistory: medicalHistory
    };

    console.log( donorData );

    fetch('/add_donor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(donorData)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => { 
        console.error('Error:', error);
    });
}); 

function searchRecipients() {
    var bloodType = document.getElementById("bloodTypeSearch").value;

    var searchData = {
        bloodType: bloodType
    };

    fetch('/search_recipients', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(searchData)
    })
    .then(response => response.json())
    .then(recipients => {
        var recipientList = document.getElementById("recipientList");
        recipientList.innerHTML = "<h3>Recipients with Blood Type " + bloodType + "</h3>";

        recipients.forEach(function(recipient) {
            recipientList.innerHTML += "<p>Name: " + recipient.Name + ", Age: " + recipient.Age + ", Blood Type: " + recipient.Blood_Type + ", Contact Info: " + recipient.Contact_Info + ", Hospital: " + recipient.Hospital + "</p>";
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
//login in page......

document.getElementById("login-container").addEventListener("submit", function(event) {
    event.preventDefault();
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    var loginData = {
        username: username,
        password: password
    };
