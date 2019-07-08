import os

# Print current working directory 
print "Current working dir : %s" % os.getcwd()
with open("/vagrant/home/EllisBot/reddit_usernames_replied_to.txt","w") as f:
   f.write("hello")

