Password Checker

This Python program, `check_password.py`, is designed to check the strength of a given password against a list of common passwords stored in a text file named `passwords.txt`. It prompts the user to input a password and then compares it against the list of common passwords. If the password matches any of the common passwords, it alerts the user and indicates the position of the password in the common passwords list. If the password is unique and not found in the list, it confirms its uniqueness.

How it works:
1. Reading Common Passwords:
   - The program reads the common passwords stored in the `passwords.txt` file. It uses the `splitlines()` method to split the content of the file into a list of common passwords.

2. Checking the Password:
   - It iterates through the list of common passwords using a `for` loop and `enumerate()` function to keep track of the index of each password.
   - For each password in the list, it compares it with the user input password.
   - If a match is found, it prints a message indicating that the password is common and shows its position in the list.
   - If no match is found after checking all the common passwords, it confirms that the password is unique.

3. Main Function:
   - The `main()` function prompts the user to enter a password.
   - It then calls the `check_password()` function to check the entered password.

4. Running the Program:
   - The program execution starts from the `__main__` block, which calls the `main()` function.

Example Usage:


Enter the password: mypassword
mypassword:❌(2)

This indicates that the entered password "mypassword" is a common password and is found at position 2 in the list of common passwords.


Enter the password: SecureP@ssw0rd
SecureP@ssw0rd:✅ (Unique)


This indicates that the entered password "SecureP@ssw0rd" is unique and not found in the list of common passwords.