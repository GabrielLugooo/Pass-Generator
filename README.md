<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# PASS GENERATOR

<a href="https://github.com/GabrielLugooo/Pass-Generator" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Pass%20Generator-000000" alt="English Generator" /></a>
<a href="https://github.com/GabrielLugooo/Pass-Generator/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Pass%20Generator-green" alt="Spanish Generator" /></a>

### Objective

This project, Pass-Generator, is a Python-based password generator designed to create strong and secure passwords with customizable parameters.

Users can define the password length, ensuring a balance between security and usability.

This tool is particularly useful for enhancing online security by generating complex passwords that are difficult to crack.

### Skills Learned

- Python programming and working with randomization libraries.
- Efficient user input handling and customization options.
- Understanding cybersecurity best practices, especially password strength and encryption principles.

### Tools Used

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)

### Project

#### Step-by-Step Explanation

1. **Import Necessary Libraries** – The script uses the `string` and `random` libraries to generate secure passwords with different characters.
2. **User Input Validation** – The program ensures the user inputs a valid number for the password length.
3. **Define Available Characters** – The script combines uppercase letters, lowercase letters, numbers, and special characters.
4. **Generate the Password** – Using a loop, the program randomly selects characters from the available pool and concatenates them to create the final password.
5. **Display the Generated Password** – The password is printed for the user.

#### Improved Code with Comments (English)

```python
# Import necessary libraries
import string
import random

def generate_password():
    """Function to generate a secure password based on user-defined length."""
    try:
        # Ask the user for the password length
        length = int(input("Enter the password length: "))

        # Ensure the password length is at least 4 characters
        if length < 4:
            print("Password length should be at least 4 characters for security.")
            return

        # Define available characters: letters, digits, and punctuation
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate the password using random choices and join method
        password = "".join(random.choice(characters) for _ in range(length))

        # Print the generated password
        print("The generated password is: " + password)
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Run the function
generate_password()
```

### Limitations

Pass Generator it's just for educational purpose under the MIT License.

---

<h3 align="left">Connect with me</h3>

<p align="left">
<a href="https://www.youtube.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=55200&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="http://www.tiktok.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=118638&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="https://instagram.com/lugooogabriel" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=32309&format=png" alt="lugooogabriel" height="40" width="40" /></a>
<a href="https://twitter.com/gabriellugo__" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=phOKFKYpe00C&format=png" alt="gabriellugo__" height="40" width="40" /></a>
<a href="https://www.linkedin.com/in/hernando-gabriel-lugo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=8808&format=png" alt="hernando-gabriel-lugo" height="40" width="40" /></a>
<a href="https://github.com/GabrielLugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=80&id=AngkmzgE6d3E&format=png" alt="gabriellugooo" height="34" width="34" /></a>
<a href="mailto:lugohernandogabriel@gmail.com"> <img align="center" src="https://img.icons8.com/?size=50&id=38036&format=png" alt="lugohernandogabriel@gmail.com" height="40" width="40" /></a>
<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://simpleicons.org/icons/linktree.svg" alt="gabriellugooo" height="40" width="40" /></a>
</p>

<p align="left">
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Version-000000" alt="English Version" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Version-Green" alt="Spanish Version" /></a>
</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Credits-Gabriel%20Lugo-green" alt="Credits" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Profile%20views&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="Last Edited" /></a>
