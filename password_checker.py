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
        has_pattern = self.has_common_pattern(password)

        if is_common:
            errors.append("Password is a commonly used password")

        if has_pattern and not is_common:
            errors.append("Password contains a common pattern")

        strength = self.get_strength(entropy)

        if is_common or has_pattern:
            strength = "Very Weak"

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "entropy": entropy,
            "strength": strength,
            "is_common": is_common,
            "has_pattern": has_pattern
        }

    def is_common_password(self, password):
        return password.lower() in self.COMMON_PASSWORDS

    def has_common_pattern(self, password):
        if len(password) < 4:
            return False

        if len(set(password)) == 1:
            return True

        increasing = True
        decreasing = True

        for i in range(1, len(password)):
            difference = ord(password[i]) - ord(password[i - 1])

            if difference != 1:
                increasing = False

            if difference != -1:
                decreasing = False

        if increasing or decreasing:
            return True

        return False

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