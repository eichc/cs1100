# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:07:29 2022

@author: eichc

Encrypt a given phrase into a cypher, decrypt the cypher, and compare the results.
"""

def encrypt(word):
    '''
    Encrypt a word into a cypher.
    '''
    word = word.replace(" a", "%4%")
    word = word.replace("he", "7!")
    word = word.replace("e", "9(*9(")
    word = word.replace("y", "*%$")
    word = word.replace("u", "@@@")
    word = word.replace("an", "-?")
    word = word.replace("th", "!@+3")
    word = word.replace("o", "7654")
    word = word.replace("9", "2")
    word = word.replace("ck", "%4")
    return word

def decrypt(word):
    '''
    Decrypt a cypher into a word.
    '''
    word = word.replace("%4", "ck")
    word = word.replace("2", "9")
    word = word.replace("7654", "o")
    word = word.replace("!@+3", "th")
    word = word.replace("-?", "an")
    word = word.replace("@@@", "u")
    word = word.replace("*%$", "y")
    word = word.replace("9(*9(", "e")
    word = word.replace("7!", "he")
    word = word.replace("%4%", " a")
    return word

if __name__ == "__main__":
    sentence = input("Enter a string to encode ==> ").strip()
    print(sentence)
    print("")

    #Create and print the cypher
    cypher = encrypt(sentence)
    print("Encrypted as ==> " + cypher)

    #Calculate and print the difference in length
    lengthDif = abs(len(sentence) - len(cypher))
    print("Difference in length ==> " + str(lengthDif))

    #Decrypt the cypher and print the result
    decryption = decrypt(cypher)
    print("Deciphered as ==> " + decryption)

    #Check if the decryption and the original sentence are the same
    if sentence == decryption:
        print("Operation is reversible on the string.")
    else:
        print("Operation is not reversible on the string.")