test_tweet = "I luv my &lt;3 iphone &amp; you're aswm apple. DisplayIsAwesome, sooo happppy to be with you :) http://www.apple.com/"

#Escape HTML
#------------------------------------------
import HTMLParser
html_parser = HTMLParser.HTMLParser()
tweet = html_parser.unescape(test_tweet)

#Decoding data
#------------------------------------------
tweet = test_tweet.decode('utf8').encode('ascii', 'ignore')

#Apostrophe search
#------------------------------------------
APOS = {"'s" : "is", "'re": "are"}
words = test_tweet.split()
transformed_tweet = [APOS[word] if word in APOS else word for word in words]
transformed_tweet = " ".join(transformed_tweet)

#Split attached words
#------------------------------------------
import re
cleaned_tweet = " ".join(re.findall('[A-Z][^A-Z]*', test_tweet))

#Normalize words
#------------------------------------------
import itertools
normalized_tweet = "".join("".join(s)[:2] for _, s in itertools.groupby(test_tweet))
