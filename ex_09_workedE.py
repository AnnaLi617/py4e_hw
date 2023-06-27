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

#find the most common word
max_count=0
most_app_w=None

for k,v in di.items():
    if v>max_count: 
        max_count=v
        most_app_w=k
print(most_app_w,max_count)