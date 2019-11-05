# Wu-Trump
## Make America Swarm Again

What is this?
------
It's a program that generates tweets by plugging Wu-Tang Clan lyrics and Donald Trump's tweets into a Markov Chain and generating sentences!

Why did you make this?
------
I figured RZA would be proud, but the Clan hasn't noticed my work yet.

You didn't answer the question
------
And the Clan didn't answer my mentions.

How do I use it?
------
1. Clone the repository
2. Generate a set of API tokens for [Tweepy](https://www.tweepy.org/)
3. Run `tweet.py` to fetch the last 1000 tweets from @realDonaldTrump
4. Run `mark.py` to generate a set of sentences from the lyric text files stored in `WuTang/` and tweets stored in `Trump/`

The scripts must be run in Python 2.

References used:
------
https://github.com/jsvine/markovify - Markov Implementation

https://hackernoon.com/automated-text-generator-using-markov-chain-de999a41e047 - Guide that helped with input formatting and stuff
