import re

# Load rockyou once (faster)
def load_common_passwords():
    try:
        with open("rockyou.txt", "r", encoding="latin-1") as f:
            return set(line.strip() for line in f)
    except:
        print("Warning: rockyou.txt not found.")
        return set()

common_passwords = load_common_passwords()


def is_common_password(password):
    return password in common_passwords


def check_password_strength(password):
    if is_common_password(password):
        return "Very Weak (Common Password)"

    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, has_upper, has_lower, has_digit, has_special


def give_feedback(password, has_upper, has_lower, has_digit, has_special):
    print("\nSuggestions to improve your password:")

    if len(password) < 8:
        print("- Use at least 8 characters")
    if not has_upper:
        print("- Add uppercase letters (A-Z)")
    if not has_lower:
        print("- Add lowercase letters (a-z)")
    if not has_digit:
        print("- Add numbers (0-9)")
    if not has_special:
        print("- Add special characters (!@#$ etc.)")


# Main
password = input("Enter password: ")

result = check_password_strength(password)

if isinstance(result, str):
    print("Strength:", result)
else:
    strength, has_upper, has_lower, has_digit, has_special = result
    print("Strength:", strength)

    if strength != "Strong":
        give_feedback(password, has_upper, has_lower, has_digit, has_special)
