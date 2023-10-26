from tkinter import Tk, Label, Entry, Button, Text
import pyperclip

def paste_text():
    text_entry.insert("insert", pyperclip.paste())
# Функция для генерации словосочетаний
def generate_phrases():
    noun = noun_entry.get()
    sentences = text_entry.get("1.0", "end-1c").split("\n")

    # Генерация словосочетаний
    direct_phrases = []
    metaphorical_phrases = []
    for sentence in sentences:
        if noun in sentence:
            words = sentence.split()
            for i in range(len(words) - 1):
                if words[i] == noun:
                    direct_phrase = words[i] + " " + words[i+1]
                    direct_phrases.append(direct_phrase)
                elif words[i+1] == noun:
                    metaphorical_phrase = words[i] + " " + words[i+1]
                    metaphorical_phrases.append(metaphorical_phrase)

    # Вывод словосочетаний
    direct_text.delete("1.0", "end")
    for phrase in direct_phrases:
        direct_text.insert("end", phrase + "\n")

    metaphorical_text.delete("1.0", "end")
    for phrase in metaphorical_phrases:
        metaphorical_text.insert("end", phrase + "\n")

    # Обновление значения количества символов
    count_characters()

# Функция для подсчета количества символов
def count_characters():
    text = text_entry.get("1.0", "end-1c")
    characters_with_spaces = len(text)
    characters_without_spaces = len(text.replace(" ", ""))
    character_count.config(text=f"Символов с пробелом: {characters_with_spaces}\nСимволов без пробела: {characters_without_spaces}")

# Создание графического интерфейса
window = Tk()
window.title("Генератор словосочетаний")

# Метка и поле для ввода текста
text_label = Label(window, text="Введите текст:")
text_label.pack()
text_entry = Text(window, height=10, width=50)
text_entry.pack()

# Метка и поле для ввода существительного
noun_label = Label(window, text="Введите существительное:")
noun_label.pack()
noun_entry = Entry(window)
noun_entry.pack()



# Кнопка для генерации словосочетаний
generate_button = Button(window, text="Сгенерировать", command=generate_phrases)
generate_button.pack()

paste_button = Button(window, text="Вставить", command=paste_text)
paste_button.pack()

# Окна для вывода словосочетаний
direct_label = Label(window, text="Существительное в прямом значении + прилагательное:")
direct_label.pack()
direct_text = Text(window, height=5, width=50)
direct_text.pack()

metaphorical_label = Label(window, text="Существительное в переносном значении + прилагательное:")
metaphorical_label.pack()
metaphorical_text = Text(window, height=5, width=50)
metaphorical_text.pack()

# Поле для количества символов
character_count_label = Label(window, text="Количество символов:")
character_count_label.pack()
character_count = Label(window, text="")
character_count.pack()


# Запуск приложения
window.mainloop()