import streamlit as st
import numpy as np

tab_Portfolio, tab_Resume, tab_About = st.tabs(["Portfolio", "Resumé", "About"])

with tab_Portfolio:
    st.write("Tab Port")
with tab_Resume:
    info_container = st.container(border=True)
    info_container.markdown("### Dinosaurus")
    info_container.markdown("#### Business Analysts")
    
with tab_About:
    st.write("Tab About")



