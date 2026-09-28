from password_checker import PasswordChecker


def display_result(result):
    print("\n" + "=" * 45)
    print("       PASSWORD STRENGTH AUDITOR")
    print("=" * 45)

    print(f"Policy Status : {'PASS' if result['valid'] else 'FAIL'}")
    print(f"Entropy       : {result['entropy']:.2f} bits")
    print(f"Strength      : {result['strength']}")

    if result["errors"]:
        print("\nPolicy Issues:")
        for error in result["errors"]:
            print(f"- {error}")
    else:
        print("\nPolicy Issues: None")

    print("=" * 45)


def main():
    print("Password Strength Auditor & Policy Checker")
    print("-------------------------------------------")

    password = input("Enter password: ")

    checker = PasswordChecker()
    result = checker.check_password(password)

    display_result(result)


if __name__ == "__main__":
    main()