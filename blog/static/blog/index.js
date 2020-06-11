const nav_bar = document.querySelector("header");
const logo = document.querySelector(".logo");
window.onscroll = function () {
  shrinkOnScroll();
};

function shrinkOnScroll() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    nav_bar.style.padding = "8px";
    nav_bar.style.backgroundColor = "yellow";
    nav_bar.style.opacity = "none";
  } else {
    nav_bar.style.padding = "20px";
    nav_bar.style.backgroundColor = "yellow";
  }
}
