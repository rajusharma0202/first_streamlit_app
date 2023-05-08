import streamlit

streamlit.title('MY Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega3 3 & Blueberry Oatmeal')
streamlit.text('🥗kale, Spinach and Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
