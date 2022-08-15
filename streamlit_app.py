import streamlit as st

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
#with tab1:
#    st.write("Tab 1")
# with tab2:
#    st.write("Tab 2")
# with tab3:
#    st.write("Tab 3")

if tab1:
#    curr_tab = "Cat"
   st.write("clicked tab1")
# elif tab2:
#    curr_tab = "Dog"
#    st.write("clicked tab2")
# elif tab3:
#    curr_tab = "Owl"
#    st.write("clicked tab3")


st.write(curr_tab)
st.write(tab1)
