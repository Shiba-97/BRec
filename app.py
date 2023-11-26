import streamlit as st
import pickle
import pandas as pd


# Load the saved objects from the binary files
books_dict = pickle.load(open(r"books_dict.pkl",'rb'))
sim = pickle.load(open(r"similarity.pkl",'rb'))
books = pickle.load(open(r"books.pkl",'rb'))


# Recommendation function
def recommend(book):
  index=books[books['title']==str(book)].index[0]
  ss=sim[index]
  booklist=sorted(list(enumerate(ss)),reverse=True,key=lambda x:x[1])[:6]
  var=[]
  for i in booklist:
    var.append(books.iloc[i[0]].title)
  return var

# Streamlit web app
st.title('Books Recommender System')

# Dropdown for selecting books
selected_book_name = st.selectbox(
    'Select Books',
    books['title'].values)

# Button to trigger recommendations
if st.button('Recommend'):
    recommendations = recommend(selected_book_name)
    for item in recommendations:
       st.subheader(item)

