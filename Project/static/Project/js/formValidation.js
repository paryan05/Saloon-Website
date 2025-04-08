// static/js/formValidation.js

document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.getElementById("contactForm");

    // Event listeners for real-time validation
    document.getElementById("name").addEventListener("input", validateName);
    document.getElementById("number").addEventListener("input", validateNumber);
    document.getElementById("email").addEventListener("input", validateEmail);
    document.getElementById("services").addEventListener("change", validateServices);
    document.getElementById("message").addEventListener("input", validateMessage);

    contactForm.addEventListener("submit", function (event) {
        // Prevent form submission if validation fails
        if (!validateForm()) {
            event.preventDefault();
        }
    });

    function validateForm() {
        let isValid = true;
        if (!validateName()) isValid = false;
        if (!validateNumber()) isValid = false;
        if (!validateEmail()) isValid = false;
        if (!validateServices()) isValid = false;
        if (!validateMessage()) isValid = false;
        return isValid;
    }

    function showErrorMessage(element, message) {
        let errorElement = element.nextElementSibling;
        if (!errorElement || !errorElement.classList.contains("error-message")) {
            errorElement = document.createElement("span");
            errorElement.classList.add("error-message");
            element.after(errorElement);
        }
        errorElement.textContent = message;
        element.classList.add("input-error");
    }

    function clearErrorMessage(element) {
        let errorElement = element.nextElementSibling;
        if (errorElement && errorElement.classList.contains("error-message")) {
            errorElement.textContent = "";
        }
        element.classList.remove("input-error");
    }

    // Name Validation
    function validateName() {
        const name = document.getElementById("name");
        const nameValue = name.value.trim();
        if (!/^[a-zA-Z\s]+$/.test(nameValue) || nameValue === "") {
            showErrorMessage(name, "Please enter a valid name (only alphabets).");
            return false;
        }
        clearErrorMessage(name);
        return true;
    }

    // Number Validation
    function validateNumber() {
        const number = document.getElementById("number");
        const numberValue = number.value.trim();
        if (!/^\d{10}$/.test(numberValue)) {
            showErrorMessage(number, "Please enter a valid 10-digit phone number.");
            return false;
        }
        clearErrorMessage(number);
        return true;
    }

    // Email Validation
    function validateEmail() {
        const email = document.getElementById("email");
        const emailValue = email.value.trim();
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(emailValue)) {
            showErrorMessage(email, "Please enter a valid email address.");
            return false;
        }
        clearErrorMessage(email);
        return true;
    }

    // Services Validation
    function validateServices() {
        const services = document.getElementById("services");
        if (services.value === "#") {
            showErrorMessage(services, "Please select a service.");
            return false;
        }
        clearErrorMessage(services);
        return true;
    }

    // Message Validation
    function validateMessage() {
        const message = document.getElementById("message");
        const messageValue = message.value.trim();
        if (messageValue === "") {
            showErrorMessage(message, "Please enter a message.");
            return false;
        }
        clearErrorMessage(message);
        return true;
    }
});
