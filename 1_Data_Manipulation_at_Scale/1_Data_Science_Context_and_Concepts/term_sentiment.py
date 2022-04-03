import sys
import json
import re

def check_sentiment_score(text):
        import string
        words = unicode(text).split()
        score = 0.0
        for word in words:
            #word = re.sub(r'[^\w\s]','',word).lower()
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

def update_lib(words, lib, score):
    for word in words:
        word = re.sub('[^A-Za-z0-9]+', '', word).lower()
        if word != "":
            if lib.__contains__(word):
                if score>0:
                    lib[word] = lib[word]+1.0
                elif score<0:
                    lib[word] = lib[word]-1.0
            else:
                if score!=0:
                    lib[word] = float(score)
    return lib

def save_new_lib(file, lib):
    f = open(file, "a")
    f.truncate()
    for i in lib:
        print(i+" "+str(lib[i]))
        f.write(i+"\t"+str(lib[i])+"\n")

def main():
    lib = get_dictionary()
    src = open(sys.argv[2])
    for line in src:
        tweetText = json.loads(line, "utf=8").get("text")
        score = check_sentiment_score(tweetText)
        words = unicode(tweetText).split()
        lib = update_lib(words, lib, score)

    # Make sure there's no space between words
    for word in lib.copy():
        w = re.sub('[^A-Za-z0-9]+', '', word).lower()
        lib[w] = lib.pop(word)
    save_new_lib("new_AFINN-111.txt", lib)

if __name__ == '__main__':
    main()
