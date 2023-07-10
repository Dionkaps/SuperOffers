//Sinartisi elegxou olwn twn pediwn gia na ginei enable to koumpi sign up
function inputCheckFunction(inputPass,inputFname,inputLname,inputEmail) {
  const signUpBtn = document.getElementById('signUpbtn');
  if (inputPass.value.length > 0 && inputFname.value.length > 0 && inputLname.value.length > 0 && inputEmail.value.length > 0) {
    signUpBtn.style.pointerEvents = 'auto';
    signUpBtn.style.opacity = '1';
  } else {
    signUpBtn.style.pointerEvents = 'none';
    signUpBtn.style.opacity = '0.2';
  }
}

//Sinartisi elegxou tou password
function passCheck(inputPass, form) {
  form.action = 'signup.php';
  var passw = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;

  if (inputPass.value.match(passw)) {
    alert('All good, brother');
    form.submit();
  } else {
    alert('Your password must contain at least 8 characters, one uppercase, one number, and one special character');
    event.preventDefault(); //Prevent form submission
  }
}
