def main():
    print("=== Basic String Operations ===")

    # 1. Get user input
    user_string = input("Enter a string: ")

    print("\n--- Operations ---")
    print(f"Original: {user_string}")
    
    # 2. Convert to uppercase
    upper_str = user_string.upper()
    print(f"Uppercase: {upper_str}")

    # 3. Convert to lowercase
    lower_str = user_string.lower()
    print(f"Lowercase: {lower_str}")

    # 4. Replace a word
    to_replace = input("\nEnter a word to replace: ")
    replacement = input("Enter the new word: ")
    replaced_str = user_string.replace(to_replace, replacement)
    print(f"After replacement: {replaced_str}")

    # 5. Strip whitespace
    stripped = user_string.strip()
    print(f"\nStripped (no leading/trailing spaces): '{stripped}'")

    # 6. Reverse the string
    reversed_str = user_string[::-1]
    print(f"Reversed: {reversed_str}")

    # 7. Check if a word is in the string
    word = input("\nEnter a word to check if it's in your string: ")
    print(f"Is '{word}' in the string? {'Yes' if word in user_string else 'No'}")

    print("\nDone!")

if __name__ == "__main__":
    main()


