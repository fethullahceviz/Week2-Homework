import string
word = (input("Enter word:")).lower()
h = list(word)
dic={}
for i in sorted(set(h)):
    dic[i] = h.count(i)
print([(k, v) for k, v in dic.items()])
