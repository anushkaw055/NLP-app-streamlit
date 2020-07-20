# Core Pkgs
import streamlit as st
import os
from PIL import Image


# NLP Pkgs
from textblob import TextBlob
import spacy
from gensim.summarization import summarize

# Function to Analyse Tokens and Lemma
@st.cache
def text_analyzer(my_text):
	nlp = spacy.load('en')
	docx = nlp(my_text)
	# tokens = [ token.text for token in docx]
	allData = [('"Token":{},\n"Lemma":{}'.format(token.text, token.lemma_))
	            for token in docx]
	return allData

# Function For Extracting Entities


@st.cache
def entity_analyzer(my_text):
	nlp = spacy.load('en')
	docx = nlp(my_text)
	tokens = [token.text for token in docx]
	entities = [(entity.text, entity.label_)for entity in docx.ents]
	allData = ['"Token":{},\n"Entities":{}'.format(tokens, entities)]
	return allData


def main():
	""" NLP Based App with Streamlit """

	st.title("NLP Web App")

	
	st.markdown("""
			
			 This is a Natural Language Processing(NLP) Based App useful for basic NLP task
			implemented using State of he Art API's on Streamlit Framework
			""")
	### features

	st.header('Features')

	st.markdown("""
			#### Basic NLP Tasks:
			+ App covers the most basic NLP task of tokenisation, parts of speech tagging.
				You can paste the desired content or may directly pass the url for the text.
			#### Named Entity Recognition and Sentiment Analysis:
			+ Named Entites like organistion person etc are recognised.Sentiment analysis can help us attain the attitude and mood of the wider public which can then help us gather insightful information about the context.
			
			#### Text Summarisation:
			+ It summerizes the given text into few lines. One can copy paste the article. Text needs be long to ensure the summariser is able to take effect.
			""")

   
    
	

	# Tokenization
	if st.checkbox("Show Tokens and Lemma"):
		st.subheader("Tokenize Your Text")

		message = st.text_area("Enter Text","Type Here ..")
		if st.button("Analyze"):
			nlp_result = text_analyzer(message)
			st.json(nlp_result)

	# Entity Extraction
	if st.checkbox("Show Named Entities"):
		st.subheader("Analyze Your Text")

		message = st.text_area("Enter Text","Type Here ..")
		if st.button("Extract"):
			entity_result = entity_analyzer(message)
			st.json(entity_result)

	# Sentiment Analysis
	if st.checkbox("Show Sentiment Analysis"):
		st.subheader("Analyse Your Text")

		message = st.text_area("Enter Text","Type Here ..")
		if st.button("Analyze",key = 1):
			blob = TextBlob(message)
			result_sentiment = blob.sentiment
			st.success(result_sentiment)

	# Summarization
	if st.checkbox("Show Text Summarization"):
		st.subheader("Summarize Your Text")

		message = st.text_area("Enter Text","Type Here ..")
		summary_options = st.selectbox("Choose Summarizer",['gensim'])
		if st.button("Summarize",key = 1):
			if summary_options == 'gensim':
				st.text("Using Gensim Summarizer ..")
				summary_result = summarize(message)
			else:
				st.warning("Using Default Summarizer")
				st.text("Using Gensim Summarizer ..")
				summary_result = summarize(message)

			st.success(summary_result)

	
	

if __name__ == '__main__':
	main()