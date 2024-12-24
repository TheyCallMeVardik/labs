import sys
import re

def process_names(input_file, output_file):
    with open(input_file, 'r') as file:
        names_list = file.readlines()
    
    errors = []
    for name in names_list:
        name = name.strip()
        if not name or not name[0].isupper() or not re.match("^[a-zA-Z]+$", name):
            errors.append(f"Error: {name} - invalid name\n")
            continue
        print(f"Hello, {name}!")
    
    if errors:
        with open(output_file, 'w') as file:
            file.writelines(errors)

def ask_user_name():
    try:
        while True:
            name = input("What's your name?\n")
            if name and name[0].isupper() and re.match("^[a-zA-Z]+$", name):
                print(f"Hello, {name}!")
            else:
                print("Invalid name, please try again.")
    except KeyboardInterrupt:
        print("\nSee you later!")

def main():
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        process_names(input_file, output_file)
    else:
        ask_user_name()

if __name__ == "__main__":
    main()
