function checkpass(){
    // Check for password length
    var user = document.getElementById("id_username").value
    if(user.length < 3){
        alert("Error: usernames must be at least 3 characters long");
        event.preventDefault();
        return("done");
    }

    // Check for a valid BLM or USGS email address
    var email = document.getElementById("id_email").value
    var emailexst = email.search("@");
    if(emailexst == -1){
        emailexst = email.search("@");
    }
    if(emailexst == -1) {
        alert("Error: A valid email address is required for registration");
        event.preventDefault();
        return("done");
    }

    // Check for matching passwords
    if(document.getElementById("id_password1").value != document.getElementById("id_password2").value){
        alert("Error: Passwords do not match");
        event.preventDefault();
        return("done");
    }

    // Check for password length
    var pass = document.getElementById("id_password1").value
    if(pass.length < 12){
        alert("Error: Passwords muct be at least 12 characters long");
        event.preventDefault();
        return("done");
    }
    // Check for lower case letter
    if(pass.toUpperCase() != pass) {
    }else{
        alert("Error: At least 1 lower case letter is required");
        event.preventDefault();
        return("done");
    }
    // Check for upper case letter
    if(pass.toLowerCase() != pass) {
    }else{
        alert("Error: At least 1 upper case letter is required");
        event.preventDefault();
        return("done");
    }

    // Check for number
    var hasNumber = /\d/;
    if(hasNumber.test(pass) == false){
        alert("Error: At least 1 number is required");
        event.preventDefault();
        return("done");
    }
    
    // Check for special character
    var hasSpecial = /[~`!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/;
    if(hasSpecial.test(pass) == false){
        alert("Error: At least 1 special character is required");
        event.preventDefault();
        return("done");
    }

    // document.getElementById("registration_form").submit();
}


function checkpass1(){
    
    // Check for matching passwords
    if(document.getElementById("id_new_password1").value != document.getElementById("id_new_password2").value){
        alert("Error: Passwords do not match");
        event.preventDefault();
        return("done");
    }

    // Check for password length
    var pass = document.getElementById("id_new_password1").value
    if(pass.length < 12){
        alert("Error: Passwords muct be at least 12 characters long");
        event.preventDefault();
        return("done");
    }
    // Check for lower case letter
    if(pass.toUpperCase() != pass) {
    }else{
        alert("Error: At least 1 lower case letter is required");
        event.preventDefault();
        return("done");
    }
    // Check for upper case letter
    if(pass.toLowerCase() != pass) {
    }else{
        alert("Error: At least 1 upper case letter is required");
        event.preventDefault();
        return("done");
    }

    // Check for number
    var hasNumber = /\d/;
    if(hasNumber.test(pass) == false){
        alert("Error: At least 1 number is required");
        event.preventDefault();
        return("done");
    }
    
    // Check for special character
    var hasSpecial = /[~`!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/;
    if(hasSpecial.test(pass) == false){
        alert("Error: At least 1 special character is required");
        event.preventDefault();
        return("done");
    }

    // document.getElementById("registration_form").submit();
}

function checkpass2(){

        // Check for matching passwords
        if(document.getElementById("id_new_password1").value != document.getElementById("id_new_password2").value){
            alert("Error: Passwords do not match");
            event.preventDefault();
            return("done");
        }

        // Check for password length
        var pass = document.getElementById("id_new_password1").value
        if(pass.length < 12){
            alert("Error: Passwords muct be at least 12 characters long");
            event.preventDefault();
            return("done");
        }
        // Check for lower case letter
        if(pass.toUpperCase() != pass) {
        }else{
            alert("Error: At least 1 lower case letter is required");
            event.preventDefault();
            return("done");
        }
        // Check for upper case letter
        if(pass.toLowerCase() != pass) {
        }else{
            alert("Error: At least 1 upper case letter is required");
            event.preventDefault();
            return("done");
        }

        // Check for number
        var hasNumber = /\d/;
        if(hasNumber.test(pass) == false){
            alert("Error: At least 1 number is required");
            event.preventDefault();
            return("done");
        }
        
        // Check for special character
        var hasSpecial = /[~`!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/;
        if(hasSpecial.test(pass) == false){
            alert("Error: At least 1 special character is required");
            event.preventDefault();
            return("done");
        }

        document.getElementById("passwordreset_form").submit();
    }