#首字母缩写
string = 'yang zhou university'
result = ''
while string:    
    string=string.strip()    
    result += string[0]
    n = string.find(' ')
    if n > -1:
        string = string[n:]
    else:
        break
result = result.upper()
print(result)
