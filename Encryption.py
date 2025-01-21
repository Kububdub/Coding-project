def encrypt(message,keyword):
    key_arr = []
    mssg_arr = []
    positions = []
    encrypted = []
    out = ""
    for letter in keyword:
        key_arr.append(letter)
    for letter in message:
        mssg_arr.append(letter)
    
    for item in key_arr:
        greatest = key_arr[0]
        for i in range(0,len(key_arr)-1):
            if greatest < key_arr[i+1]:
                greatest = key_arr[i+1]
        positions.append(key_arr.index(greatest))
        key_arr[key_arr.index(greatest)]= "a"

    complete = False
    while not complete:
        for i in range(0,len(positions)):
            try: encrypted.append(mssg_arr[positions[i]])
            except: continue
            if i == len(mssg_arr)-1:
                complete = True
            else:
                continue
        for i in range(0,len(positions)):
            mssg_arr.pop(0)
            if len(mssg_arr) == 0:
                complete = True
                break

    for j in range(0,len(encrypted)):
        out = out + str(encrypted[j])
    return(out)


#this is a carbon copy of the encryption algorythm
'''def decrypt(message,keyword):
    key_arr = []
    mssg_arr = []
    positions = []
    encrypted = []
    out = ""
    for letter in keyword:
        key_arr.append(letter)
    for letter in message:
        mssg_arr.append(letter)
    
    for item in key_arr:
        greatest = key_arr[0]
        for i in range(0,len(key_arr)-1):
            if greatest < key_arr[i+1]:
                greatest = key_arr[i+1]
        positions.append(key_arr.index(greatest))
        key_arr[key_arr.index(greatest)]= "a"
        print(greatest)
        print(key_arr)
    print(positions)
    complete = False
    while not complete:
        for i in range(0,len(positions)):
            try: encrypted.append(mssg_arr[positions[i]])
            except: continue
            if i == len(mssg_arr)-1:
                complete = True
            else:
                continue
        for i in range(0,len(positions)):
            mssg_arr.pop(0)
            if len(mssg_arr) == 0:
                complete = True
                break
        print(encrypted)

    for j in range(0,len(encrypted)):
        out = out + str(encrypted[j])
    return(out)'''


#WILL NOT WORK PROPERLY IF KEYWORD CONTAINS AN "a"

#here, the illusion of choice
who_cares = input("do you want to encrypt or decrypt?")

message = input("what is your message")
keyword = input("what is your key word (WARNING: code may not work if keyword contains letter 'a')")
print(encrypt(message,keyword))