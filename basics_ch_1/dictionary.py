sample_dict = {}
# Ask the user for input
while True:
    key_input = input("Enter a key (or 'q' to quit): ")

    # Check if the user wants to quit
    if key_input.lower() == 'q':
        break

    # Ask the user for the corresponding value
    value_input = input("Enter a value: ")

    # Add the key-value pair to the dictionary
    sample_dict[key_input] = value_input



for k,v in sample_dict.items():
    print(f"{k}:{v}")