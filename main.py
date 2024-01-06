from tkinter import *
from tkinter import filedialog
from gtts import gTTS
from PyPDF2 import PdfReader
# from playsound import playsound

def load_file():
    filepath = filedialog.askopenfilename()
    with open(filepath,'rb') as file:
        pdf = PdfReader(file)
        text = ''
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            text += page.extract_text()
        speech = gTTS(text=text)
        speech.save('audiobook.mp3')
        # playsound('audiobook.mp3')


def main():
    window = Tk()
    window.geometry('600x600')
    window.config(background='black')
    window.title('PDF to SOUND')
    button = Button(text = "Open File" ,command = load_file)
    button.pack()
    # Text_to_speech(load_file())
    window.mainloop()
if __name__=='__main__':
    main()
