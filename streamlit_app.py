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
st.write('Count = ', st.session_state.count)

#############################################
# 2.2 Callback functions
st.header('Callback functions')

if 'count_value' not in st.session_state:
    st.session_state.count_value = 0

def increment_counter():
    st.session_state.count_value += 1
   
def decrement_counter():
    st.session_state.count_value -= 1
   
st.button('Increment', on_click=increment_counter)
st.button('Decrement', on_click=decrement_counter)

st.write('Count = ', st.session_state.count_value)
