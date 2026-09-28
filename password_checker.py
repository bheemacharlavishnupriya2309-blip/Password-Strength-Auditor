from policy import PasswordPolicy
from entropy import EntropyCalculator


class PasswordChecker:

    def __init__(self):
        self.policy = PasswordPolicy()
        self.entropy_calculator = EntropyCalculator()

    def check_password(self, password):
        errors = self.policy.check(password)
        entropy = self.entropy_calculator.calculate(password)

        strength = self.get_strength(entropy)

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "entropy": entropy,
            "strength": strength
        }

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