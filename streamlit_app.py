import streamlit as st

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
if tab1:
   curr_tab = "Cat"
elif tab2:
   curr_tab = "Dog"
elif tab3:
   curr_tab = "Owl"
