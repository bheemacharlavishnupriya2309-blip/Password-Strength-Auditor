from policy import PasswordPolicy
from entropy import EntropyCalculator
from password_checker import PasswordChecker
from password_generator import PasswordGenerator


def test_valid_password():
    policy = PasswordPolicy()
    assert policy.is_valid("Hello@123")


def test_short_password():
    policy = PasswordPolicy()
    assert not policy.is_valid("Hi@1")


def test_missing_uppercase():
    policy = PasswordPolicy()
    errors = policy.check("hello@123")
    assert "Password must contain an uppercase letter" in errors


def test_missing_lowercase():
    policy = PasswordPolicy()
    errors = policy.check("HELLO@123")
    assert "Password must contain a lowercase letter" in errors


def test_missing_digit():
    policy = PasswordPolicy()
    errors = policy.check("Hello@abc")
    assert "Password must contain a digit" in errors


def test_missing_special_character():
    policy = PasswordPolicy()
    errors = policy.check("Hello123")
    assert "Password must contain a special character" in errors


def test_entropy_empty_password():
    calculator = EntropyCalculator()
    assert calculator.calculate("") == 0.0


def test_entropy_increases_with_length():
    calculator = EntropyCalculator()
    short_password = calculator.calculate("Ab1!")
    long_password = calculator.calculate("Abcdef1234!")
    assert long_password > short_password


def test_password_checker():
    checker = PasswordChecker()
    result = checker.check_password("Hello@123")
    assert result["valid"] is True
    assert result["entropy"] > 0
    assert result["strength"] != ""


def test_weak_password():
    checker = PasswordChecker()
    result = checker.check_password("hello")
    assert result["valid"] is False
    assert result["strength"] == "Very Weak"


def test_common_password():
    checker = PasswordChecker()
    result = checker.check_password("password")
    assert result["is_common"] is True
    assert "Password is a commonly used password" in result["errors"]


def test_non_common_password():
    checker = PasswordChecker()
    result = checker.check_password("Xy7!mQ2@")
    assert result["is_common"] is False


def test_common_password_is_very_weak():
    checker = PasswordChecker()
    result = checker.check_password("password")
    assert result["strength"] == "Very Weak"


def test_repeated_character_pattern():
    checker = PasswordChecker()
    result = checker.check_password("aaaaaa")
    assert result["has_pattern"] is True
    assert "Password contains a common pattern" in result["errors"]


def test_increasing_pattern():
    checker = PasswordChecker()
    result = checker.check_password("abcdef")
    assert result["has_pattern"] is True


def test_decreasing_pattern():
    checker = PasswordChecker()
    result = checker.check_password("fedcba")
    assert result["has_pattern"] is True


def test_normal_password_has_no_pattern():
    checker = PasswordChecker()
    result = checker.check_password("Xy7!mQ2@")
    assert result["has_pattern"] is False


def test_qwerty_keyboard_pattern():
    checker = PasswordChecker()
    result = checker.check_password("qwerty")
    assert result["has_keyboard_pattern"] is True


def test_asdf_keyboard_pattern():
    checker = PasswordChecker()
    result = checker.check_password("asdfgh")
    assert result["has_keyboard_pattern"] is True


def test_zxcv_keyboard_pattern():
    checker = PasswordChecker()
    result = checker.check_password("zxcvbn")
    assert result["has_keyboard_pattern"] is True


def test_normal_password_has_no_keyboard_pattern():
    checker = PasswordChecker()
    result = checker.check_password("Xy7!mQ2@")
    assert result["has_keyboard_pattern"] is False


def test_keyboard_pattern_is_very_weak():
    checker = PasswordChecker()
    result = checker.check_password("qwerty")
    assert result["strength"] == "Very Weak"


def test_generated_password_has_correct_length():
    generator = PasswordGenerator()
    password = generator.generate(length=16)
    assert len(password) == 16


def test_generated_password_contains_required_character_types():
    generator = PasswordGenerator()
    password = generator.generate(
        length=16,
        include_uppercase=True,
        include_lowercase=True,
        include_digits=True,
        include_special=True
    )

    assert any(char.isupper() for char in password)
    assert any(char.islower() for char in password)
    assert any(char.isdigit() for char in password)
    assert any(
        char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        for char in password
    )


def test_generated_password_can_be_checked():
    generator = PasswordGenerator()
    checker = PasswordChecker()

    password = generator.generate(length=16)
    result = checker.check_password(password)

    assert result["entropy"] > 0
    assert result["strength"] != ""


def test_generator_rejects_invalid_length():
    generator = PasswordGenerator()

    try:
        generator.generate(length=0)
        assert False
    except ValueError:
        assert True


def test_generator_requires_character_type():
    generator = PasswordGenerator()

    try:
        generator.generate(
            length=16,
            include_uppercase=False,
            include_lowercase=False,
            include_digits=False,
            include_special=False
        )
        assert False
    except ValueError:
        assert True


def test_custom_minimum_length():
    policy = PasswordPolicy(min_length=12)
    errors = policy.check("Hello@123")

    assert "Password must contain at least 12 characters" in errors


def test_custom_policy_without_uppercase():
    policy = PasswordPolicy(
        min_length=8,
        require_uppercase=False
    )

    assert policy.is_valid("hello@123")


def test_custom_policy_without_digit():
    policy = PasswordPolicy(
        min_length=8,
        require_digit=False
    )

    assert policy.is_valid("Hello@abc")


def test_custom_policy_without_special_character():
    policy = PasswordPolicy(
        min_length=8,
        require_special=False
    )

    assert policy.is_valid("Hello123")


def test_custom_policy_allows_basic_password():
    policy = PasswordPolicy(
        min_length=6,
        require_uppercase=False,
        require_lowercase=True,
        require_digit=False,
        require_special=False
    )

    assert policy.is_valid("hello1")


def test_invalid_minimum_length():
    try:
        PasswordPolicy(min_length=0)
        assert False
    except ValueError:
        assert True