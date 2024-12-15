import sys

def greet(names):
    for name in names:
        if name[0].islower():
            sys.stderr.write(f"Error: Name '{name}' needs to start with an uppercase letter!\n")
        else:
            print(f"Nice to see you {name}!")

def main():
    try:
        with open('names.txt', 'r') as file:
            names = file.read().splitlines()  
        greet(names)
    except FileNotFoundError:
        sys.stderr.write("Error: The file 'names.txt' was not found!\n")

if __name__ == "__main__":
    main()
