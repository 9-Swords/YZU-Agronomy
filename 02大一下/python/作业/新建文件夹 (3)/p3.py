plaintext=input('请输入明文：')
ciphertext = ''
for char in plaintext:
    if char.islower():              
        ciphertext += chr((ord(char)- 97 + 3)% 26 + 97)
    elif char.isupper():
        ciphertext += chr((ord(char)- 65 + 3)% 26 + 65)
    else:
        ciphertext += char   
print('明文为：'+plaintext)
print('密文为：'+ciphertext)
