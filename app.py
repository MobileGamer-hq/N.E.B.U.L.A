from tkinter import *
import assistant

nebula = assistant

root = Tk()

root.title("N.E.B.U.L.A")
root.geometry("210x310")
root.configure(bg = "midnight blue")

speakText = Label(root,text="S.O.F.I.E", bg = "midnight blue",fg= "white", font= ("Serif",15))

listenButton = Button(root, text = "Listen", font=("Serif", 10), command= nebula.Assistant.start(""), bg="white", fg="midnight blue")
listenButton.place(x = 85, y = 260)

speakText.pack()

root.mainloop()


#mic_btn= PhotoImage(file='Graphics/Logo.png')
#mic_img_label= Label(image=mic_btn)
#listean_button= Button(root, image=mic_btn,command= sofie.listen ,borderwidth=0)
#listean_button.place(x = 90, y = 250)

#listenButton = Button(root, text = "listen", command=sofie.listen)
#speechBox = Entry(root)
#speechBox.place(x = 45, y = 260)
#speakText.pack()
#listenButton.place(x = 85, y = 260)