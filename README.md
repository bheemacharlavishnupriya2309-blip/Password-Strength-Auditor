# Password Strength Auditor & Policy Checker

## 📌 Project Description

Password Strength Auditor & Policy Checker is a Python-based security application that evaluates the strength of a password using configurable password policies and entropy calculation.

The application checks password requirements such as minimum length, uppercase letters, lowercase letters, digits, and special characters. It also calculates estimated password entropy and classifies the password strength.

---

## 🎯 Objective

The objective of this project is to develop a modular password security auditing system using Python and Object-Oriented Programming.

The system is designed to:

- Validate passwords against security policies.
- Calculate estimated password entropy.
- Classify password strength.
- Identify missing password requirements.
- Provide useful feedback to users.
- Demonstrate Object-Oriented Programming concepts.
- Implement automated testing using Pytest.

---

## 🚀 Features

- Minimum password length validation
- Uppercase letter validation
- Lowercase letter validation
- Digit validation
- Special character validation
- Password entropy calculation
- Password strength classification
- Detailed policy error messages
- Object-Oriented Programming
- Automated unit testing using Pytest

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming
- Pytest
- Git
- GitHub

---

## 📂 Project Structure

```text
Password_Strength_Auditor/
│
├── README.md
├── main.py
├── password_checker.py
├── policy.py
├── entropy.py
├── test_password.py
└── requirements.txt
```

---

## 📄 File Description

| File | Purpose |
|---|---|
| `main.py` | Runs the main application |
| `password_checker.py` | Combines policy checking and entropy analysis |
| `policy.py` | Checks password policy requirements |
| `entropy.py` | Calculates estimated password entropy |
| `test_password.py` | Contains automated test cases |
| `requirements.txt` | Contains project dependencies |
| `README.md` | Contains project documentation |

---

## 🔍 How the System Works

The application follows this workflow:

```text
User enters password
        ↓
Password Policy Check
        ↓
Entropy Calculation
        ↓
Strength Classification
        ↓
Final Password Audit
```

The system performs the following operations:

1. Accepts a password from the user.
2. Checks the password against the configured security policy.
3. Identifies the character types present in the password.
4. Calculates the estimated password entropy.
5. Classifies the password strength.
6. Displays the final password audit result.

---

## 🔐 Password Policy

The default password policy checks the following requirements:

| Requirement | Description |
|---|---|
| Minimum Length | At least 8 characters |
| Uppercase | At least one uppercase letter |
| Lowercase | At least one lowercase letter |
| Digit | At least one number |
| Special Character | At least one special character |

A password must satisfy all the required rules to pass the default policy.

---

## 📊 Entropy Calculation

Password entropy is estimated using the password length and the size of the character pool.

The calculation used in this project is:

```text
Entropy = Password Length × log₂(Character Pool)
```

The character pool is determined from the types of characters present in the password:

- Lowercase letters
- Uppercase letters
- Numbers
- Special characters

A higher estimated entropy represents a larger theoretical search space.

---

## 💪 Password Strength Classification

The application classifies passwords based on estimated entropy.

| Entropy | Strength |
|---:|---|
| Less than 28 bits | Very Weak |
| 28–35 bits | Weak |
| 36–59 bits | Moderate |
| 60–79 bits | Strong |
| 80+ bits | Very Strong |

These thresholds are used for this project's classification and are not a guarantee of real-world password security.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Open the Project Directory

```bash
cd Password_Strength_Auditor
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the following command:

```bash
python main.py
```

The application will ask you to enter a password:

```text
Password Strength Auditor & Policy Checker
-------------------------------------------
Enter password:
```

Enter a password to receive the audit result.

---

## 💻 Sample Input

```text
Hello@123
```

## 📤 Sample Output

```text
=============================================
       PASSWORD STRENGTH AUDITOR
=============================================
Policy Status : PASS
Entropy       : 58.99 bits
Strength      : Moderate

