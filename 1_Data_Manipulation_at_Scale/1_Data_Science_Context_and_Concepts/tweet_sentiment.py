import re
import sys

def check_sentiment_score(text):
        words = unicode(text).split()
        score = 0.0
        for word in words:
            word = re.sub('[^A-Za-z0-9]+', '', word).lower()
            word_score = get_dictionary().get(word, 0.0)
            score += word_score
        return score

def get_dictionary():
        afinnfile = open(sys.argv[1])
        scores = {}
        for line in afinnfile:
          term, score  = line.split("\t")
          scores[term] = int(score)    
        return scores

def get_output():
        import json
        with open(sys.argv[2]) as tf:
            for line in tf:
                tweet = json.loads(line, "utf=8")
                tweetText = tweet.get("text")
                score = check_sentiment_score(tweetText)
                print(score)

def main():
    get_output()

if __name__ == '__main__':
    main()
