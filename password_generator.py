import secrets
import string


class PasswordGenerator:

    def generate(
        self,
        length=16,
        include_uppercase=True,
        include_lowercase=True,
        include_digits=True,
        include_special=True
    ):
        character_sets = []

        if include_uppercase:
            character_sets.append(string.ascii_uppercase)

        if include_lowercase:
            character_sets.append(string.ascii_lowercase)

        if include_digits:
            character_sets.append(string.digits)

        if include_special:
            character_sets.append(string.punctuation)

        if not character_sets:
            raise ValueError("At least one character type must be selected")

        if length < len(character_sets):
            raise ValueError(
                "Password length is too short for the selected character types"
            )

        password = []

        for character_set in character_sets:
            password.append(secrets.choice(character_set))

        all_characters = "".join(character_sets)

        while len(password) < length:
            password.append(secrets.choice(all_characters))

        secrets.SystemRandom().shuffle(password)

        return "".join(password)