# Job description processing

import re         #Regular Expressions - to find, replace, or clean text using patterns
import nltk       #Natural Language Toolkit - for text processing: tokenization, stemming, tagging, parsing, etc
from nltk.corpus import stopwords   #imports the stopwords list (like "is", "and", "the") 

# Download stopwords once
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))  #Loads a list of common English stopwords (like "is", "the", "and", etc.) 

def clean_text(text):
    # Lowercase
    text = text.lower()

    # Remove special characters and numbers (keep only a-z and spaces)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Tokenize (split into words)
    words = text.split()

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    #Join words back into a cleaned string
    cleaned_text = ' '.join(words)

    return cleaned_text