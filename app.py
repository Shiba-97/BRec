import streamlit as st
import pickle
import pandas as pd

books_dict = pickle.load(open(r"books_dict.pkl",'rb'))
sim = pickle.load(open(r"similarity.pkl",'rb'))
books = pickle.load(open(r"books.pkl",'rb'))


def recommend(book):
  index=final[final['title']==str(book)].index[0]
  ss=sim[index]
  booklist=sorted(list(enumerate(ss)),reverse=True,key=lambda x:x[1])[:6]
  var=[]
  for i in booklist:
    var.append(final.iloc[i[0]].title)
  return var


st.title('Books Recommender System')
selected_book_name = st.selectbox(
    'Select Books',
    books['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_book_name)
    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(recommendations[0])
        
    with col2:
        st.text(recommendations[1])
        

    with col3:
        st.text(recommendations[2])
        
    with col4:
       st.text(recommendations[3])
    with col5:
        st.text(recommendations[4])
        