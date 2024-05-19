document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("myForm");

    const validationRules = {
        name: {
            required: true,
            minLength: 3,
            maxLength: 20,
            pattern: /^[a-zA-Z\s]+$/
        },
        email: {
            required: true,
            pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/
        },
        password: {
            required: true,
            minLength: 6,
            maxLength: 20,
            pattern: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/
        },
        confirmPassword: {
            required: true,
            matchWith: 'password'
        }
    };

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        let isValid = true;
        const formData = new FormData(form);

        for (const [field, rules] of Object.entries(validationRules)) {
            const input = form.elements[field];
            const errorMessage = validateField(input, rules, formData);
            const errorSpan = input.nextElementSibling;

            if (errorMessage) {
                errorSpan.textContent = errorMessage;
                isValid = false;
            } else {
                errorSpan.textContent = "";
            }
        }

        if (isValid) {
            alert("Form submitted successfully!");
            form.reset();
        }
    });

    function validateField(input, rules, formData) {
        const value = input.value.trim();

        if (rules.required && !value) {
            return `${input.name} is required.`;
        }

        if (rules.minLength && value.length < rules.minLength) {
            return `${input.name} must be at least ${rules.minLength} characters long.`;
        }

        if (rules.maxLength && value.length > rules.maxLength) {
            return `${input.name} must be no more than ${rules.maxLength} characters long.`;
        }

        if (rules.pattern && !rules.pattern.test(value)) {
            return `Invalid ${input.name}.`;
        }

        if (rules.matchWith) {
            const matchValue = formData.get(rules.matchWith);
            if (value !== matchValue) {
                return `${input.name} does not match ${rules.matchWith}.`;
            }
        }

        return null;
    }
});
