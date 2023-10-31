def encoder(password):
    encoded = list(password)
    for i in range(0, len(encoded)):
        encoded[i] = int(encoded[i])
    for i in range(0, len(encoded)):
        if encoded[i] == 7:
            encoded[i] = 0
        if encoded[i] == 8:
            encoded[i] = 1
        if encoded[i] == 9:
            encoded[i] = 2
        else:
            encoded[i] = int(encoded[i]) + 3
    for i in range(0, len(encoded)):
        encoded[i] = str(encoded[i])

    return "".join(encoded)


'''
Written by: Case Zumbrum

decode() encodes an integer password by decreasing each integer by 3

Input:
    password (String): password to be encoded, all characters must be integers and there should be 8 digits

Return:
    decoded_password (String): encoded password
'''
def decode(password):
    decoded_password = ''
    for char in password:
        if char == '0':
            decoded_password += str(7)
        elif char == '1':
            decoded_password += str(8)
        elif char == '2':
            decoded_password += str(9)
        else:
            decoded_password += str(int(char)-3)
    return decoded_password


while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    menu = input("Please enter an option: ")
    if menu == '1':
        password = input("Please enter your password to encode: ")
        encoded = encoder(password)
        print("Your password has been encoded and stored!")
    elif menu == '2':
        decoded = decode(encoded)
        print(f"The encoded password is {encoded}, and the original password is {decoded}.")
    elif menu == '3':
        break
    else:
        print("Input valid command")






