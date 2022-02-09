a = int(input("enter a number1:"))
n = int(input("enter a number2:"))
list = list(range(1, (a+1)))
# print(list)
if n > 0:
    list = (list[len(list)-n:len(list)]+list[0:len(list)-n])
    print(list)

else:
    list = (list[-n:len(list)]+list[0:(-n)])
    print(list)
