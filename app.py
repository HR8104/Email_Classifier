import streamlit as st
import pickle

model = pickle.load(open('spam.pkl','rb'))
cv = pickle.load(open('vectorizer.pkl','rb'))


st.title("Email Spam Classification Application")
st.write("rhis is a machine learning application to classify emails as spam or ham")
st.subheader("Classification")

user_input = st.text_area("Enter an email: ")

if st.button("Classify"):
	data =[user_input]
	vect = cv.transform(data)
	pred = model.predict(vect)
	print(pred)

	if user_input is None :
		st.write("Enter message")
	elif pred[0] == 1:
		st.write("Email is spam")
	else:
		st.write("Email is not spam")

