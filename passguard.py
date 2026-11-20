
import math
import secrets
import string

common_passwords = {
    "123456", "123456789", "12345678", "1234567", "1234567890", "password",
    "password123", "qwerty", "qwerty123", "abc123", "111111", "123123",
    "admin", "admin123", "welcome", "iloveyou", "000000", "654321",
    "pass123", "india123", "monkey", "dragon", "sunshine", "football",
    "letmein", "login", "hello123", "test123", "password1", "00000000",
    "1q2w3e4r", "qwertyuiop", "asdfghjkl", "lovely", "starwars", "whatever",
    "trustno1", "zaq12wsx", "123qwe", "1234", "12345", "123456789a",
    "iloveyou123", "secret", "secret123", "changeme", "master", "computer",
    "shadow", "superman", "michael", "jessica", "ashley", "charlie",
    "donald", "freedom", "ninja"
}

while True:

    print("\n===== PASSGUARD =====")
    print("1. Analyze Password")
    print("2. Generate Password")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # VERSION 1 TO 5: PASSWORD ANALYSIS

    if choice == "1":

        password = input("Enter Your Password: ")

        length = len(password)

        if length == 0:
            print("Password cannot be empty")
            continue

        if length < 8:
            print("Too short Password")
        else:
            print("Length is OK")

        upper = 0
        lower = 0
        digit = 0
        special = 0

        for word in password:

            if word.isupper():
                upper += 1

            if word.islower():
                lower += 1

            if word.isdigit():
                digit += 1

            if not word.isalnum():
                special += 1

        print("Uppercase:", upper)
        print("Lowercase:", lower)
        print("Digits:", digit)
        print("Special:", special)

        # COMMON PASSWORD CHECK

        if password.lower() in common_passwords:
            print("WARNING: This is a very common password!")
        else:
            print("Not found in common password list")

        # SCORE

        score = 0

        if length >= 8:
            score += 20

        if length >= 12:
            score += 10

        if length >= 16:
            score += 10

        if upper > 0:
            score += 15

        if lower > 0:
            score += 15

        if digit > 0:
            score += 15

        if special > 0:
            score += 15

        if password.lower() in common_passwords:
            score = 10

        print("Score:", score, "/ 100")

        if score < 40:
            print("Strength: Weak")

        elif score < 70:
            print("Strength: Medium")

        elif score < 90:
            print("Strength: Strong")

        else:
            print("Strength: Very Strong")

        # VERSION 5: ENTROPY

        pool = 0

        if lower > 0:
            pool += 26

        if upper > 0:
            pool += 26

        if digit > 0:
            pool += 10

        if special > 0:
            pool += 32

        entropy = length * math.log2(pool)

        print("Entropy:", round(entropy, 1), "bits")

                # CRACK TIME

        if password.lower() in common_passwords:
            crack_time = "Instantly (Common Password)"

        elif entropy >= 100:
            crack_time = "More than a trillion years"

        else:
            seconds = (2 ** entropy) / 10000000000

            if seconds < 1:
                crack_time = "Less than a second"

            elif seconds < 60:
                crack_time = str(round(seconds)) + " seconds"

            elif seconds < 3600:
                crack_time = str(round(seconds / 60)) + " minutes"

            elif seconds < 86400:
                crack_time = str(round(seconds / 3600)) + " hours"

            elif seconds < 31536000:
                crack_time = str(round(seconds / 86400)) + " days"

            else:
                crack_time = str(round(seconds / 31536000)) + " years"

        print("Estimated Crack Time:", crack_time)
        
        # SUGGESTIONS

        suggestions = []

        if length < 12:
            suggestions.append("Use 12 or more characters")

        if upper == 0:
            suggestions.append("Add an uppercase letter")

        if lower == 0:
            suggestions.append("Add a lowercase letter")

        if digit == 0:
            suggestions.append("Add a digit")

        if special == 0:
            suggestions.append("Add a special character")

        if password.lower() in common_passwords:
            suggestions.append("Avoid common passwords")

        if len(suggestions) == 0:
            print("Suggestions: None. Great password!")

        else:
            print("Suggestions:")

            for tip in suggestions:
                print("-", tip)

    # VERSION 6: PASSWORD GENERATOR

    elif choice == "2":

        size = input("Enter password length (8 or more): ")

        if not size.isdigit() or int(size) < 8:
            print("Please enter a number that is 8 or more")

        else:

            size = int(size)

            chars = string.ascii_letters + string.digits + string.punctuation

            new_password = ""

            for i in range(size):
                new_password += secrets.choice(chars)

            print("Generated Password:", new_password)

    # EXIT

    elif choice == "3":

        print("Thank you for using PassGuard!")
        break

    else:
        print("Invalid choice. Enter 1, 2 or 3.")
