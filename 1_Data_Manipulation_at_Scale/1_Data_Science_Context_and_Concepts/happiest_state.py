import sys 
import re
import json

def get_states():
    states_dict = ['WA', 'WI', 'WV', 'FL', 'WY', 'NH', 'NJ', 'NM', 'NA', 'NC', 'ND', 'NE', 'NY', 'RI', 'NV', 'GU', 'CO', 'CA', 'GA', 
        'CT', 'OK', 'OH', 'KS', 'SC', 'KY', 'OR', 'SD', 'DE', 'DC', 'HI', 'PR', 'TX', 'LA', 'TN', 'PA', 'VA', 'VI', 'AK', 'AL', 
        'AS', 'AR', 'VT', 'IL', 'IN', 'IA', 'AZ', 'ID', 'ME', 'MD', 'MA', 'UT', 'MO', 'MN', 'MI', 'MT', 'MP', 'MS'] 

    states = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
    }

    for state in states.copy():
        s = state.lower()
        states[s] = states.pop(state)

    return [i.lower() for i in states_dict], states

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

def get_location(tweet):
    if tweet.get("lang")=="en":
        location = tweet.get("user").get("location").encode("utf-8").split()
        for i in location:
            location[location.index(i)] = re.sub('[^A-Za-z0-9]+', '', i).lower()
        return location
    else:
        return []

def update_state(state, score, state_dict):
    if state_dict.__contains__(state):
        state_dict[state] += score
    else:
        state_dict[state] = score
    return state_dict

def main():
    file = open(sys.argv[2])

    state_score = {}
    for line in file:
        tweet = json.loads(line, "utf=8")
        location = get_location(tweet)
        state_list, state_dict = get_states()
        for i in location:
            if i in state_list: 
                score = check_sentiment_score(tweet.get("text"))
                state_score = update_state(i, score, state_score)
        
    try:
        highest_state = max(state_score, key=state_score.get)
    except:
        pass
    print(state_dict[highest_state])

if __name__ == '__main__':
    main()
