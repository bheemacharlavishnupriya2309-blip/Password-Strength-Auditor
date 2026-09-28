# Password Strength Auditor & Policy Checker

## Project Description

Password Strength Auditor & Policy Checker is a Python-based security application that evaluates password strength using password policy validation, entropy calculation, password strength classification, common password detection, common pattern detection, and keyboard pattern detection.

Version 5 also introduces a secure password generator that can create random passwords using uppercase letters, lowercase letters, digits, and special characters.

The project is developed using Object-Oriented Programming principles and includes automated testing using Pytest.

---

## Objective

The objective of this project is to develop a modular password security auditing and password generation system using Python.

The system is designed to:

- Validate passwords against security policies.
- Calculate estimated password entropy.
- Classify password strength.
- Detect commonly used passwords.
- Detect predictable password patterns.
- Detect repeated characters.
- Detect increasing character sequences.
- Detect decreasing character sequences.
- Detect keyboard patterns.
- Generate secure random passwords.
- Allow users to select password length.
- Support different character types during password generation.
- Identify missing password requirements.
- Provide useful security feedback.
- Demonstrate Object-Oriented Programming.
- Implement automated testing using Pytest.

---

## Features

### Password Auditing

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

### Password Generation

- Secure random password generation
- Custom password length
- Uppercase letter support
- Lowercase letter support
- Digit support
- Special character support
- Input validation
- Generated password auditing

### Development

- Object-Oriented Programming
- Modular Python design
- Automated unit testing using Pytest
- Git version control
- GitHub repository management

---

## Technologies Used

- Python 3
- Object-Oriented Programming
- Pytest
- secrets module
- string module
- Git
- GitHub

---

## Project Structure

Password_Strength_Auditor/
│
├── README.md
├── main.py
├── password_checker.py
├── password_generator.py
├── policy.py
├── entropy.py
├── test_password.py
├── requirements.txt
└── .gitignore

---

## File Description

| File | Purpose |
|---|---|
| main.py | Provides the application menu and connects auditing and password generation |
| password_checker.py | Performs password policy checking, entropy analysis, common password detection, pattern detection, and keyboard pattern detection |
| password_generator.py | Generates secure random passwords |
| policy.py | Checks password policy requirements |
| entropy.py | Calculates estimated password entropy |
| test_password.py | Contains automated test cases |
| requirements.txt | Contains project dependencies |
| README.md | Contains project documentation |
| .gitignore | Prevents unnecessary files from being uploaded to GitHub |

---

## How the System Works

The application provides a menu-driven interface.

The main menu contains:

1. Audit Password
2. Generate Password
3. Exit

The application follows this workflow:

User
  ↓
Main Menu
  ↓
Choose Operation
  ↓
Audit Password OR Generate Password
  ↓
Display Result

---

## Password Auditing Workflow

When the user chooses Audit Password:

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

## Password Generation Workflow

When the user chooses Generate Password:

User selects Generate Password
        ↓
Enter Password Length
        ↓
Generate Secure Random Characters
        ↓
Ensure Required Character Types
        ↓
Shuffle Characters
        ↓
Display Generated Password

The generator uses Python's secrets module for security-oriented random generation.

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

The application checks for common keyboard sequences such as:

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

## Password Generator

Version 5 introduces the Password Generator.

The generator is implemented using the Python secrets module.

The generator can include:

- Uppercase letters
- Lowercase letters
- Digits
- Special characters

The user can specify the desired password length.

Example:

Enter password length:

16

The generator then creates a random password such as:

G7@kP2!xQ9#mL4$z

The actual generated password will be different each time.

---

## Secure Random Generation

The project uses Python's secrets module rather than the ordinary random module for password generation.

The secrets module is designed for generating random values suitable for security-sensitive applications.

The generator:

1. Creates the selected character sets.
2. Ensures at least one character from every selected character category.
3. Fills the remaining password length with random characters.
4. Shuffles the generated characters.
5. Returns the final password.

---

## Password Generator Validation

The generator validates the user's configuration.

It raises an error when:

- No character type is selected.
- The requested password length is too short for the selected character types.

For example, if four character categories are selected, the password must have enough length to include at least one character from each selected category.

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

The application will display:

=============================================
 PASSWORD STRENGTH AUDITOR & POLICY CHECKER
=============================================
1. Audit Password
2. Generate Password
3. Exit
=============================================
Enter your choice:

---

## Audit Password

Select:

1

The application asks:

Enter password:

Enter a password such as:

Hello@123

The application displays the password audit result.

---

## Sample Audit Output

=============================================
       PASSWORD STRENGTH AUDITOR
