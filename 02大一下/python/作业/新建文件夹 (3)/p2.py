plaintext=input('请输入明文：')
ciphertext=''
for char in plaintext:
    if ord('A')<=ord(char)<=ord('Z') or ord('a')<=ord(char)<=ord('z'): 
        ciphertext += chr(ord(char)+3)
    else:
        ciphertext += char
print('明文为：'+plaintext)
print('密文为：'+ciphertext)

