from addsub import add, sub 

def main():
    print("Welcome to the calculator app")

    print("""
    1. Addition
    2. Subtraction
    """)

    choice = int(input("enter your choice\n"))

    a = int(input("enter the first number\n"))
    b = int(input("enter the second number\n"))

    if choice == 1:
        result = add(a, b)
    elif choice == 2:
        result = sub(a, b)

    print(result)

if __name__ == "__main__":
    main()