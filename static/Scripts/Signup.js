function validateSignup() {
    console.log(document.forms);
    var x = document.forms["signupForm"]["username"].value;
    if (x == "sd" || x == null) {
      alert("Name must be filled out");
      return false;
    }
  }