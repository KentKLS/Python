
alpha = list("abcdefghijklmnopqrstuvwxyz!,.:? ")
# def vigenere(message, cle):
#     message_chiffre = ""
#     cle = cle.lower()
#     for i, letter in enumerate(message):
#         if letter in alpha:
#             index = alpha.index(letter)
#             decalage = alpha.index(cle[i % len(cle)])+1
#             vigenere_letter = alpha[(index + decalage) % len(alpha)]
#             message_chiffre += vigenere_letter
#         else:
#             message_chiffre += letter 
#     return message_chiffre

a = 8
g = 5
n = 25926
def intermediaryKey():
    return (g**a)%n

A = intermediaryKey()

# B = fournis par l'autre parti
B = 14045
def finalKey(B):
    return (B**a)%n

C = finalKey(B)



def vigenere(message, cle):
    cle = str(cle)
    message_chiffre = ""    
    cle = cle.lower()
    for i, letter in enumerate(message):
        if letter in alpha:
            index = alpha.index(letter)
            decalage = int(cle[i % len(cle)])
            vigenere_letter = alpha[(index + decalage) % len(alpha)]
            message_chiffre += vigenere_letter
        else:
            message_chiffre += letter 
    return message_chiffre

Y = vigenere("une phrase, peut etre",C)






def chiffrement(msg, e, n):
    # intLetters = [ str(ord(letter)) for letter in msg ]
    # stringLetters = int("".join(intLetters))
    return pow(msg, e, n)


test = chiffrement(3065,17,3233)


def returnTwoNumbers():
    num1 = 1.2
    num2 =2
    num3 = 3
    return num1, num2, num3

test = returnTwoNumbers()

print(test)
