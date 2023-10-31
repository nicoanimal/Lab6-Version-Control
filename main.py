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

    print("".join(encoded))


while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    menu = input("Please enter an option: ")
    if menu == '1':
        password = input("Please enter your password to encode: ")
        encoder(password)
        print("Your password has been encoded and stored!")
    elif menu == '2':
        print("Nothing happens yet")
    elif menu == '3':
        break
    else:
        print("Input valid command")






