import time

## TAKE USER INPUT
user_input = input('Enter a text to print out : ').upper()

output = ''

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for letter in user_input :
    if letter in alphabet :
        i = 0
        while letter != alphabet[i] :
            print(output + str(alphabet[i]))
            i += 1
            time.sleep(0.04)

    output += letter 

    print(output)
