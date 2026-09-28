class PasswordPolicy:

    def __init__(
        self,
        min_length=8,
        require_uppercase=True,
        require_lowercase=True,
        require_digit=True,
        require_special=True
    ):
        if min_length < 1:
            raise ValueError("Minimum length must be at least 1")

        self.min_length = min_length
        self.require_uppercase = require_uppercase
        self.require_lowercase = require_lowercase
        self.require_digit = require_digit
        self.require_special = require_special

    def check(self, password):
        errors = []

        if len(password) < self.min_length:
            errors.append(
                f"Password must contain at least {self.min_length} characters"
            )

        if self.require_uppercase and not any(c.isupper() for c in password):
            errors.append("Password must contain an uppercase letter")

        if self.require_lowercase and not any(c.islower() for c in password):
            errors.append("Password must contain a lowercase letter")

        if self.require_digit and not any(c.isdigit() for c in password):
            errors.append("Password must contain a digit")

        special_characters = "!@#$%^&*()-_=+[]{};:',.<>?/\\|`~"

        if self.require_special and not any(
            c in special_characters for c in password
        ):
            errors.append("Password must contain a special character")

        return errors

    def is_valid(self, password):
        return len(self.check(password)) == 0