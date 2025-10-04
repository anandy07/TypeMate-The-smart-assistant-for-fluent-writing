import streamlit as st
from keras.models import load_model
import numpy as np
import pickle

# Load model
model = load_model('next_words.h5')

# Load tokenizer
with open('token.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Function to predict top N words
def predict_next_words(model, tokenizer, text, top_n=3):
    sequence = tokenizer.texts_to_sequences([text])
    sequence = np.array(sequence)
    preds = model.predict(sequence, verbose=0)[0]  # shape: (vocab_size,)

    top_indices = preds.argsort()[-top_n:][::-1]
    words, confidences = [], []

    for idx in top_indices:
        for word, value in tokenizer.word_index.items():
            if value == idx:
                words.append(word)
                confidences.append(preds[idx])
                break
    confidences_percent = [round(float(c) * 100, 2) for c in confidences]
    return words, confidences_percent

# Streamlit App with logo
st.set_page_config(
    page_title="Next Word Predictor",
    page_icon="📝",  # You can replace this with "logo.png" if you have a local image
    layout="wide"
)

st.title("✨ Interactive Next Word Predictor")
st.write("Type some text and see AI suggest the next words!")

# Options
top_n = st.selectbox("Number of predictions:", options=[1, 2, 3, 4, 5], index=2)

# Session state
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "predicted_words" not in st.session_state:
    st.session_state.predicted_words = []
if "confidences" not in st.session_state:
    st.session_state.confidences = []

# Text area input
st.session_state.user_input = st.text_area(
    "Enter your text:", value=st.session_state.user_input, height=120
)

# Predict button
if st.button("🔮 Predict Next Words"):
    if st.session_state.user_input.strip():
        last_words = " ".join(st.session_state.user_input.split()[-3:])
        st.session_state.predicted_words, st.session_state.confidences = predict_next_words(
            model, tokenizer, last_words, top_n=top_n
        )
    else:
        st.info("Start typing to see predictions...")

# Display predictions in a user-friendly way
if st.session_state.predicted_words:
    st.write("### Predictions:")
    cols = st.columns(len(st.session_state.predicted_words))
    for i, (word, conf) in enumerate(zip(st.session_state.predicted_words, st.session_state.confidences)):
        with cols[i]:
            if st.button(f"{word} ({conf}%)"):
                st.session_state.user_input += " " + word
                st.experimental_rerun()
            st.progress(conf / 100)  # show confidence visually

# Show updated text
st.write("### Your text so far:")
st.markdown(f"📝 {st.session_state.user_input}")
