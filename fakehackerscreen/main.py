import time

print('Welcome to FakeHackerScreen. Want to fool your friends and make them think you are a hacker? This is the right tool! \n \n')

response_isvalid = False

while response_isvalid == False :
    print('PLEASE SELECT THE SCREEN YOU WOULD LIKE TO SHOW BY TYPING THE CORRESPONDING NUMBER IN THE INPUT FIELD: \n 1. BINARY \n 2. C++ CODE \n')
    response = input()
    
    if response == '1' or response == '2' :
        response_isvalid = True
    else :
        print('#ERR_DISPTYPE_INPUT_INVLD \n INVALID INPUT. TRY AGAIN. \n')

response_isvalid = False 

while response_isvalid == False :
    print('PLEASE PROVIDE THE DESIRED DISPLAY DURATION IN SECONDS (ONLY ENTER THE DURATION, WITHOUT THE UNITS AT THE END) \nTYPE "i" IF YOU WANT THE PROGRAM TO RUN INDEFINETLY. \nTYPE "s" IF YOU WANT TO GO THROUGH THE FILE EXACTLY ONCE.\n')
    duration = input()

    if duration == 's' or duration == 'i':
        response_isvalid = True
    else :
        try:
            int(duration)
            response_isvalid = True
        except ValueError:
            print("#ERR_DURATION_INPUT_INVLD \n INVALID INPUT. TRY AGAIN. \n")

if response == '1' :
    srcfile = open('binary.txt', 'r')
    if duration == 's':
        for char in srcfile.readline() :
            print(char, end='')
            time.sleep(0.01)
    elif duration == 'i':
        while True :
            for char in srcfile.readline() :
                print(char, end='')
                time.sleep(0.01)
            srcfile.seek(0)
    else:
        seconds_count = 0
        for char in srcfile.readline() :
            seconds_count += 0.01
            print(char, end='')
            time.sleep(0.01)
            if seconds_count > int(duration):
                break
elif response == '2':
    srcfile = open('cpp.txt', 'r')
    if duration == 's':
        for char in srcfile.read() :
            print(char, end='')
            time.sleep(0.01)
    elif duration == 'i':
        while True :
            for char in srcfile.read() :
                print(char, end='')
                time.sleep(0.01)
            srcfile.seek(0)
    else:
        seconds_count = 0
        for char in srcfile.read() :
            seconds_count += 0.01
            print(char, end='')
            time.sleep(0.01)
            if seconds_count > int(duration):
                break
else:
    print('#ERR_DISPTYPE_UNEXPECTED \n SOMEHOW THE DISPLAY TYPE WAS WRONG BUT WAS NOT DETECTED BY THE DISPLAY TYPE ERROR CHECKER. EITHER THIS IS AN UNRESOLVED BUG (UNLIKELY) OR YOU ARE DOING SOMETHING FUNKY.')
    