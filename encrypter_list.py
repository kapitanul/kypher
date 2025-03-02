cypher=[
    [" ","L"],
    ["a","m"],
    ["b","♂"],
    ["c","p"],
    ["d","R"],
    ["e","s"],
    ["f","T"],
    ["g","#"],
    ["h","█"],
    ["i","w"],
    ["j","X"],
    ["k","y"],
    ["l","聲"],
    ["m","+"],
    ["n","○"],
    ["o","]"],
    ["p","2"],
    ["q","'"],
    ["r","A"],
    ["s","u"],
    ["t",":"],
    ["u","3"],
    ["v","7"],
    ["w","☺"],
    ["x","♥"],
    ["y","♦"],
    ["z","♣"],
    ["A","♠"],
    ["B","•"],
    ["C","◘"],
    ["D","b"],
    ["E","◙"],
    ["F","z"],
    ["G","♀"],
    ["H","♪"],
    ["I","♫"],
    ["J","☼"],
    ["K","►"],
    ["L","◄"],
    ["M","↕"],
    ["N","‼"],
    ["O","¶"],
    ["P","§"],
    ["Q","▬"],
    ["R","↨"],
    ["S","↑"],
    ["T","↓"],
    ["U","→"],
    ["V","←"],
    ["W","∟"],
    ["X","↔"],
    ["Y","▲"],
    ["Z","▼"],
    ["0","░"],
    ["1","▒"],
    ["2","▓"],
    ["3","│"],
    ["4","┤"],
    ["5","╡"],
    ["6","╢"],
    ["7","╖"],
    ["8","╕"],
    ["9","╣"],
]

#########################################

def encrypt(message):
    encmessage=""
    for c in message:
        for i in range(0,len(cypher)):
            if cypher[i][0]==c:
                encmessage+=cypher[i][1]
                break
    return encmessage
def decrypt(decmessage):
    decmessage=""
    for c in message:
        for i in range(0,len(cypher)):
            if cypher[i][1]==c:
                decmessage+=cypher[i][0]
                break
    return decmessage

option= int(input("Press 1 for encryption\nPress 2 for decryption\n"))
if option ==1:
    message = input("Message:")
    print (encrypt(message))
if option ==2:
    message = input("Message:")
    print (decrypt(message))

    