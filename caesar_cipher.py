choice = input("Do you want to (E)ncrypt or (D)ecrypt? ")

text = input("Enter your message: ")
shift = int(input("Enter a shift number (e.g. 3): "))

result = ""

# Encryption
if choice == "E":
    for letter in text:
        if 'A' <= letter <= 'Z':
            #ord converts the letter in ASCII NUMBER 
            new_code = ord(letter) + shift
            if new_code > ord('Z'):
                new_code -= 26
            result += chr(new_code)
 #chr turns the number back into a letter
        elif 'a' <= letter <= 'z':
            new_code = ord(letter) + shift
            if new_code > ord('z'):
                new_code -= 26
            result += chr(new_code)
        else:
            result += letter

    print("Encrypted message:", result)

# Decryption
elif choice == "D":
    for letter in text:
        if 'A' <= letter <= 'Z':
            new_code = ord(letter) - shift
            if new_code < ord('A'):
                new_code += 26
            result += chr(new_code)

        elif 'a' <= letter <= 'z':
            new_code = ord(letter) - shift
            if new_code < ord('a'):
                new_code += 26
            result += chr(new_code)
        else:
            result += letter

    print("Decrypted message:", result)

else:
    print("Invalid option. Please choose 'E' or 'D'.")


