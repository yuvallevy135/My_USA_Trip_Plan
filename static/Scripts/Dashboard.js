const username = "yuval"

document.getElementById("greeting").innerText = "Hello " + username + "!"
document.getElementById("tripsHeadline").innerText = "Saved trips:"

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  if (acc[i] == undefined)
    continue
    
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}


