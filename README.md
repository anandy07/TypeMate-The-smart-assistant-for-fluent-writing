# TypeMate ✒️

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red.svg)](https://streamlit.io)
[![Keras](https://img.shields.io/badge/Keras-3.0%2B-D00000.svg)](https://keras.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> An AI-powered writing assistant to predict the next word in your sentence, built with LSTMs and Streamlit.

**TypeMate** is an interactive web application that acts as your smart writing companion, providing real-time word suggestions to help you write faster and more fluently.

---

## ✨ Demo

![TypeMate Demo GIF](https://your-link-to-a-demo-gif.com/demo.gif)
*(**Note**: You should record a short GIF of your app working and replace the link above.)*

---

## 🔮 Features

-   **Real-time Word Prediction**: Get instant suggestions as you type.
-   **Multiple Suggestions**: View the top 3 predicted words with their confidence scores.
-   **Interactive UI**: A simple and clean interface built with Streamlit.
-   **Click-to-Append**: Easily add a suggested word to your text with a single click.

---

## 🛠️ Technology Stack

-   **Backend & Model**: Python, TensorFlow, Keras
-   **Frontend**: Streamlit
-   **Data Processing**: NumPy
-   **Core Architecture**: Long Short-Term Memory (LSTM) Neural Network

---

## 🧠 How It Works

The model was trained on the text of "The Adventures of Sherlock Holmes" to learn linguistic patterns.

1.  **Preprocessing**: The text is cleaned, and a tokenizer converts words into integer sequences.
2.  **Sequence Generation**: Input sequences of 3 words are created to predict the 4th word.
3.  **Model Architecture**: The core of the model is an LSTM network, which is excellent for learning from sequential data like text.
    -   `Embedding Layer`: Converts word integers into dense vectors of a fixed size.
    -   `LSTM Layers`: Two LSTM layers process the sequences to capture context.
    -   `Dense Layer`: A final output layer with a softmax activation function predicts the probability for each word in the vocabulary.
4.  **Inference**: The Streamlit app takes the last three words of the user's input, feeds them into the trained model, and displays the words with the highest predicted probabilities.

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python 3.9+ and pip installed on your system.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your_username/TypeMate.git](https://github.com/your_username/TypeMate.git)
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd TypeMate
    ```
3.  **Install the required packages:**
    *(**Note**: You should create a `requirements.txt` file with all the necessary libraries like `tensorflow`, `streamlit`, `numpy`)*.
    ```sh
    pip install -r requirements.txt
    ```

---

## Usage

To run the application, execute the following command in your terminal:

```sh
streamlit run app.py
