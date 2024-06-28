import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import string

# Descargar punkt
nltk.download("punkt") # tokenizacion considerando puntuacion
# Descargar punkt
nltk.download("wordnet") # red semantica para POSTag y Lematizacion
# Descargar diccionarion de stopwords
nltk.download("stopwords")
# Open Multilingual wordnet -- red semantica multilingue
nltk.download("omw-1.4")

## Creo los procesadores que voy a utilizar
stemmer = SnowballStemmer('spanish')
lemmatizer = WordNetLemmatizer()
mystopwords = list(set(stopwords.words('spanish')))

def preprocessing(paragraphs:str, do_stem:bool=False, do_post:bool=False) ->dict:
  # Segmentation -- Cuando es un parrafo debo separar las oraciones
  lsentences = sent_tokenize(paragraphs)
  # Tokenization  
  lltokens = [word_tokenize(a_sentence) for a_sentence in lsentences]
  ## Stemming (Optional)
  lstemmed = None
  if do_stem: 
    lstemmed = [[stemmer.stem(a_token) for a_token in a_sentence] for a_sentence in lltokens]
  ## Postagging (Optional)
  ltagged=None
  if do_post:
    ltagged = [pos_tag(a_sentence) for a_sentence in lltokens]
  # Lemmatization
  llemmatized = [[lemmatizer.lemmatize(a_token) for a_token in a_sentence] for a_sentence in lltokens]
  # Remove Stop words
  filtered = [a_token for a_token in llemmatized if not(a_token in mystopwords) ]
  # Remove punctuation
  filtered = [[a_token for a_token in a_sentence if not(a_token in string.punctuation)] for a_sentence in filtered]

  return {"paragraphs":paragraphs, "sentences":lsentences, "tokens":lltokens,
          "stemed":lstemmed, "tagged": ltagged, "lemma":llemmatized, "result":filtered}

