import re


def password_strength_checker(password):
    # Define initial strength level
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase letters for more strength.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include lowercase letters for more complexity.")

    # Check for digits
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add numbers to make the password stronger.")

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~`-]", password):
        strength += 1
    else:
        feedback.append("Use special characters (e.g., !@#$%) for added security.")

    # Provide feedback based on strength level
    if strength == 5:
        return "Password is very strong!"
    elif strength == 4:
        return "Password is strong, but could be improved.", feedback
    elif strength == 3:
        return "Password is moderate; it needs more complexity.", feedback
    else:
        return "Password is weak. Please improve it.", feedback


# Example usage
password = input("Enter a password to check its strength: ")
strength_result, feedback = password_strength_checker(password)

print("\nStrength Assessment:")
print(strength_result)
if feedback:
    print("Suggestions:")
    for suggestion in feedback:
        print("- " + suggestion)
