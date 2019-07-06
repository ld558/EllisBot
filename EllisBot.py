import praw
import pdb
import re
import os
reddit = praw.Reddit('bot1')
subreddit=reddit.subreddit("pythonforengineers")
keyword = '!WEllisBot'

if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

else:
    with open("comments_replied_to.txt","r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))


if not os.path.isfile("reddit_usernames_replied_to.txt"):
    usernames_replied_to=[]

else:
    with open("reddit_usernames_replied_to.txt","r") as f:
        usernames_replied_to = f.read()
        usernames_replied_to = usernames_replied_to.split("\n")
        usernames_replied_to = list(filter(None, usernames_replied_to))



for post in subreddit.hot(limit=5):
    post.comments.replace_more(limit=None)
    i = 0
    for comment in post.comments.list():
        i += 1
        print(i)
        if comment.id not in comments_replied_to:
            if re.search(keyword,comment.body,re.IGNORECASE):
                post.reply("Shut up pleaseeeee, you clapped donnie")
                print("Successful reply to: ", comment.author.name)
                comments_replied_to.append(comment.id)
                usernames_replied_to.append(comment.author.name)

with open("comments_replied_to.txt","w") as f:
    for comment_id in comments_replied_to:
        f.write(comment_id+"\n")

with open("reddit_usernames_replied_to.txt","w") as f:
    for username in usernames_replied_to:
        f.write(username+"\n")

