let username = ""
function validateLogin() {
    console.log(document.forms);
    var x = document.forms["loginForm"]["username"].value;
    username = x
    if (x == "sd" || x == null) {
      alert("Name must be filled out");
      return false;
    }
    loggedIn = true
    return true
  }

function getUsername() {
    document.getElementById("greetings").innerText = "Hello " + username + "!"
}

