#10.2 Write a program to read through the mbox-short.txt and figure out 
#the distribution by hour of the day for each of the messages. You can 
#pull the hour out from the 'From ' line by finding the time and then 
#splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

fh=open('mbox-short.txt','r')

d={}
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
        #print(line)
        piece=line.split()
        time=piece[5]
        tpiece=time.split(':')
        hours=tpiece[0]
        d[hours]=d.get(hours,0)+1

for h,c in sorted(d.items()):
    print(h,c)
