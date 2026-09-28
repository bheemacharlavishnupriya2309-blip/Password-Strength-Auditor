import math
import string


class EntropyCalculator:

    def calculate(self, password):
        if not password:
            return 0.0

        character_pool = 0

        if any(char.islower() for char in password):
            character_pool += 26

        if any(char.isupper() for char in password):
            character_pool += 26

        if any(char.isdigit() for char in password):
            character_pool += 10

        if any(char in string.punctuation for char in password):
            character_pool += len(string.punctuation)

        if character_pool == 0:
            return 0.0

        return len(password) * math.log2(character_pool)


if __name__ == "__main__":
    calculator = EntropyCalculator()

    password = "Hello@123"

    entropy = calculator.calculate(password)

    print("Password:", password)
    print("Entropy:", entropy)
