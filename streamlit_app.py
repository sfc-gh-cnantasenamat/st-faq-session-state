import streamlit as st

st.title('🎈 FAQ: How to prevent app reruns')


#############################################
# 1. Use st.form
st.header('st.form')

with st.form(key='my_form'):
   text_input = st.text_input(label='Enter some text')
   submit_button = st.form_submit_button(label='Submit')

st.write(text_input)


#############################################
# 2.1 Session state
st.header('Session state')

# Initialize session state variables
if 'count' not in st.session_state:
   st.session_state.count = 0

# Update session state variables
if st.button('Increment'):
   st.session_state.count += 1

if st.button('Decrement'):
   st.session_state.count -= 1

# Print session state variable
st.write('Count: ', st.session_state.count)

#############################################
# 2.2 Callback functions
st.header('Callback functions')


if 'squared' not in st.session_state:
   st.session_state.squared = 0

def callback():
   st.session_state.squared = x * 2

x = st.slider('Selct a value for **x**:', 1, 9, 1, on_change=callback)

st.write('Squared: ', st.session_state.squared)
