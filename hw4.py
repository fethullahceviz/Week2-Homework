word1=str(input("enter a word1:"))
for i in word1:
    x=tuple(word1)
    #print(sorted(x))
word2=str(input("enter a word2:"))
for j in word2:
    y=tuple(word2)
    #print(sorted(y))
x=set(x)
y=set(y)
my_list=[sorted(x&y),sorted(x-y),sorted(y-x)]
#print(my_list)
output_list=[]
for t in my_list:   
   output_list.append(''.join(t))
print(output_list)