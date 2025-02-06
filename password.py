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

print(fetchWord()+fetchWord())