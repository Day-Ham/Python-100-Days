import os
print("Write the Word to Encrypt")
WordToEncrypt=input()
print("Input the Number of Shifts")
OffsetNumber=int(input())
CypherWord=''
for letter in WordToEncrypt:
   EncryptedLetter =chr((ord(letter)-OffsetNumber)%26)
   CypherWord +=EncryptedLetter

print(CypherWord)