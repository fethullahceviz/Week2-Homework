n = int(input("Enter_a_number:"))
s = list(range(1, (n+1)))
#print(s)
i=1
while i<len(s):
    del s[i::i+1]
    #print ("luckyNumbers :",(s))
    i+=1
print ("luckyNumbers :",(s))
