# Password Strength Auditor & Policy Checker

## Project Description

Password Strength Auditor & Policy Checker is a Python-based security application that evaluates password strength using password policy validation, entropy calculation, password strength classification, common password detection, common pattern detection, and keyboard pattern detection.

The application checks password requirements such as minimum length, uppercase letters, lowercase letters, digits, and special characters. It also estimates password entropy and detects passwords that are commonly used or contain predictable patterns.

The project is developed using Object-Oriented Programming principles and includes automated testing using Pytest.

---

## Objective

The objective of this project is to develop a modular password security auditing system using Python.

The system is designed to:

- Validate passwords against security policies.
- Calculate estimated password entropy.
- Classify password strength.
- Detect commonly used passwords.
- Detect simple predictable password patterns.
- Detect repeated characters.
- Detect increasing character sequences.
- Detect decreasing character sequences.
- Detect keyboard patterns.
- Identify missing password requirements.
- Provide useful feedback to users.
- Demonstrate Object-Oriented Programming.
- Implement automated testing using Pytest.

---

## Features

- Minimum password length validation
- Uppercase letter validation
- Lowercase letter validation
- Digit validation
- Special character validation
- Password entropy calculation
- Password strength classification
- Common password detection
- Repeated character pattern detection
- Increasing character sequence detection
- Decreasing character sequence detection
- Keyboard pattern detection
- Detailed password policy error messages
- Object-Oriented Programming
- Automated unit testing using Pytest

---

## Technologies Used

- Python 3
- Object-Oriented Programming
- Pytest
- Git
- GitHub

---

## Project Structure

Password_Strength_Auditor/
│
├── README.md
├── main.py
├── password_checker.py
├── policy.py
├── entropy.py
├── test_password.py
├── requirements.txt
└── .gitignore

---

## File Description

| File | Purpose |
|---|---|
| main.py | Runs the main application |
| password_checker.py | Combines policy checking, entropy analysis, common password detection, pattern detection, and keyboard pattern detection |
| policy.py | Checks password policy requirements |
| entropy.py | Calculates estimated password entropy |
| test_password.py | Contains automated test cases |
| requirements.txt | Contains project dependencies |
| README.md | Contains project documentation |
| .gitignore | Prevents unnecessary files from being uploaded to GitHub |

---

## How the System Works

The application follows this workflow:

User enters password
        ↓
Common Password Check
        ↓
Common Pattern Check
        ↓
Keyboard Pattern Check
        ↓
Password Policy Check
        ↓
Entropy Calculation
        ↓
Strength Classification
        ↓
Final Password Audit

The system performs the following operations:

1. Accepts a password from the user.
2. Checks whether the password is commonly used.
3. Checks whether the password contains a predictable pattern.
4. Checks whether the password contains a keyboard pattern.
5. Validates the password against the configured security policy.
6. Identifies the character types present in the password.
7. Calculates estimated password entropy.
8. Classifies the password strength.
9. Displays the final password audit result.

---

## Password Policy

The default password policy checks the following requirements:

| Requirement | Description |
|---|---|
| Minimum Length | At least 8 characters |
| Uppercase | At least one uppercase letter |
| Lowercase | At least one lowercase letter |
| Digit | At least one number |
| Special Character | At least one special character |

A password must satisfy all required rules to pass the default policy.

---

## Common Password Detection

The application checks whether the entered password matches a list of commonly used passwords.

If a password is detected as common:

- The user receives a warning.
- A common-password error is added to the audit result.
- The password is classified as Very Weak.

Example commonly detected passwords include:

- password
- password123
- 123456
- qwerty
- admin
- welcome
- letmein

The list is intended for educational demonstration and is not a complete database of commonly used passwords.

---

## Common Pattern Detection

The application detects simple predictable character patterns.

### Repeated Characters

The system detects passwords where the same character is repeated throughout the password.

Example:

aaaaaa

### Increasing Character Sequence

The system detects characters that continuously increase by one character code.

Example:

abcdef

### Decreasing Character Sequence

The system detects characters that continuously decrease by one character code.

Example:

fedcba

If a common pattern is detected, the system adds:

Password contains a common pattern

The password is classified as Very Weak.

---

## Keyboard Pattern Detection

Version 4 introduces keyboard pattern detection.

The system checks for common keyboard sequences such as:

- qwerty
- asdfgh
- zxcvbn
- qwertyui
- asdfghjk
- zxcvbnm

Examples:

qwerty
asdfgh
zxcvbn

If a keyboard pattern is detected, the system adds:

Password contains a keyboard pattern

The password is classified as Very Weak.

The keyboard pattern check is case-insensitive.

For example:

QWERTY

and

qwerty

are treated as the same keyboard pattern.

---

## Pattern Detection Logic

The pattern detector performs the following checks:

