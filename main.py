def encode(password):

    input_array = [int(char) for char in password]
    for i in range(len(input_array)):
        new_digit = input_array[i] + 3
        input_array[i] = new_digit % 10
    result_string = ''.join(map(str, input_array))
    return result_string


#Ethan Reinhart
def decode(saved_pass):
    input_array = [int(char) for char in password]
    for i in range(len(input_array)):
        new_digit = input_array[i] -3
    orginal_password = ''.join(map(str, input_array))
    return orginal_password

def console():
    print("menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

__main__ = __name__

running = 1
while running == 1:
    console()
    menu_value = int(input("please enter an option"))
    if menu_value > 3 or menu_value < 1:
        print("incorrect input format. Please try again")
    else:
        if menu_value == 1:
            password = input("Please enter your password to encode: ")
            while len(password) !=8:
                print("incorrect format please try again")
                password = input("please enter your password to encode")
            saved_pass = encode(password)
            print("Your password has been encoded and stored!")
        elif menu_value == 2:
            try:
                decoded = decode(saved_pass)
                print(f"The encoded password is {saved_pass}, and the orginal password is, {decoded}")
            except:
                print("No stored password")
        if menu_value == 3:
            break