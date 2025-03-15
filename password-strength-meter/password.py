import string
import random
import streamlit as st
import re

# Step 1 - Password Generator
def generate_password(length):
    characters = string.digits + string.ascii_letters + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Step 2 - Password Strength Checker
def check_password_strength(password):
    score = 0
    common_passwords = ["12345678", "abc123", "Khan123", "pakistan123", "password"]
    
    if password in common_passwords:
        return "❌ This password is too common, choose a more unique one", "Weak"

    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔹 Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔹 Include both uppercase and lowercase letters")

    if re.search(r"\d", password):  # Corrected regex
        score += 1
    else:
        feedback.append("🔹 Add at least one number (0-9)")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔹 Include at least one special character (!@#$%^&*)")

    # Fixing strength classification
    if score == 4:
        return "✔ Strong password!", "Strong"
    elif score == 2 or score == 3:
        return "⚠ Moderate password - consider adding more security features", "Moderate"
    else:
        return "\n".join(feedback), "Weak"

# Streamlit UI
st.title("🔐 Password Strength Checker & Generator")

# Password Strength Checking Section
check_password = st.text_input("Enter your password", type="password")
if st.button("Check Strength"):
    if check_password:
        result, strength = check_password_strength(check_password)
        if strength == "Strong":
            st.success(result)
            st.balloons()
        elif strength == "Moderate":
            st.warning(result)
        else:
            st.error("Weak password - improve it using these tips:")
            for tip in result.split("\n"):  # Corrected newline split
                st.write(tip)
    else:
        st.warning("⚠ Please enter a password")  # Fixed typo in `st.warning`

# Password Generator Section
password_length = st.number_input("Enter the length of password", min_value=8, max_value=20, value=10)
if st.button("Generate Password"):
    password = generate_password(password_length)
    st.success(f"🔑 Generated Password: `{password}`")
