import tkinter as tk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from pymystem3 import Mystem
import nltk

nltk.download('stopwords')

mystem = Mystem()


def split_sentences():
    text = text_input.get("1.0", "end-1c")
    sentences = sent_tokenize(text)

    output_text.delete("1.0", "end")

    for sentence in sentences:
        output_text.insert("end", sentence + "\n")


def tokenize_text():
    text = output_text.get("1.0", "end-1c")
    tokens = word_tokenize(text)

    output_text.delete("1.0", "end")

    for token in tokens:
        output_text.insert("end", token + "\n")


def insert_text():
    text = window.clipboard_get()
    text_input.delete("1.0", "end")
    text_input.insert("end", text)


def pos_tagging():
    text = output_text.get("1.0", "end-1c")
    tokens = word_tokenize(text)
    lemmas = [lemma['analysis'][0]['lex'] for lemma in mystem.analyze(' '.join(tokens)) if lemma.get('analysis')]
    pos_tags = nltk.pos_tag(lemmas)

    output_text.delete("1.0", "end")

    for token, pos in pos_tags:
        output_text.insert("end", f"{token} ({pos})\n")


window = tk.Tk()
window.title("Text Processing")

text_input = tk.Text(window, height=10, width=50)
text_input.pack()

insert_button = tk.Button(window, text="Вставить текст", command=insert_text)
insert_button.pack()

split_button = tk.Button(window, text="Разделить на предложения", command=split_sentences)
split_button.pack()

tokenize_button = tk.Button(window, text="Токенизировать", command=tokenize_text)
tokenize_button.pack()

pos_tag_button = tk.Button(window, text="Определить части речи", command=pos_tagging)
pos_tag_button.pack()

output_text = tk.Text(window, height=10, width=50)
output_text.pack()

window.mainloop()