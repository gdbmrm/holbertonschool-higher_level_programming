document.getElementById("red_header").addEventListener("click", myScript);

function myScript() {
  if (document.querySelector("header").classList.contains("red")) {
    document.querySelector("header").classList.add("green");
    document.querySelector("header").classList.remove("red");
  } else {
      document.querySelector("header").classList.add("red");
      document.querySelector("header").classList.remove("green");
  }
}
