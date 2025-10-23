// Sidebar toggle
const openBtn = document.getElementById("openSidebar");
const closeBtn = document.getElementById("closeSidebar");
const sidebar = document.getElementById("sidebar");

openBtn.addEventListener("click", () => sidebar.classList.add("active"));
closeBtn.addEventListener("click", () => sidebar.classList.remove("active"));

// Theme toggle
const toggle = document.getElementById("theme-toggle");
toggle.addEventListener("click", () => {
  document.body.classList.toggle("dark");
});
