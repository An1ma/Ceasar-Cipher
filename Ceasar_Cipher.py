# Ceasar Cipher

def encryption (text,key):
    cipher = []
    cipher_text = []
    result = ''
    for i in range(len(text)):
        cipher.append(ord(text[i])+3)
    
    for i in range(len(cipher)):
        cipher_text.append(chr(cipher[i]))
    
    return result.join(cipher_text)

def decryption (text,key):
    cipher = []
    cipher_text = []
    result = ''
    for i in range(len(text)):
        cipher.append(ord(text[i])-3)
    
    for i in range(len(cipher)):
        cipher_text.append(chr(cipher[i]))
    
    return result.join(cipher_text)


original_text = input("Enter Text: ")
key = int(input("Enter key: "))
text = list(original_text)
output = ''
edited_text = []
tag = int(input("Encryption 1 | Decryption 2: "))

if tag == 1:
    
    print(encryption(text,key))
elif tag == 2:
    
    edited_text = decryption(text,key)
    print(output.join(edited_text))
else:
    print("Error")