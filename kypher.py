
def cypher_read():
    file = open('cypher.txt', 'r',encoding='utf-8')
    cypher = []
    line = file.readline()
    while line:
        char,cryptchar= line.strip().split(',')
        cypher += [[char,cryptchar]]
        if any(c.isspace() for c in line) is True:
            cypher += [[' ',cryptchar]]
        line = file.readline()
    file.close()
    return cypher

cypher = cypher_read()
def encrypt(message):
    encmessage = ""
    for c in message:
        for pair in cypher:
            if pair[0] == c:
                encmessage += pair[1]
                break
    return encmessage

def decrypt(message):
    decmessage = ""
    for c in message:
        for pair in cypher:
            if pair[1] == c:
                if c== 'L':
                    decmessage +=' '
                else:
                    decmessage += pair[0]
                    break
    return decmessage

option = int(input("Press 1 for encryption\nPress 2 for decryption\n"))
if option == 1:
    message = input("Message: ")
    print(encrypt(message))
if option == 2:
    message = input("Message: ")
    print(decrypt(message))