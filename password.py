import random
import string
import requests

def randomCharacter():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)

passwordLength = int(input("Enter the desired length of your password:"))

def generateStrongPassword():
    strongPW = ""
    for i in range(passwordLength):
        strongPW = strongPW + randomCharacter()
    print(strongPW)

generateStrongPassword()

def fetchWord():
    url = "https://random-word-api.herokuapp.com/word?length=6"
    response = requests.get(url)
    word = response.json()[0]
    return word

def generateWeakerPassword():
    word1 = fetchWord()
    word2 = fetchWord()
    word1 = replaceLetters(word1)
    word2 = replaceLetters(word2)
    password = word1 + word2
    return password

def replaceLetters(word):
    word = word[0].upper() + word[1:]
    if "a" in word:
        word = word.replace("a", "@")
    if "l" in word:
        word = word.replace("l", "1")
    if "o" in word:
        word = word.replace("o", "0")
    if "e" in word:
        word = word.replace("e", "3")
    return word

print(generateWeakerPassword())