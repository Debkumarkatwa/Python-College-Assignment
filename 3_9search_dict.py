def check_key_exists(key):
    if key in my_dict:
        print(f"The key '{key}' exists in the dictionary.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
key_to_check = input("Enter the key to check: ")

check_key_exists(key_to_check)