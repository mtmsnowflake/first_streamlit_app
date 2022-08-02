
import streamlit
import pandas 
streamlit.title('My parents New Healthy Diner')
streamlit.header('🍞 Breakfast')
streamlit.text('espinafre, brocolis, couve, abobrinha, leite de oco, batata, salsäo, pimentäo')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

