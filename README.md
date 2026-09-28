# Password Strength Auditor & Policy Checker

## Project Description

Password Strength Auditor & Policy Checker is a Python-based security application that evaluates the strength of a password using password policy validation, entropy calculation, password strength classification, and common password detection.

The application checks password requirements such as minimum length, uppercase letters, lowercase letters, digits, and special characters. It also estimates password entropy and detects passwords that are commonly used.

The project is developed using Object-Oriented Programming principles and includes automated testing using Pytest.

---

## Objective

The objective of this project is to develop a modular password security auditing system using Python.

The system is designed to:

- Validate passwords against security policies.
- Calculate estimated password entropy.
- Classify password strength.
- Detect commonly used passwords.
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
| password_checker.py | Combines policy checking, entropy analysis, and common password detection |
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
3. Validates the password against the configured security policy.
4. Identifies the character types present in the password.
5. Calculates estimated password entropy.
6. Classifies the password strength.
7. Displays the final password audit result.

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

A password detected as a common password is classified as Very Weak by the application.

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

## Testing

The project uses Pytest for automated testing.

Run all tests using:

pytest

The current test suite contains 13 test cases.

Expected result:

13 passed

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

---

## Algorithm

Step 1: Accept Password

The user enters a password through the application.

Step 2: Check Common Password

The password is compared against the application's common-password list.

Step 3: Validate Password Policy

The system checks:

- Minimum password length
- Uppercase letter
- Lowercase letter
- Digit
- Special character

Step 4: Determine Character Pool

The system identifies the character categories present in the password.

Step 5: Calculate Entropy

The estimated entropy is calculated using:

Entropy = Password Length × log₂(Character Pool)

Step 6: Determine Strength

The entropy value is compared with the predefined strength thresholds.

If the password is detected as a common password, its strength is classified as Very Weak.

Step 7: Generate Result

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

### Overall Time Complexity

O(n)

### Space Complexity

For the fixed project configuration:

O(1)

---

## Test Coverage

The automated tests cover the major components of the application.

Password Policy

- Valid Password
- Short Password
- Missing Uppercase
- Missing Lowercase
- Missing Digit
- Missing Special Character

Entropy Calculator

- Empty Password
- Entropy Comparison

Password Checker

- Valid Password
- Weak Password
- Common Password
- Non-Common Password
- Common Password Strength

Current test result:

13 tests passed

---

## Future Enhancements

Possible future improvements include:

- Larger common-password database
- Dictionary-based password analysis
- Detection of repeated characters
- Detection of common password patterns
- Detection of sequential characters
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
- Python OOP
- Software testing

It can also serve as a foundation for developing more advanced password auditing tools.

---

## Author

Developed as a Python security and software engineering project.

---

## License

This project is intended for educational and learning purposes.