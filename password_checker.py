from policy import PasswordPolicy
from entropy import EntropyCalculator


class PasswordChecker:

    COMMON_PASSWORDS = {
        "password",
        "password123",
        "123456",
        "12345678",
        "123456789",
        "qwerty",
        "qwerty123",
        "admin",
        "admin123",
        "welcome",
        "welcome123",
        "letmein",
        "iloveyou"
    }

    def __init__(self):
        self.policy = PasswordPolicy()
        self.entropy_calculator = EntropyCalculator()

    def check_password(self, password):
        errors = self.policy.check(password)
        entropy = self.entropy_calculator.calculate(password)

        is_common = self.is_common_password(password)

        if is_common:
            errors.append("Password is a commonly used password")

        strength = self.get_strength(entropy)

        if is_common:
            strength = "Very Weak"

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "entropy": entropy,
            "strength": strength,
            "is_common": is_common
        }

    def is_common_password(self, password):
        return password.lower() in self.COMMON_PASSWORDS

    def get_strength(self, entropy):
        if entropy < 28:
            return "Very Weak"
        elif entropy < 36:
            return "Weak"
        elif entropy < 60:
            return "Moderate"
        elif entropy < 80:
            return "Strong"
        else:
            return "Very Strong"