function visibleFunction() {
    var x = document.getElementById("pw");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }

function lightTheme(){
  var icon =document.getElementById("icon");
  document.body.classList.toggle("light-theme");
  if(document.body.classList.contains("light-theme")){
    icon.src="../static/images/moon.png";
  }else{
    icon.src="../static/images/sun.png";
  }
}