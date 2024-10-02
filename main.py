import streamlit as st
st.title("My First Web App")
st.write("WELCOME TO MY WORLD")
st.header("This is a testamet that the Lord is good and kind to me")
st.subheader("Grace is my story")
html_code ="<h1>Hello World</h1>"
st.markdown(html_code, unsafe_allow_html=True)

st.text("The Lord Is my Shepherd, I shall not want.")
st.code("print('Psalm 23:1')")

codes = """
 from sklearn.datasets import make_moons
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import recall_score, precision_score, f1_score
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
 """

st.code(codes, language='python')
st.latex(r'''a+2a^2+3a^3+4a^4''')
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
st.markdown('[Google], www.google.com')

st.caption('I am a chosen generation')

st.image("C:\\Users\\HP\\OneDrive\\Pictures\\WhatsApp Image 2024-05-05 at 17.38.11_68e98ac0.jpg", caption='This is a beautiful picture')

import pandas as pd

data = {
 'Name': ['John', 'Alice', 'Bob', 'Charlie'],
 'Age': [25, 30, 28, 32],
 'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']}
df = pd.DataFrame(data)

st.table(df)

st.dataframe(data)

st.write(df)



st.video("C:\\Users\\HP\\Videos\\Wish.mp4")


royal = st.checkbox("Are you a Queen?")

if royal == True:
 st.write("Welcome Queen")
else:
 st.write("You are not a Queen, out!!!!")


wealth = st.radio("How rich are you?",("Millionaire", "Billionaire", "Trillionaire"))

if wealth == "Millionaire":
 st.write("You are a Millionaire, work harder")
elif wealth == "Billionaire":
 st.write("You are a Billionaire, work a bit harder")
else:
 st.write("Odogwu Trillionaire, you have money but it's not enough")

def click():
 st.success("Form has been submitted Successfully")

st.button("Submit", on_click= click)

st.selectbox("what is yournfavorite food?", options= ("Mash potatoes","Seafood Pasta","Braised Beef Ribs","Calamari Rings"))

options = st.multiselect("What are your favorite colors?", options=("Red", "Blue", "Green", "Yellow", "Orange"))
st.write(f"These are your favorite colors:{','.join(options)}")


st.slider("How old are you?", min_value=0, max_value=100, value=30)
st.slider("Decimal", min_value=0.0, max_value= 10.0, value=0.0, format="%0.2f")

age= st.number_input("Enter your age", value=0)
if age < 18:
 st.error("you are too young")
else:
 st.success("Welcome!")

st.text_input("Enter your name", value="John Doe", max_chars=100)

st.text_area("Enter your message", value="Hello, Streamlit!")

upload= st.file_uploader("Upload a file", type=["pdf", "jpg"], accept_multiple_files=True)
if upload is not None:
 for i in upload:
    if i.name.endswith(".pdf"):
        st.write(f"PDF file uploaded: {i.name}")
 
elif i.name.endswith(".jpg"): 
 st.write(f"filename is {i.name}")
 st.image(i, caption=i.name)
else:
 st.write(f"Unsupported file format: {i.name}")

st.color_picker("Pick a color", value="hashtag#ff0000")

st.text_area("why do you think you should be selected for this Job?")

st.date_input("Enter the date", format="YYYY-MM-DD")

st.time_input("Enter the time:")