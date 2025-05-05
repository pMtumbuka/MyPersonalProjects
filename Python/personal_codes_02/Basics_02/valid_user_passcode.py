def is_valid_password(s):
    state = "q0"
    for char in s:
        if state == "q0" and char == "a":
            state = "q1"
        elif state == "q1" and char == "b":
            state = "q2"
        elif state == "q2" and char == "c":
            state = "q3"
        else:
            return False  # invalid transition
    return state == "q3"

# Keep asking until a valid password is entered
while True:
    user_input = input("Enter your 3-character password: ")
    if is_valid_password(user_input):
        print("✅ Password accepted.")
        break
    else:
        print("❌ Invalid password. Try again.\n")
