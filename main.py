from password_checker import PasswordChecker
from password_generator import PasswordGenerator


def display_result(result):
    print("\n" + "=" * 45)
    print("       PASSWORD STRENGTH AUDITOR")
    print("=" * 45)

    print(f"Policy Status : {'PASS' if result['valid'] else 'FAIL'}")
    print(f"Entropy       : {result['entropy']:.2f} bits")
    print(f"Strength      : {result['strength']}")

    print(
        f"Common Password: "
        f"{'YES' if result['is_common'] else 'NO'}"
    )

    print(
        f"Keyboard Pattern: "
        f"{'YES' if result['has_keyboard_pattern'] else 'NO'}"
    )

    if result["errors"]:
        print("\nPolicy Issues:")
        for error in result["errors"]:
            print(f"- {error}")
    else:
        print("\nPolicy Issues: None")

    print("=" * 45)


def generate_password():
    generator = PasswordGenerator()

    print("\n" + "=" * 45)
    print("          PASSWORD GENERATOR")
    print("=" * 45)

    try:
        length = int(input("Enter password length: "))

        password = generator.generate(length=length)

        print("\nGenerated Password:")
        print(password)

    except ValueError as error:
        print(f"\nError: {error}")

    print("=" * 45)


def audit_password():
    print("\n" + "=" * 45)
    print("       PASSWORD STRENGTH AUDITOR")
    print("=" * 45)

    password = input("Enter password: ")

    checker = PasswordChecker()
    result = checker.check_password(password)

    display_result(result)


def main():
    while True:
        print("\n")
        print("=" * 45)
        print(" PASSWORD STRENGTH AUDITOR & POLICY CHECKER")
        print("=" * 45)
        print("1. Audit Password")
        print("2. Generate Password")
        print("3. Exit")
        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            audit_password()

        elif choice == "2":
            generate_password()

        elif choice == "3":
            print("\nExiting application...")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()