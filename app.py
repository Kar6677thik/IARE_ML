import os
from groq import Groq
from markupsafe import Markup
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from flask import Flask,render_template,request

load_dotenv()

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        return f"You submitted: {user_input}"
    return render_template("generate.html")

if __name__ == "__main__":
    app.run(debug=True)