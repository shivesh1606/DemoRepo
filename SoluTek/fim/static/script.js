(function () {
  function scroller() {
    let scroll = $("div.scroll");

    let height = scroll.height();

    let topAdj = -height - 30;
    scroll.animate(
      {
        top: [topAdj, "linear"],
      },
      10000,
      function () {
        scroll.css("top", 400);
        scroller();
      }
    );
  }

  scroller();
})();

const slider = document.querySelector(".items");
let isDown = false;
let startX;
let scrollLeft;

slider.addEventListener("mousedown", (e) => {
  isDown = true;
  slider.classList.add("active");
  startX = e.pageX - slider.offsetLeft;
  scrollLeft = slider.scrollLeft;
});
slider.addEventListener("mouseleave", () => {
  isDown = false;
  slider.classList.remove("active");
});
slider.addEventListener("mouseup", () => {
  isDown = false;
  slider.classList.remove("active");
});
slider.addEventListener("mousemove", (e) => {
  if (!isDown) return;
  e.preventDefault();
  const x = e.pageX - slider.offsetLeft;
  const walk = (x - startX) * 3; //scroll-fast
  slider.scrollLeft = scrollLeft - walk;
  console.log(walk);
});


//about us page

// page navigation variables
// const navigationLinks = document.querySelectorAll("[data-nav-link]");
// const pages = document.querySelectorAll("[data-page]");
// console.log(navigationLinks,pages)

// // add event to all nav link
// for (let i = 0; i < navigationLinks.length; i++) {
//   console.log(navigationLinks,pages)
//   navigationLinks[i].addEventListener("click", function () {
//     for (let i = 0; i < pages.length; i++) {
//       if (this.innerHTML.toLowerCase() === pages[i].dataset.page) {
//         pages[i].classList.add("active");
//         navigationLinks[i].classList.add("active");
//         window.scrollTo(0, 0);
//       } else {
//         pages[i].classList.remove("active");
//         navigationLinks[i].classList.remove("active");
//       }
//     }

//   });
// }


var divs = ["fim", "founder", "director", "mentor", "core"];
var visibleDivId = null;
var currDiv ='fim'
function divVisibility(divId) {
  var temp = divId + 'Div';
  var divv = document.getElementById(temp)
  divv.style.background = "#3EC2FB";
  divv.style.color = "white"
  if(currDiv===divId){

  }
  else{
    if (visibleDivId === divId) {
      visibleDivId = null;
    } else {
      visibleDivId = divId;
    }
    hideNonVisibleDivs();
    currDiv = divId
  }
}
function hideNonVisibleDivs() {
  var divs = ["fim", "founder", "director", "mentor", "core"];
  var i, divId, div;
  for (i = 0; i < 5; i++) {
    divId = divs[i];
    div = document.getElementById(divId);
    if (visibleDivId === divId) {
      div.style.display = "flex";
    } else {
      div.style.display = "none";
      var temp = divId + 'Div';
      var divv = document.getElementById(temp)
      divv.style.background = "none";
      divv.style.color = "#475569"
    }
  }
}