import re
import nltk
import string

from emot.emo_unicode import UNICODE_EMO, EMOTICONS #not being used RN

# Function for url's
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

# Converting emojis to words
def convert_emojis(text):
    for emot in UNICODE_EMO:
        text = text.replace(emot, "_".join(UNICODE_EMO[emot].replace(",","").replace(":","").split()))
        return text
# Converting emoticons to words    
def convert_emoticons(text):
    for emot in EMOTICONS:
        text = re.sub(u'('+emot+')', "_".join(EMOTICONS[emot].replace(",","").split()), text)
        return text

#emoticon function not yet active
def remove_emoticons(text):
    emoticon_pattern = re.compile(u'(' + u'|'.join(k for k in EMOTICONS) + u')')
    return emoticon_pattern.sub(r'', text)

def clean_tweets(tweet):
    tweet=remove_urls(convert_emojis(convert_emoticons(tweet)))
    #print(tweet)
    #after tweepy preprocessing the colon symbol left remain after      
    #removing mentions
    tweet = re.sub(r':', '', tweet)
    tweet = re.sub(r'‚Ä¶', '', tweet)
    #replace consecutive non-ASCII characters with a space
    tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.word_tokenize(tweet)
    

    #remove emojis from tweet
    #tweet = emoji_pattern.sub(r'', tweet)#filter using NLTK library append it to a string
    
    filtered_tweet = [w for w in word_tokens if not w in stop_words]
    filtered_tweet = []#looping through conditions
    for w in word_tokens:
#check tokens against stop words and punctuations
        if w not in stop_words and w not in string.punctuation:
            filtered_tweet.append(w)
    return ' '.join(filtered_tweet)
    
    #print(word_tokens)
    #print(filtered_sentence)
    #return tweet