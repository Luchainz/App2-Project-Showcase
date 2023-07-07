import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/luther_nft_.jpeg")

with col2:
    st.title("Luchainz")
    content = """
    Hi, i'm Luchainz. New to Python, 
    and interested in web development, 
    machine learning, and data analysis. Tap in!
    """
    st.info(content)
