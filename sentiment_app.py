# -*- coding: utf-8 -*-
"""
Created on Apr 17 2024

@author: Chandana Chaudhry
"""

# -*- coding: utf-8 -*-
"""
Created on Apr 17 2024

@author: Chandana Chaudhry
"""

import pandas as pd
import streamlit as st
import joblib
from joblib import load
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK data
nltk.download('stopwords')

# Initialize stemmer and stopwords
stemmer = PorterStemmer()
ENGLISH_STOP_WORDS = set(stopwords.words('english'))

def my_tokenizer(sentence):
    # Remove punctuation and set to lower case
    for punctuation_mark in string.punctuation:
        sentence = sentence.replace(punctuation_mark, '').lower()

    # Split sentence into words
    list_of_words = sentence.split()

    # Remove stopwords and any tokens that are just empty strings
    list_of_stemmed_words = []
    for word in list_of_words:
        # Stem words and remove stopwords
        stemmed_word = stemmer.stem(word)
        if (stemmed_word not in ENGLISH_STOP_WORDS) and (stemmed_word != ''):
            list_of_stemmed_words.append(stemmed_word)

    return list_of_stemmed_words

def main():
    st.title("Sentiment Analysis")

    # Insert image of sentiment analysis
    # Custom subheader with smaller font size
    st.subheader("Let's predict how you feel!")
    st.image("/Users/gulshanchaudhary/Desktop/capstone_model/5-Top-APIs-For-Sentiment-Analysis.png", use_column_width=True)
    
    st.markdown(
        """
        <div style="font-size: 12px;">
        **This is a simple sentiment analysis app that predicts whether a given text is positive or negative.
        Just enter your review text in the input field, and we'll do the rest!
        </div>
        """,
        unsafe_allow_html=True
    )

     # Dummy table with introduction to sentiment analysis
    st.subheader("What is Sentiment Analysis?")
    st.markdown(
         """
         Sentiment analysis, also known as opinion mining, is the process of determining whether a piece of text 
         expresses positive, negative, or neutral sentiment. It is widely used in various applications, including 
         social media monitoring, customer feedback analysis, and market research.
         """
     )
    st.write("Here's a snippet of train data and actual sentiment:")
    
    # Define your data
    data = {
       'Review Text': [
           "Absolutely wonderful - silky and sexy and comfy all at the same time. it's not super supportive in the breast area, so i went and got a bra with help from a salesperson. the lace is soft and not itchy which is what i was worried about. i just cant get enough of this jumper!",
           "Love this dress! it's sooo pretty. i happened to find it in a store, and i'm glad i did bc i never would have ordered it online bc it's petite. i bought a petite and am 5'8. i love the length on me- hits just a little below the knee. would definitely be a true midi on someone who is truly petite.",
           "I had such high hopes for this dress and really wanted it to work for me. i initially ordered the petite small (my usual size) but i found this to be outrageously small. so small in fact that i could not zip it up! i reordered it in petite medium, which was just ok. overall, the top half was comfortable and fit nicely, but the bottom half had a very tight under layer and several somewhat cheap (net) over layers. imo, a major design flaw was the net over layer sewn directly into the zipper - it c",
           "I love, love, love this jumpsuit. it's fun, flirty, and fabulous! every time i wear it, i get nothing but great compliments!",
           "This shirt is very flattering to all due to the adjustable front tie. it is the perfect length to wear with leggings and it is sleeveless so it pairs well with any cardigan. love it!"
       ],
       'Sentiment': ['Positive', 'Positive', 'Negative', 'Positive', 'Positive']
   }
   
   # Convert data to DataFrame
    df = pd.DataFrame(data)
    
    # Render the table
    st.table(df.style.set_properties(**{'font-size': '12px'}))

    

    # Set up input field
    st.subheader("Enter Your Review Text")
    text = st.text_input("")

    # Use the model to predict sentiment & write result
    if text:
        try:
            model = joblib.load("/Users/gulshanchaudhary/Desktop/capstone_model/sentiment_pipeline.pkl 2")
            prediction = model.predict([text])
            probabilities = model.predict_proba([text])
            if prediction == 1:
                st.success("We predict that this is a positive review!")
            else:
                st.error("We predict that this is a negative review!")
            
            # Display probabilities
            st.write("Probability for Positive Sentiment:", probabilities[0][1])
            st.write("Probability for Negative Sentiment:", probabilities[0][0])
        except Exception as e:
            st.error(f"Error predicting sentiment: {e}")

if __name__ == "__main__":
    main()
