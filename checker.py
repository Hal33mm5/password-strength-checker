import re
import os
import sys

WORDLIST_PATH = "rockyou.txt"


# -----------------------------
# Load common passwords (fast)
# -----------------------------
def load_common_passwords(path):
    if not os.path.exists(path):
        print("[!] Warning: rockyou.txt not found. Skipping dictionary check.")
        return set()

    try:
        with open(path, "r", encoding="latin-1") as f:
            return set(line.strip() for line in f)
    except Exception as e:
        print(f"[!] Error loading wordlist: {e}")
        return set()


COMMON_PASSWORDS = load_common_passwords(WORDLIST_PATH)


# -----------------------------
# Strength Evaluation
# -----------------------------
def evaluate_password(password):
    if password in COMMON_PASSWORDS:
        return {
            "strength": "Very Weak",
            "reason": "Password found in common password list",
            "score": 0
        }

    score = 0
    feedback = []

    length = len(password)

    # Length scoring
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Character checks
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    # Final classification
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }


# -----------------------------
# Display Result
# -----------------------------
def display_result(result):
    print("\n[+] Password Strength:", result["strength"])
    print("[+] Score:", result.get("score", 0))

    if "reason" in result:
        print("[!] Reason:", result["reason"])

    if result.get("feedback"):
        print("\nSuggestions:")
        for item in result["feedback"]:
            print(f"- {item}")


# -----------------------------
# Main
# -----------------------------
def main():
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter password: ")

    result = evaluate_password(password)
    display_result(result)


if __name__ == "__main__":
    main()
