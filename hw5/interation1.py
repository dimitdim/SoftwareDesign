from pattern.web import Twitter, hashtags

T=Twitter(language="en")

for tweet in T.search("#oscars", start=None, count=5, cached=False):
    print tweet.text
