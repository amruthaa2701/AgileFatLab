def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    choice = input("Enter choice (1): ")
    if choice == '1':
        c = float(input("Enter Celsius: "))
        print(f"Fahrenheit: {celsius_to_fahrenheit(c)}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
