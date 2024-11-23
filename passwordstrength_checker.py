import re

def check_password_strength(password):
    """
    Check the strength of a password and return a score with suggestions.
    """
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digits": bool(re.search(r"[0-9]", password)),
        "special_characters": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
        "no_common_words": not bool(re.search(r"(password|1234|qwerty|letmein|admin|welcome)", password.lower())),
    }
    
    # Calculate the score based on criteria
    score = sum(strength_criteria.values())
    
    # Suggestions for improvement
    suggestions = []
    if not strength_criteria["length"]:
        suggestions.append("Make the password at least 8 characters long.")
    if not strength_criteria["uppercase"]:
        suggestions.append("Add uppercase letters (A-Z).")
    if not strength_criteria["lowercase"]:
        suggestions.append("Include lowercase letters (a-z).")
    if not strength_criteria["digits"]:
        suggestions.append("Add numbers (0-9).")
    if not strength_criteria["special_characters"]:
        suggestions.append("Use special characters (!@#$%^&*(), etc.).")
    if not strength_criteria["no_common_words"]:
        suggestions.append("Avoid common words or patterns (e.g., 'password', '1234').")
    
    # Return the score and suggestions
    return score, suggestions


def main():
    print("Welcome to Shiv's Projects: Password Strength Checker!")
    password = input("Enter your password: ")
    score, suggestions = check_password_strength(password)
    
    print(f"\nPassword Strength: {score}/6")
    if score == 6:
        print("Your password is strong! 🎉")
    else:
        print("Your password could be improved. Consider the following suggestions:")
        for suggestion in suggestions:
            print(f" - {suggestion}")

if __name__ == "__main__":
    main()
