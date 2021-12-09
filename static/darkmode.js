const themeChanger = document.querySelector('.themeswap input[type="checkbox"]');
const pageTheme = localStorage.getItem("colors");

if (pageTheme) 
{
    document.documentElement.setAttribute("new-theme", pageTheme);
    if (pageTheme === "darkmode") {
        themeChanger.checked = true;
    }
}

function switchTheme(e) 
{
    if (e.target.checked) 
    {
        document.documentElement.setAttribute("new-theme", "darkmode");
        localStorage.setItem("colors", "darkmode");
    } 
    else 
    {
        document.documentElement.setAttribute("new-theme", "lightmode");
        localStorage.setItem("colors", "lightmode");
    }
}
themeChanger.addEventListener("change", switchTheme, false);
  