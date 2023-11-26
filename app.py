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