=============================================
Policy Status : PASS
Entropy       : 58.99 bits
Strength      : Moderate
Common Password: NO
Keyboard Pattern: NO

Policy Issues: None
=============================================

---

## Generate Password

Select:

2

The application asks:

Enter password length:

Enter:

16

The application generates a secure random password.

Example:

Generated Password:

G7@kP2!xQ9#mL4$z

The generated password will be different each time.

---

## Exit Application

Select:

3

The application displays:

Exiting application...

and terminates.

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
Keyboard Pattern: NO

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
Keyboard Pattern: NO

Policy Issues:
- Password must contain an uppercase letter
- Password must contain a digit
- Password must contain a special character
- Password is a commonly used password
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
Keyboard Pattern: YES

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

The current test suite contains 27 test cases.

Expected result:

27 passed

---

## Test Categories

### Password Policy Tests

- Valid Password
- Short Password
- Missing Uppercase
- Missing Lowercase
- Missing Digit
- Missing Special Character

### Entropy Tests

- Empty Password
- Entropy Comparison

### Password Checker Tests

- Valid Password
- Weak Password
- Common Password
- Non-Common Password
- Common Password Strength

### Common Pattern Tests

- Repeated Character Pattern
- Increasing Character Pattern
- Decreasing Character Pattern
- Normal Password Without Pattern

### Keyboard Pattern Tests

- QWERTY Pattern
- ASDFGH Pattern
- ZXCVBN Pattern
- Normal Password Without Keyboard Pattern
- Keyboard Pattern Strength

### Password Generator Tests

- Generated Password Length
- Required Character Types
- Generated Password Can Be Audited
- Invalid Generator Length
- No Character Type Selected

---

## Algorithm

### Password Auditing Algorithm

Step 1: Accept Password

The user enters a password.

Step 2: Check Common Password

The password is compared against the application's common-password set.

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

The estimated entropy is calculated.

Step 8: Determine Strength

The entropy value is compared with the predefined strength thresholds.

Step 9: Generate Result

The application displays the final password audit.

---

## Password Generation Algorithm

Step 1: Select Character Types

The generator determines which character types are enabled.

Step 2: Validate Settings

The generator checks that at least one character type is selected.

Step 3: Validate Length

The generator checks that the requested length is sufficient for the selected character types.

Step 4: Select Required Characters

At least one character is selected from each enabled character set.

Step 5: Fill Remaining Characters

Additional characters are selected from the combined character pool.

Step 6: Shuffle

The characters are securely shuffled.

Step 7: Return Password

The final generated password is returned to the user.

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

### PasswordGenerator

The PasswordGenerator class is responsible for:

- Generating random passwords
- Handling character-type selections
- Validating generator settings
- Creating passwords using the secrets module

This modular design improves:

- Code organization
- Maintainability
- Reusability
- Testing

---

## Time Complexity

Let n represent the password length.

### Policy Checking

O(n)

### Entropy Calculation

O(n)

### Common Password Detection

Average-case:

O(1)

### Common Pattern Detection

O(n)

### Keyboard Pattern Detection

For the fixed pattern list used in this project:

O(n)

### Password Generation

The generator creates a password of length n.

O(n)

### Overall Auditing Complexity

O(n)

### Overall Generation Complexity

O(n)

### Space Complexity

For the fixed project configuration, the additional working space is approximately:

O(n)

because the generated password is stored in memory.

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

### Password Generator

- Correct Password Length
- Required Character Types
- Generated Password Auditing
- Invalid Length Handling
- Character Type Validation

Current test result:

27 tests passed

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

### Version 5

Added:

- Secure password generation
- Python secrets module
- Custom password length
- Uppercase character support
- Lowercase character support
- Digit support
- Special character support
- Generator validation
- Generated password auditing
- Menu-driven application
- Additional automated tests

Current test count:

27 tests

---

## Future Enhancements

Possible future improvements include:

- Larger common-password database
- Dictionary-based password analysis
- More advanced password pattern detection
- Detection of numeric sequences
- Detection of repeated blocks
- Detection of dates and years
- Configurable password policies
- Password history analysis
- Graphical User Interface
- Web-based interface
- Detailed security reports
- Password audit report export
- Real-time password strength feedback
- Privacy-preserving password breach checking
- More customizable password generator options

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
- Secure random generation
- Python secrets module
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
- Secure password generation
- Python OOP
- Software testing

It can also serve as a foundation for developing more advanced password security applications.

---

## Author

Developed as a Python security and software engineering project.

---

## License

This project is intended for educational and learning purposes.