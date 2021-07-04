import hashlib
import os
import tkinter as tk
from tkinter import filedialog, simpledialog



def bxor(b1, b2): # use xor for bytes
    result = bytearray()
    for b1, b2 in zip(b1, b2):
        result.append(b1 ^ b2)
    return result

def getShaBytesStr(password:str):
    return bytearray(hashlib.sha256(password.encode('utf-8')).digest())

def getShaBytes(password:bytearray):
    passwordStr:str = password.hex()
    return bytearray(hashlib.sha256(passwordStr.encode('utf-8')).digest())

def cowCrypt(fileName, password:str = 'NULL'):
    f = open(fileName,'rb')
    data = bytearray(f.read())
    #print(data)
    print('Data size:' , len(data))
    shaTimes = 1
    print('Generating key...')
    pwdSHA = getShaBytesStr(password)
    while(len(pwdSHA) < len(data)):
        pwdSHA.extend(getShaBytes(pwdSHA))
        shaTimes += 1
    print('SHA-256 executed ' + str(shaTimes) + ' times.')

    result = bxor(data, pwdSHA)

    savedFile = open(fileName+'.cow','wb')
    savedFile.write(result)
    savedFile.flush()
    print('Done.')

def cowDecrypt(fileName, password:str = 'NULL'):
    cowCrypt(fileName, password)

#cowCrypt('test.txt')
#cowDecrypt('test.txt.cow')
tk.messagebox.showinfo(title=None, message='Welcome using this cow encryption/decryption tool by Alan Z!')
print()
root = tk.Tk()
root.withdraw()

fileName = filedialog.askopenfilename(title = 'Please select file to encrypt/decrypt:')
pwd = simpledialog.askstring(title = 'Please enter password:',prompt ='Please enter password:')
if(pwd == ''):
    pwd = 'NULL'
if(os.path.isfile(fileName) == False):
    tk.messagebox.showinfo(title=None, message='Error, no such file!')
else:
    cowCrypt(fileName,pwd)
    tk.messagebox.showinfo(title=None, message='Done!')


