import streamlit as st
from api import get_words, filter_words

st.header("Solve Spelling Bee!")

letters = st.text_input("Letters")

words = get_words(letters)

must_contain = st.text_input("Center letter")

st.header("Optional filters")

starts_with = st.text_input("Must start with...", '')

length = st.number_input("Word length", min_value=4, max_value=None, value=None, step=1)

words = filter_words(words, starts_with=starts_with, contains=must_contain, length=length)

words.sort()

st.write(', '.join(words))