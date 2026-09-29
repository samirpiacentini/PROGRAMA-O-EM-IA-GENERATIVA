import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st 

nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')


st.title('Analise de sentimento')

texto = st.text_input('Digite um texto')


sid = SentimentIntensityAnalyzer()


# Passo 1: Tokenizar
tokens = word_tokenize(texto, language='portuguese')

# Passo 2: Remover stop words
stop_pt = set(stopwords.words('portuguese'))
texto_limpo = [p for p in tokens
               if p.lower() not in stop_pt]

st.write("Original:", texto)
st.write("Tokens:", tokens)
st.write("Limpo:", texto_limpo)

# analise de sentimento

sia  =  SentimentIntensityAnalyzer()

sentimento =  sia.polarity_scores(texto)

st.write(sentimento)

score  =  sentimento['neg'] +  sentimento['pos'] +  sentimento ['neu']

score_ = sentimento['compound']

# st.subheader(score)

if st.button('ANalisar'):
    if score_ >= 0.22:
       st.write('POsitivo') 
    elif score_ <= - 0.1:
       st.write('Negativo')
    elif score_ == 0:
       st.write('Neutro')

       