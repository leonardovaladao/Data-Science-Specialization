import sys
import json
import re

def word_global_counter(file):
    count = 0
    for line in file:
        tweetText = json.loads(line, "utf=8").get("text")
        words = unicode(tweetText).split()
        for word in words:
            count+=1
    return count

def get_word_counts(file):
    lib = {}
    for line in file:
        tweetText = json.loads(line, "utf=8").get("text")
        words = unicode(tweetText).split()
        for word in words:
            word = re.sub('[^A-Za-z0-9]+', '', word).lower()
            if word != "":
                if lib.__contains__(word):
                    lib[word]+=1
                else:
                    lib[word]=1
    return lib

def get_freqs(total_global_words, word_lib):
    for i in word_lib:
        print(i+" "+ str(float(word_lib[i])/total_global_words) )

def main():
    total_words = word_global_counter(open(sys.argv[1]))
    word_counts = get_word_counts(open(sys.argv[1]))
    get_freqs(total_words, word_counts)

if __name__ == '__main__':
    main()