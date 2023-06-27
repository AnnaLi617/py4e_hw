fname=input('Enter file name:')
if len(fname)<1: fname='clown.txt'
fh=open(fname,'r')

#count the words using dictionary 
di={}
for line in fh:
    line=line.rstrip()
    words=line.split()
    for word in words:
        di[word]=di.get(word,0)+1 

#print(di)

#find the 5 most common words
lst=[]
for k,v in di.items():
    newtup=(v,k)
    lst.append(newtup)
    lst=sorted(lst, reverse=True)

for v,k in lst[:5]:
    print(k,v)
