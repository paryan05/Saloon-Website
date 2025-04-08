let menuToggle = document.querySelector('.menuToggle');
let header = document.querySelector('header');
let section = document.querySelector('section');
// let section = document.getElementsByTagName('*');
menuToggle.onclick = function () {
    header.classList.toggle('active')
    section.classList.toggle('active')
}
const slides = document.querySelectorAll('.slide');
let counter = 0;
// console.log(i)
slides.forEach((slide, index) => {
    slide.style.left = `${index * 100}%`

});

const goPrev = () => {
    counter--
    slideImg()
}
const goNext = () => {
    counter++
    slideImg()
}


const slideImg = () => {
    for (let i = 0; i < slides.length; i++) {
        if (counter >= slides.length) {
            slides.forEach(slide => {
                slide.style.transform = `translateX(-${counter * 0}%)`
            });
        } else {
            slides.forEach(slide => {
                slide.style.transform = `translateX(-${counter * 100}%)`
            });
        }
    }
}


// popup
const signInPopup = document.getElementById("signInPopup");
const signUpPopup = document.getElementById("signUpPopup");

// Get the buttons
const logInButton = document.getElementById("LogIn");
const closeSignInButton = document.getElementById("closeSignIn");
const closeSignUpButton = document.getElementById("closeSignUp");
const openSignUpButton = document.getElementById("openSignUp");
const openSignInButton = document.getElementById("openSignIn");

// Function to open Sign In popup
logInButton.onclick = function () {
    signInPopup.style.display = "flex"; // Show Sign In Popup
};

// Function to close Sign In popup
closeSignInButton.onclick = function () {
    signInPopup.style.display = "none"; // Hide Sign In Popup
};

// Function to open Sign Up popup
openSignUpButton.onclick = function (event) {
    event.preventDefault(); // Prevent default link action
    signInPopup.style.display = "none"; // Hide Sign In Popup
    signUpPopup.style.display = "flex"; // Show Sign Up Popup
};

// Function to close Sign Up popup
closeSignUpButton.onclick = function () {
    signUpPopup.style.display = "none"; // Hide Sign Up Popup
};

// Function to open Sign In from Sign Up
openSignInButton.onclick = function (event) {
    event.preventDefault(); // Prevent default link action
    signUpPopup.style.display = "none"; // Hide Sign Up Popup
    signInPopup.style.display = "flex"; // Show Sign In Popup
};

// Close the popups when clicking outside of them
window.onclick = function (event) {
    if (event.target === signInPopup) {
        signInPopup.style.display = "none"; // Hide Sign In Popup
    }
    if (event.target === signUpPopup) {
        signUpPopup.style.display = "none"; // Hide Sign Up Popup
    }
};

window.onload = function() {
    // Check if the URL contains '#'
    if (window.location.hash === '#') {
        showPopup('signInPopup'); // Show the Sign In popup
    }
};
window.onclick = function(event) {
    const signInPopup = document.getElementById('signInPopup');
    const signUpPopup = document.getElementById('signUpPopup');

    if (event.target === signInPopup) {
        closePopup('signInPopup'); // Hide Sign In Popup
    }
    if (event.target === signUpPopup) {
        closePopup('signUpPopup'); // Hide Sign Up Popup
    }
};

function showPopup(popupId) {
    document.getElementById(popupId).style.display = "block"; // Show the specified popup
}

function closePopup(popupId) {
    document.getElementById(popupId).style.display = "none"; // Hide the specified popup
}