import re

def check_password_strength(password):
    # Initialize variables for criteria
    length = len(password)
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'[0-9]', password) is not None
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Determine strength based on criteria
    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Provide feedback based on score
    if score == 5:
        return "Strong password! Your password is very secure."
    elif score == 4:
        return "Good password! Consider adding more characters or special symbols to increase security."
    elif score == 3:
        return "Moderate password. You should add uppercase letters, numbers, or special characters to make it stronger."
    elif score == 2:
        return "Weak password. It's recommended to use a mix of uppercase letters, lowercase letters, numbers, and special characters."
    else:
        return "Very weak password. You should create a more complex password with at least 8 characters, including uppercase letters, lowercase letters, numbers, and special symbols."

def main():
    print("Password Strength Checker")
    password = input("Enter a password to assess its strength: ")
    feedback = check_password_strength(password)
    print(feedback)

if __name__ == "__main__":
    main()
