
list = []
for b in range(10):
    list+=[b]
print(list)
three = 0
for k in range(1,len(list)):
    if(k%3==0):
        three+=1
print('Кол-во цифр кратных трем: ',three)



