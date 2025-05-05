# Dictionaries In Py

word_count: str = "34"

word_count_2: int = 34

word_count_3: float = 34.0

my_details = {
    "name": "Patrick Munthali",
    "reg_number": "bsc-com-ne-14-22",
    "email": "bsc-com-ne-14-22@unima.ac.mw"
    }

def print_name():
    print(my_details["name"].upper())

# Only run this if the script is executed directly (not imported)
if __name__ == "__main__":
    # These will only run when this file is executed directly, not imported

    my_details["course"] = "Computer Science"  # Add new key-value pair

    for key, value in my_details.items():
        print(f"{key}: {value}")

    print(my_details)

    print(my_details["name"])  # Output: Patrick Munthali
    print(my_details.get("reg_number"))  # Output: bsc-com-ne-14-22

    print(type(word_count))

    print(type(word_count_2))

    print(type(word_count_3))

    print(type(my_details))
