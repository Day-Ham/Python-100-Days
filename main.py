import os
print("Write the Word to Encrypt")
WordToEncrypt=input()
print("Input the Number of Shifts")
OffsetNumber=int(input())
CypherWord=''
WordToEncrypt = WordToEncrypt.lower()
for letter in WordToEncrypt:
   base = ord('a')
   shifted  =(ord(letter) - base + OffsetNumber) % 26
   EncryptedLetter = chr(shifted + base)
   CypherWord +=EncryptedLetter

print(CypherWord)