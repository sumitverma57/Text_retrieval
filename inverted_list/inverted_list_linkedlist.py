import words_tokenizer
import numpy as np
import linked_list
n=input("Enter the no. of files you want to tokenize.")
key=[""]*n
inv_list=[]
dic={}
for i in range(n):
    files=[]
    files.append(raw_input( "Enter the file name you want to tokenize"))
    key[i]=words_tokenizer.word_tokenizer(files)
#print "key",key

def make_dict(x1,l):
    if x1 in dic.keys():
        dic[x1][0]+=l[0]
        ls=dic[x1][1]
        ls.add_tail(l[1])
        dic[x1][1]=ls
        print x1
    else:
        ls=linked_list.Slist()
        ls.add_first(l[1])
        dic[x1]=[l[0],ls]

#making a dicionary of each and every unique term with their count and posting array

for i in range(n):
    for x in set(key[i]):
        make_dict(x,[key[i].count(x),i+1])

#finally making a inverted list
for key in dic.keys():
    inv_list.append([key,dic[key][0],dic[key][1]])
print inv_list
