function validateLogin() {
    console.log(document.forms);
    var x = document.forms["loginForm"]["username"].value;
    if (x == "sd" || x == null) {
      alert("Name must be filled out");
      return false;
    }
    loggedIn = true
    return true
  }