1. If the password is shorter than four characters, no common pattern is reported.
2. If all characters are identical, a repeated-character pattern is detected.
3. The system checks whether every character increases sequentially.
4. The system checks whether every character decreases sequentially.
5. If either sequential condition is satisfied, a common pattern is detected.
6. The system checks for predefined keyboard patterns.
7. If a keyboard sequence is found, a keyboard pattern is detected.
8. Otherwise, the password is treated as not containing a detected pattern.

---

## Entropy Calculation

Password entropy is estimated using password length and the size of the character pool.

The calculation used in this project is:

Entropy = Password Length × log₂(Character Pool)

The character pool is determined from the types of characters present in the password:

- Lowercase letters
- Uppercase letters
- Numbers
- Special characters

A higher estimated entropy represents a larger theoretical search space.

---

## Password Strength Classification

The application classifies passwords based on estimated entropy.

| Entropy | Strength |
|---:|---|
| Less than 28 bits | Very Weak |
| 28–35 bits | Weak |
| 36–59 bits | Moderate |
| 60–79 bits | Strong |
| 80+ bits | Very Strong |

A password detected as a common password, common pattern, or keyboard pattern is classified as Very Weak by the application.

These thresholds are used for this project's classification and are not a guarantee of real-world password security.

---

## Installation

### 1. Clone the Repository

git clone <YOUR_GITHUB_REPOSITORY_URL>

### 2. Open the Project Directory

cd Password-Strength-Auditor

### 3. Create a Virtual Environment

python -m venv venv

### 4. Activate the Virtual Environment

For Windows:

venv\Scripts\activate

### 5. Install Dependencies

pip install -r requirements.txt

---

## Running the Application

Run the following command:

python main.py

The application will ask the user to enter a password.

Example:

Password Strength Auditor & Policy Checker
-------------------------------------------
Enter password:

Enter a password to receive the audit result.

---

## Sample Input

Hello@123

## Sample Output

=============================================
       PASSWORD STRENGTH AUDITOR
=============================================
Policy Status : PASS
Entropy       : 58.99 bits
Strength      : Moderate
Common Password: NO

Policy Issues: None
=============================================

---

## Example of a Weak Password

Input:

hello

Output:

=============================================
       PASSWORD STRENGTH AUDITOR
=============================================
Policy Status : FAIL
Entropy       : 23.50 bits
Strength      : Very Weak
Common Password: NO

Policy Issues:
- Password must contain at least 8 characters
- Password must contain an uppercase letter
- Password must contain a digit
- Password must contain a special character
=============================================

---

## Example of a Common Password

Input:

password

Output:

=============================================
       PASSWORD STRENGTH AUDITOR
=============================================
Policy Status : FAIL
Entropy       : ...
Strength      : Very Weak
Common Password: YES

Policy Issues:
- Password must contain an uppercase letter
- Password must contain a digit
- Password must contain a special character
- Password is a commonly used password
=============================================

---

## Example of a Common Pattern

Input:

abcdef

Output:

=============================================
       PASSWORD STRENGTH AUDITOR
=============================================
Policy Status : FAIL
Entropy       : ...
Strength      : Very Weak
Common Password: NO

Policy Issues:
- Password must contain an uppercase letter
- Password must contain a digit
- Password must contain a special character
- Password contains a common pattern
=============================================

---

## Example of a Keyboard Pattern

Input:

qwerty

Output:

=============================================
       PASSWORD STRENGTH AUDITOR
=============================================
Policy Status : FAIL
Entropy       : ...
Strength      : Very Weak
Common Password: YES

Policy Issues:
- Password must contain an uppercase letter
- Password must contain a digit
- Password must contain a special character
- Password is a commonly used password
=============================================

Note: qwerty is already included in the common-password list, so the common-password detection takes priority in the displayed error list.

---

## Testing

The project uses Pytest for automated testing.

Run all tests using:

pytest

The current test suite contains 22 test cases.

Expected result:

22 passed

The test suite checks:

- Valid passwords
- Short passwords
- Missing uppercase letters
- Missing lowercase letters
- Missing digits
- Missing special characters
- Empty password entropy
- Entropy comparison
- Password checker functionality
- Weak password detection
- Common password detection
- Non-common password detection
- Common password strength classification
- Repeated character pattern detection
- Increasing pattern detection
- Decreasing pattern detection
- Normal password pattern detection
- QWERTY keyboard pattern detection
- ASDFGH keyboard pattern detection
- ZXCVBN keyboard pattern detection
- Normal password without keyboard pattern
- Keyboard pattern strength classification

---

## Algorithm

Step 1: Accept Password

The user enters a password through the application.

Step 2: Check Common Password

The password is compared against the application's common-password list.

Step 3: Check Common Pattern

The system checks for:

