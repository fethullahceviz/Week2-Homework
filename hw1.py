n = int(input("Enter_a_number:"))
s = list(range(1, (n+1)))
#print(s)

i=1
while i<len(s):
    del s[i::i+1]
    #print ("luckyNumbers :",(s))
    i+=1

print ("luckyNumbers :",(s))


#del my_list[1::2]
#print(my_list)
#del my_list[2::3]
#print(my_list)
#del my_list[3::4]
#print(my_list)
#del my_list[4::5]
#print(my_list)

