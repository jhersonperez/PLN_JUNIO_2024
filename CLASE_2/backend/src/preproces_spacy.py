import spacy
import string

nlp=spacy.load('es_core_news_sm')

def preprocessing(paragraphs:str, do_stem:bool=False, do_post:bool=False) ->dict:
  a_doc = nlp(paragraphs)
  # Segmentation -- Cuando es un parrafo debo separar las oraciones
  lsentences = [a_sentence.text.strip() for a_sentence in a_doc.sents]
  # Tokenization 
  lltokens = [a_token for a_token in a_doc]
  # Lemmatization
  llemmatized = [a_token.lemma_ for a_token in a_doc]
  
  # Remove Stop words
  filtered = [w for w in llemmatized if nlp.vocab[w].is_stop == False]
  # Remove punctuation
  filtered = [[a_token for a_token in a_sentence if not(a_token in string.punctuation)] for a_sentence in filtered]

  return {"paragraphs":paragraphs, "sentences":lsentences, "tokens":lltokens,
            "lemma":llemmatized, "result":filtered}


# ## testing preprocessing
# a_paragraph = "Un párrafo es una unidad de un texto compuesta por una o varias oraciones"\
#   ", que comienza con una mayúscula y que termina con un punto y aparte. Los textos se "\
#   "organizan de manera tal que cada párrafo trata sobre una idea central. "\
#   "Generalmente, la primera oración de cada párrafo suele explicitar cuál es el "\
#   "punto principal que se desarrollará."

# result= preprocessing(a_paragraph)
# print(result["result"])