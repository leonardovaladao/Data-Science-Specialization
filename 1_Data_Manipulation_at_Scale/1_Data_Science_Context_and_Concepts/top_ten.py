import sys
import json
from types import NoneType
from collections import Counter

def main():
    tweet_file = open(sys.argv[1])
    hashtags_list = []

    for line in tweet_file:
        tweet = json.loads(line, "utf=8")
        if type(tweet.get("entities")) != NoneType:
            if tweet.get("entities").get("hashtags") != []:
                hashtags = tweet.get("entities").get("hashtags")

                for hashtag in hashtags:
                    h = hashtag.get("text")
                    hashtags_list.append(h)

    occurences = dict(Counter(hashtags_list))
    sorted_occurences = sorted(occurences.items(), key=lambda x: x[1], reverse=True)
    top_ten = sorted_occurences[:10]

    for i in top_ten:
        print(i[0].encode("utf-8")+" "+str(i[1]))
    

if __name__ == '__main__':
    main()