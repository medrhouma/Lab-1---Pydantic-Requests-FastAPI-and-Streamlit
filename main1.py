import streamlit as st
import pandas as pd
import numpy as np
st.write('Hello World')
# this capture the return value into x
x = st.text_input('Favorite Movie?')

st.write(f"Your favorite movie is: {x}")
is_clicked = st.button("Click Me")


st.write("## This is a H2 Title!")

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
data = pd.read_csv("movies.csv")
# This shows the data in a nice table
st.write(data)  # display the data inside the app

# Some random generated data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)