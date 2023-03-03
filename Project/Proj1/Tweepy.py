import snscrape.modules.twitter as sntwitter


def scrapper(query, n_tweet):
    tweets = []
    max_tweet = n_tweet
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) > max_tweet:
            break
        tweets.append([tweet.date, tweet.user.username, tweet.rawContent])
    results = []
    for tweetObj in tweets:
        results.append({
            "date": tweetObj[0],
            "user": tweetObj[1],
            "tweet": tweetObj[2]
        })
    return results