- Repeated characters
- Increasing character sequences
- Decreasing character sequences

Step 4: Check Keyboard Pattern

The system checks whether the password contains a predefined keyboard sequence.

Step 5: Validate Password Policy

The system checks:

- Minimum password length
- Uppercase letter
- Lowercase letter
- Digit
- Special character

Step 6: Determine Character Pool

The system identifies the character categories present in the password.

Step 7: Calculate Entropy

The estimated entropy is calculated using:

Entropy = Password Length × log₂(Character Pool)

Step 8: Determine Strength

The entropy value is compared with the predefined strength thresholds.

If the password is detected as a common password, contains a common pattern, or contains a keyboard pattern, its strength is classified as Very Weak.

Step 9: Generate Result

The application displays:

- Policy status
- Entropy
- Password strength
- Common password status
- Policy issues

---

## Object-Oriented Design

The project uses Object-Oriented Programming to separate different responsibilities.

### PasswordPolicy

The PasswordPolicy class is responsible for validating password requirements.

It checks:

- Password length
- Uppercase letters
- Lowercase letters
- Digits
- Special characters

### EntropyCalculator

The EntropyCalculator class calculates the estimated entropy of a password.

### PasswordChecker

The PasswordChecker class combines:

- Password policy validation
- Entropy calculation
- Common password detection
- Common pattern detection
- Keyboard pattern detection
- Password strength classification

This modular design improves:

- Code organization
- Maintainability
- Reusability
- Testing

---

## Time Complexity

Let n represent the length of the password.

### Policy Checking

The password is scanned to check the required character categories.

O(n)

### Entropy Calculation

The password is scanned to determine its character categories.

O(n)

### Common Password Detection

The password is checked against a set of common passwords.

Average-case lookup:

O(1)

### Common Pattern Detection

The password is scanned to identify repeated or sequential characters.

O(n)

### Keyboard Pattern Detection

The password is checked against a fixed set of keyboard patterns.

For the fixed pattern list used in this project, this is effectively O(n).

### Overall Time Complexity

O(n)

### Space Complexity

For the fixed project configuration:

O(1)

---

## Test Coverage

The automated tests cover the major components of the application.

### Password Policy

- Valid Password
- Short Password
- Missing Uppercase
- Missing Lowercase
- Missing Digit
- Missing Special Character

### Entropy Calculator

- Empty Password
- Entropy Comparison

### Password Checker

- Valid Password
- Weak Password
- Common Password
- Non-Common Password
- Common Password Strength

### Common Pattern Detection

- Repeated Character Pattern
- Increasing Character Pattern
- Decreasing Character Pattern
- Normal Password Without Pattern

### Keyboard Pattern Detection

- QWERTY Pattern
- ASDFGH Pattern
- ZXCVBN Pattern
- Normal Password Without Keyboard Pattern
- Keyboard Pattern Strength

Current test result:

22 tests passed

---

## Version History

### Version 1

Initial implementation containing:

- Password policy validation
- Entropy calculation
- Password strength classification
- Automated testing

### Version 2

Added:

- Common password detection
- Common password warnings
- Common password strength override
- Additional automated tests

### Version 3

Added:

- Common pattern detection
- Repeated character detection
- Increasing sequence detection
- Decreasing sequence detection
- Additional automated tests

### Version 4

Added:

- Keyboard pattern detection
- QWERTY pattern detection
- ASDFGH pattern detection
- ZXCVBN pattern detection
- Keyboard pattern strength classification
- Additional automated tests

Current test count:

22 tests

---

## Future Enhancements

Possible future improvements include:

- Larger common-password database
- Dictionary-based password analysis
- More advanced password pattern detection
- Detection of numeric sequences
- Detection of repeated blocks
- Detection of dates and years
- Secure password generation
- Graphical User Interface
- Web-based interface
- Configurable password policies
- Detailed security reports
- Privacy-preserving password breach checking
- Password history analysis
- Real-time password strength feedback
- Exporting password audit reports

---

## Learning Outcomes

This project demonstrates the following concepts:

- Python programming
- Object-Oriented Programming
- Classes and objects
- Modular programming
- Password policy validation
- Password entropy
- Password strength classification
- Common password detection
- Pattern detection
- Keyboard pattern detection
- Unit testing
- Pytest
- Algorithm design
- Time complexity
- Space complexity
- Git
- GitHub
- Software project organization

---

## Project Applications

This project can be used as an educational example for understanding:

- Password security
- Secure authentication concepts
- Password policy validation
- Password entropy
- Common password detection
- Password pattern analysis
- Keyboard pattern analysis
- Python OOP
- Software testing

It can also serve as a foundation for developing more advanced password auditing tools.

---

## Author

Developed as a Python security and software engineering project.

---

## License

This project is intended for educational and learning purposes.