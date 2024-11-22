function myScript() {
  const element = document.createElement("li");
  element.textContent = "Item";
  const liste = document.querySelector(".my_list");
  liste.appendChild(element);
}
document.getElementById("add_item").addEventListener("click", myScript);
