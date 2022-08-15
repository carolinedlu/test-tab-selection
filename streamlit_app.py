import streamlit as st

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
   st.write("Tab 1")
with tab2:
   st.write("Tab 2")
with tab3:
   st.write("Tab 3")

if tab1:
   curr_tab = "Cat"
elif tab2:
   curr_tab = "Dog"
elif tab3:
   curr_tab = "Owl"

st.write(curr_tab)
