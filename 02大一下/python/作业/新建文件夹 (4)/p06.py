li = ["alex  ", "  aric", " Alex ", "Tony  ", "  rain"]
for i in li:
    v = i.strip()
    if v.endswith('c'):
        if v.startswith('a') or v.startswith('A'):
             print(v)
