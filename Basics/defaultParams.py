def describe_pet(animal_type="Dog", pet_name="Cooper"):
    print(f"You have a {animal_type} named {pet_name}. Cool pet name!")

# Collect inputs for the first pet
animal_type_1 = input("What Type Of Pet Do You Have (if any)? \n")
pet_name_1 = input(f"What Is The Name Of Your Pet ({animal_type_1})? \n")

# Call describe_pet with the collected inputs
describe_pet(animal_type_1, pet_name_1)

# Collect inputs for another pet
animal_type_2 = input(f"Do You Have Any Other Pet apart from the {animal_type_1} above? \n")
pet_name_2 = input(f"What Is The Name Of Your Pet ({animal_type_2})? \n")

# Call describe_pet again
describe_pet(animal_type_2, pet_name_2)
