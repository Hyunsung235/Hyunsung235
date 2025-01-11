from tkinter import *
from deep_translator import GoogleTranslator


root = Tk()
root.title("Translator")
root.geometry("600x200+500+100")
root.resizable(False, False)


english_list = ['영어', 'English', 'english', 'en', '영국어']
start = 'en'
target = 'ko'


def on_button_click1():
  entry_text1 = text_input.get() # 단어, 문장
  result.config(text=GoogleTranslator(source=start, target=target).translate(entry_text1))


def on_button_click2():
   global start
   global target


   start, target = target, start


   start_language.config(text="시작 언어 : {}".format('한국어' if start == 'ko' else '영어'))
   target_language.config(text="목표 언어 : {}".format('한국어' if target == 'ko' else '영어'))




result = Label(root, text="")
result.place(x=100, y=65)


start_language = Label(root, text="시작 언어 : {}".format('한국어' if start == 'ko' else '영어'))
start_language.place(x=100, y=100)


target_language = Label(root, text="목표 언어 : {}".format('한국어' if target == 'ko' else '영어'))
target_language.place(x=400, y=100)


input_message = Label(root, text="문장 입력")
input_message.place(x=280, y=10)


text_input = Entry(root, width=60)
text_input.place(x=100, y=30)


translate_button = Button(root, text="번역", command=on_button_click1)
translate_button.place(x=200, y=150)


language_change_button = Button(root, text="변환", command=on_button_click2)
language_change_button.place(x=400, y=150)


root.mainloop()
