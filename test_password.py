from policy import PasswordPolicy
from entropy import EntropyCalculator
from password_checker import PasswordChecker


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