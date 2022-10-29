#!/usr/bin/python
from time import sleep
import praw
import re
import string

from email.message import EmailMessage
import ssl 
import smtplib

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("watchexchange")
# subreddit = reddit.subreddit("pythonforengineers")
vintageWatchList = r'\bspeedmaster\b|\bseamaster\b|\bdatejust\b|\btank\b|\bprimero\b'
anyWatchList = r'\bluch\b|\bkurono\b|\bnomos\b|\bspaceview\b|\bautodromo\b|\bhked\b'
yearRange = '(19[0-8]\d)'


def emailWatchLink(link):
    email_sender = 'my.reddit.watch.bot@gmail.com'
    email_password = 'ewsnxcopcliukdll'
    email_reciever = 'abertjames235@gmail.com'
    subject = "Here's a watch I thought you might like"
    body = link

    em = EmailMessage()

    em['from'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())
    
    # print('success')

def watchBot(newSubmission):
        if re.search( vintageWatchList, newSubmission.title.strip(string.punctuation), re.IGNORECASE):
            # print('i worked for brand')
            for top_level_comment in newSubmission.comments:
                if top_level_comment.author == newSubmission.author and re.search(yearRange, top_level_comment.body, re.IGNORECASE):
                    # print('i worked for a good year check')
                    link = submission.shortlink
                    emailWatchLink(link)
        elif re.search( anyWatchList, newSubmission.title.strip(string.punctuation), re.IGNORECASE):
            link = submission.shortlink
            emailWatchLink(link)
        

for submission in subreddit.stream.submissions(skip_existing=True):
    sleep(60*5)
    # sleep(30)
    watchBot(submission)





