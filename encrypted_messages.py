import base64
import string
import random

mode=input("select mode (1)Encrypt or (2)Decryption\n")
x=0
D=0

#Encrypt message
if mode == '1':
 Decryption_key = random.randint(1,26)
 plain_text = input("enter message:\n")
 #Encrypt message with Caesar Encryption
 shift = Decryption_key
 shift %= 26
 alphabet = string.ascii_lowercase
 shifted = alphabet[shift:] + alphabet[:shift]
 table = str.maketrans(alphabet, shifted)
 Caesar_encrypted = plain_text.translate(table)
 # output is Caesar_encrypted
 #Encrypt message with 64 bit
 message = Caesar_encrypted
 message_bytes = message.encode('ascii')
 base64_bytes = base64.b64encode(message_bytes)
 base64_message = base64_bytes.decode('ascii')
 #loop Encrypton
 while (x<6):
  message = base64_message
  message_bytes = message.encode('ascii')
  base64_bytes = base64.b64encode(message_bytes)
  base64_message = base64_bytes.decode('ascii')
  x=x+1
 print ("\nDecryption key:")
 print(Decryption_key)
 print ("Encrypted message:")
 print(base64_message)

#Decryption
if mode == '2':
 base64_message = input ('\nEnter encrypted message:\n')
 base64_bytes = base64_message.encode('ascii')
 message_bytes = base64.b64decode(base64_bytes)
 message = message_bytes.decode('ascii')
 #loop 64 bit Decryption
 while (D<6):
  base64_message = message
  base64_bytes = base64_message.encode('ascii')
  message_bytes = base64.b64decode(base64_bytes)
  message = message_bytes.decode('ascii')
  D=D+1
 #Decryption of Caesar encryption
 k = input ('Enter decryption key: ')
 key = int(''.join(filter(str.isdigit, k)))
 plain_text = message
 shift = 26
 shift = shift - key
 shift %=26
 alphabet = string.ascii_letters
 shifted = alphabet[shift:] + alphabet[:shift]
 table = str.maketrans(alphabet, shifted)
 Caesar_encrypted = plain_text.translate(table)
 print ("\nUnencrypted message:")
 print(Caesar_encrypted)
print ("\nThank you for using unofficial encrypted messages ")
print ("By a real company")
#By Brodey Halse
