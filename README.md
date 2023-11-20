# telenamechecker.py
A simple, semi-decent name availibility checker for Telegram. 

HOW THE BOT WORKS:
1. The way it works is it sends HTTP requests to t.me/{name} and input a word from a given word list into the {name} and check to see if the name is registered to an account already or not.
2. The bot takes words from the words list and makes them pluralized to see if the plural form of a specific word is availible.
3. It skips over words that are less than 5 letters, or two part words.


A problem that I am running into is that the bot shows accounts that do not exist or were banned, as availible, so it prints out a lot of false positives in the output.
I am working on how to fix this as of right now.


HOW TO USE THE BOT:

1. Import the required python modules (os, requests, re, time).
2. Create a word list (.txt file) and put it in the same folder as the bot.
3. Get words from https://relatedwords.org and copy and paste the words you would like to check
4. Run the bot and let it do its thing for like a minute.

#Originally I had the bot check each word and print out if its availible one by one, but I changed it so you have to wait and I will give you all the results in one print. (if that makes sense ;P)
