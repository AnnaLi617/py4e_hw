#9.4 Write a program to read through the mbox-short.txt and figure out who 
#has sent the greatest number of mail messages. The program looks for 
#'From ' lines and takes the second word of those lines as the person who 
#sent the mail. The program creates a Python dictionary that maps the 
#sender's mail address to a count of the number of times they appear in the 
#file. After the dictionary is produced, the program reads through the 
#dictionary using a maximum loop to find the most prolific committer.

fh=open('mbox-short.txt')

mail_ad=dict()
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
        #print(line)
        word=line.split()
        sender=word[1]
        #print(sender)
        mail_ad[sender]=mail_ad.get(sender,0)+1

most_sender=None
max_times=0
for sender, times in mail_ad.items():
    if times>max_times:
        most_sender=sender
        max_times=times

#Easier code: 
#most_sender=max(mail_ad,key=mail_ad.get)
#max_times=mail_ad[most_sender]

print(most_sender,max_times)

