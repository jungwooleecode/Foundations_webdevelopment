function visibleFunction() {
    var x = document.getElementById("pw");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }

function switchDarkLightTheme(){

  function setThemeFromCookie() {
    const themeState = document.getElementById('body');
    themeState.className = isThemeSelected() ? 'dark-theme' : 'light-theme';
  }

  function switchState(){
    document.getElementById('icon').onclick=isThemeSelected();
  }

  function isThemeSelected() {
    return document.cookie.match(/theme=dark/i) != null;
  }

  function toggleTheme() {
    const themeState = document.getElementById('body');
    const currentState = themeState.className;
    const newState = currentState == 'dark-theme' ? 'light-theme' : 'dark-theme';
    if(newState==='light-theme'){
      document.getElementById('icon').src="../static/images/moon.png"
    }else{
      document.getElementById('icon').src="../static/images/sun.png"
    }
    themeState.className = newState;
    document.cookie = 'theme=' + (newState == 'light-theme' ? 'light' : 'dark');
  }

  (function() {
    setThemeFromCookie();
    switchState();
    document.getElementById('icon').onclick=toggleTheme;
  })();
}
