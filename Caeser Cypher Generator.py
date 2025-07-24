import os


print("Do you want to Encode Or Decode a word")
valid= False
Decision=''
while valid==False:
   Decision= input()
   if Decision == 'encode':
      valid=True
   elif Decision == 'decode':
      valid=True
   else:
      print("Input Invalid")



def Encode():
   print("Write the Word to Encrypt")
   WordToEncrypt=input()
   print("Input the Number of Shifts")
   OffsetNumber=int(input())
   CypherWord=''
   for letter in WordToEncrypt:
      if letter.islower():
         base = ord('a')
         shifted  =(ord(letter) - base + OffsetNumber) % 26
         EncryptedLetter = chr(shifted + base)
         CypherWord +=EncryptedLetter
      else:
         base = ord('A')
         shifted  =(ord(letter) - base + OffsetNumber) % 26
         EncryptedLetter = chr(shifted + base)
         CypherWord +=EncryptedLetter   
   print(CypherWord)
def Decode():
   print("Write the Word to Decode")
   WordToEncrypt=input()
   print("Input the Number of Shifts")
   OffsetNumber=int(input())
   CypherWord=''
   for letter in WordToEncrypt:
      if letter.islower():
         base = ord('a') #Use as the reference Archor of the 
         shifted  =(ord(letter) - base - OffsetNumber) % 26
         EncryptedLetter = chr(shifted + base)
         CypherWord +=EncryptedLetter
      else:
         base = ord('A')
         shifted  =(ord(letter) - base - OffsetNumber) % 26
         EncryptedLetter = chr(shifted + base)
         CypherWord +=EncryptedLetter   
   print(CypherWord)
if Decision == 'encode':
      Encode()
elif Decision == 'decode':
      Decode()
else:
   print("None")