Policy Issues: None
=============================================
```

---

## ❌ Example of a Weak Password

### Input

```text
hello
```

### Output

```text
=============================================
       PASSWORD STRENGTH AUDITOR
=============================================
Policy Status : FAIL
Entropy       : 23.50 bits
Strength      : Very Weak

Policy Issues:
- Password must contain at least 8 characters
- Password must contain an uppercase letter
- Password must contain a digit
- Password must contain a special character
=============================================
```

---

## 🧪 Testing

The project uses Pytest for automated testing.

Run all tests using:

```bash
pytest
```

The current test suite contains 10 test cases.

Expected result:

```text
10 passed
```

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

---

## 🧠 Algorithm

### Step 1: Accept Password

The user enters a password through the application.

### Step 2: Validate Password Policy

The system checks:

- Minimum password length
- Uppercase letter
- Lowercase letter
- Digit
- Special character

### Step 3: Determine Character Pool

The system identifies which character categories are present in the password.

### Step 4: Calculate Entropy

The system calculates the estimated entropy using:

```text
Entropy = Password Length × log₂(Character Pool)
```

### Step 5: Determine Strength

The entropy value is compared with the predefined strength thresholds.

### Step 6: Generate Result

The application displays:

- Policy status
- Entropy
- Password strength
- Policy issues

---

## 🧱 Object-Oriented Design

The project uses Object-Oriented Programming to separate different responsibilities.

### PasswordPolicy

The `PasswordPolicy` class is responsible for validating password requirements.

It checks:

- Password length
- Uppercase letters
- Lowercase letters
- Digits
- Special characters

### EntropyCalculator

The `EntropyCalculator` class calculates the estimated entropy of a password.

### PasswordChecker

The `PasswordChecker` class combines the password policy and entropy calculator to produce the final password audit result.

This modular design improves:

- Code organization
- Maintainability
- Reusability
- Testing

---

## ⏱️ Time Complexity

Let `n` represent the length of the password.

### Policy Checking

The password is scanned to check the required character categories.

```text
O(n)
```

### Entropy Calculation

The password is scanned to determine its character categories.

```text
O(n)
```

### Overall Time Complexity

```text
O(n)
```

### Space Complexity

The application uses a fixed number of variables and policy messages.

```text
O(1)
```

---

## 🧪 Test Coverage

The automated tests verify the major components of the application.

```text
Password Policy
       │
       ├── Valid Password
       ├── Short Password
       ├── Missing Uppercase
       ├── Missing Lowercase
       ├── Missing Digit
       └── Missing Special Character

Entropy Calculator
       │
       ├── Empty Password
       └── Entropy Comparison

Password Checker
       │
       ├── Valid Password
       └── Weak Password
```

Current test result:

```text
10 tests passed
```

---

## 🔮 Future Enhancements

Possible future improvements include:

- Common password detection
- Dictionary-based password analysis
- Detection of repeated characters
- Detection of common password patterns
- Secure password generation
- Graphical User Interface
- Web-based interface
- Configurable password policies
- Detailed security reports
- Privacy-preserving password breach checking
- Password history analysis
- Real-time password strength feedback

---

## 📚 Learning Outcomes

This project demonstrates the following concepts:

- Python programming
- Object-Oriented Programming
- Classes and objects
- Modular programming
- Password policy validation
- Entropy calculation
- Unit testing
- Pytest
- Algorithm design
- Time complexity
- Space complexity
- Git
- GitHub
- Software project organization

---

## 🎓 Project Applications

This project can be used as an educational example for understanding:

- Password security
- Secure authentication concepts
- Security policy validation
- Password entropy
- Python OOP
- Software testing

It can also serve as a foundation for developing more advanced password auditing tools.

---

## 👨‍💻 Author

Developed as a Python security and software engineering project.

---

## 📄 License

This project is intended for educational and learning purposes.