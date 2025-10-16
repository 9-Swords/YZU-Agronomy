person = {"li":18,"wang":50,"zhang":20,"sun":22}
max_age = 0
#**********FOUND**********
for key,value in person.items():
#**********FOUND**********
    if value >= max_age:
        max_age = value
#**********FOUND**********
        name = key
print(name)
print(max_age)
