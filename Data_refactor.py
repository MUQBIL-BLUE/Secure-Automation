from Octate import octet_mass as adder


def encoder(received_data):
    initial_list = list(received_data)   # string input to list for encoding
    encoded_list = []
    for count in range(len(initial_list)):
        encoded_list.insert(count, adder() + str(initial_list[count]))
    # return encoded_list                        return encoded list
    # list to string converter
    encoded_string = ""
    for exe in encoded_list:
        encoded_string += exe
    # print(encoded_string)                       print encoded list as combine string
    return encoded_string


def decoder(encode_data):
    initial_list = list(encode_data)    # string input to list for decoding
    z = 1
    a = 0
    decoded_list = []
    for counter in range(len(initial_list)):
        if counter % 9 == 0:
            index = ((8 * z) + (a))
            decoded_list.append(initial_list[index])
            z += 1
            a+=1
    # return decoded_list            return decoded list
    # list to string converter
    decoded_String = ""
    for exe in decoded_list:
        decoded_String += exe
    return decoded_String  # return decoded string

