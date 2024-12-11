from tkinter import Tk, Label, Entry, Button
import json
import string
import random
import nltk
from nltk.stem import WordNetLemmatizer 
# ... rest of your code (including imports and functions)

# Load data (assuming dataSET.json is in the same directory)
with open('dataSET.json') as json_file:
    data = json.load(json_file)

# Initialize chatbot
lm = WordNetLemmatizer()
ourClasses = sorted(set([intent["tag"] for intent in data["ourIntents"]]))
newWords = sorted(set())  # Update with your preprocessed words

def send_message(message_entry, chat_history):
  """Sends a message from the user and displays the chatbot response"""
  new_message = message_entry.get()
  message_entry.delete(0, 'end')  # Clear the message entry
  chat_history.config(text=chat_history.cget("text") + f"You: {new_message}\n")

  # Process the message and get chatbot response
  intents = Pclass(new_message, newWords, ourClasses)
  response = getRes(intents, data)

  chat_history.config(text=chat_history.cget("text") + f"Chatbot: {response}\n")

# Create the main window
root = Tk()
root.title("Chatbot")
root.geometry("400x400")

# Create chat history label
chat_history = Label(root, text="", font=("Arial", 12))
chat_history.pack(fill="both", expand=True)

# Create message entry field
message_entry = Entry(root, width=50)
message_entry.pack(fill="x")

# Create send button
send_button = Button(root, text="Send", command=lambda: send_message(message_entry, chat_history))
send_button.pack()

root.mainloop()