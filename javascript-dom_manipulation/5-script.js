function myScript() {
    const element = document.querySelector("header");
    element.textContent = "New Header!!!";
  }
  document.getElementById("update_header").addEventListener("click", myScript);
  