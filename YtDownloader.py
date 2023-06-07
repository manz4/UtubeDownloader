import os
import tkinter
from pytube import YouTube

#created the windows and names on them

root = tkinter.Tk(className=' BALAK DOWNLOADER')
root.resizable(False,False)
icon = tkinter.PhotoImage(file='icon1.png')
root.iconphoto(False,icon)

def on_leave(buto):
    buto.config(background='darkgreen')


def getlinkmp3():
    try:
        lank = entry1.get()
        def Download(link):
            youtubeObject = YouTube(link)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            try:
                youtubeObject.download(output_path='~/Desktop/Music')
            except:
                print("An error has occurred")
            print(fr"{youtubeObject.title} Download is completed successfully")
        Download(lank)
        os.system(f'start C:/users/{os.getlogin()}/Desktop/~/Desktop')
    except:
        windnot = tkinter.Tk(className='Notification')
        windnot.configure(pady=20, padx=20)
        windnot.resizable(False, False)
        windnot.iconbitmap('favicon.ico')

        def closewindow():
            windnot.destroy()

        acknoledge = tkinter.Label(windnot, text='Type a Valid Link!!', font=('Times New Roman', 20, 'bold'))
        notibutton = tkinter.Button(windnot, text='Ok', command=closewindow, font=('Times New Roman', 20, 'bold'),
                                    bg='red')
        acknoledge.pack()
        notibutton.pack()
        windnot.mainloop()

def getlinkvid():

    try:
        lank = entry1.get()
        def Download(link):
            youtubeObject = YouTube(link)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            try:
                youtubeObject.download(output_path='~/Desktop/Video')
            except:
                print("An error has occurred")
            print(fr"{youtubeObject.title} Download is completed successfully")
        Download(lank)
        os.system(f'start C:/users/{os.getlogin()}/Desktop/~/Desktop')
    except:
        windnot = tkinter.Tk(className='Notification')
        windnot.resizable(False,False)
        windnot.configure(pady=20,padx=20)
        windnot.iconbitmap('favicon.ico')
        def closewindow():
            windnot.destroy()
        acknoledge = tkinter.Label(windnot,text='Type a Valid Link!!',font=('Times New Roman',20,'bold'))
        notibutton = tkinter.Button(windnot,text='Ok',command=closewindow,font=('Times New Roman',20,'bold'),bg='red')
        acknoledge.pack()
        notibutton.pack()
        windnot.mainloop()


#configured window baground color
root.configure(bg='grey',pady=20, padx=20)

#Set the window size
root.geometry('680x300')

text_var = tkinter.StringVar()

#Added a label on top                                                               #Configured the font
yuu = tkinter.Label(root, text="Enter or Paste Link Below",font=("Times New Roman", 20, "bold"),bg='grey')


#yuu.configure()

entry1 = tkinter.Entry(root,textvariable=text_var,font=("Times New Roman", 20, "bold"))
buton1 = tkinter.Button(root,font=("Times New Roman", 20, "bold"),text='Get Video',command=getlinkvid)
buton2 = tkinter.Button(root,font=("Times New Roman", 20, "bold"),text='Get MP3',command=getlinkmp3)

#learn tommorow
buton1.bind('<Leave>', on_leave(buton1))
buton2.bind('<Leave>', on_leave(buton2))
###
yuu.place(relx=0.5,rely=0.1,anchor='center')
entry1.place(relx=0.5,rely=0.4,anchor='center')
buton1.place(relx=0.8,rely=0.8,anchor='center')
buton2.place(relx=0.2,rely=0.8,anchor='center')
root.mainloop()


#

