from tkinter import *
from tkinter.filedialog import askopenfilename

LABEL_01 = 'File Id'
LABEL_02 = 'File type'
LABEL_03 = 'Create time'
LABEL_04 = 'Weather'
LABEL_05 = 'Location'
LABEL_06 = 'Hdfs location path'
LABEL_07 = 'File Extension'
LABEL_08 = 'Total frame'
LABEL_09 = 'Image width'
LABEL_10 = 'Image height'
LABEL_11 = 'Fps'


root = Tk()

#This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")

# Title is the name of application (like title web application)
Title = root.title( "Tool copy file")


theLabel01 = Label(root, text=LABEL_01)
theLabel01.grid(row=0, column = 0)

# entry space 01
entrySpace = Entry(root)
entrySpace.grid(row=0, column=1)
# theLabel01.pack()

theLabel02 = Label(root, text=LABEL_02)
theLabel02.grid(row=1, column = 0)
# entry space 02
entrySpace02 = Entry(root)
entrySpace02.grid(row=1, column=1)


theLabel03 = Label(root, text=LABEL_03)
theLabel03.grid(row=2, column = 0)
# theLabel02.pack()
# entry space 02
entrySpace03 = Entry(root)
entrySpace03.grid(row=2, column=1)

theLabel04 = Label(root, text=LABEL_04)
theLabel04.grid(row=3, column = 0)
# theLabel02.pack()
# entry space 02
entrySpace04 = Entry(root)
entrySpace04.grid(row=3, column=1)

theLabel05 = Label(root, text=LABEL_05)
theLabel05.grid(row=4, column = 0)
# theLabel02.pack()
# entry space 02
entrySpace05 = Entry(root)
entrySpace05.grid(row=4, column=1)

# Space for browse file upload to hdfs
theLabel06 = Label(root, text=LABEL_06)
theLabel06.grid(row=5, column = 0)

buttonBrowse = Button(root, text='Open File', command = OpenFile)
buttonBrowse.grid(row=5, column=1)
# Menu bar


theLabel07 = Label(root, text=LABEL_07)
theLabel07.grid(row=6, column = 0)
# theLabel02.pack()
# entry space 02
entrySpace07 = Entry(root)
entrySpace07.grid(row=6, column=1)

theLabel07 = Label(root, text=LABEL_07)
theLabel07.grid(row=6, column = 0)
# theLabel02.pack()
# entry space 02
entrySpace07 = Entry(root)
entrySpace07.grid(row=6, column=1)

theLabel08 = Label(root, text=LABEL_08)
theLabel08.grid(row=7, column = 0)
# theLabel02.pack()
# entry space 02
entrySpace08 = Entry(root)
entrySpace08.grid(row=7, column=1)

theLabel09 = Label(root, text=LABEL_09)
theLabel09.grid(row=8, column = 0)
# theLabel02.pack()
# entry space 02
entrySpace09 = Entry(root)
entrySpace09.grid(row=8, column=1)


theLabel10 = Label(root, text=LABEL_10)
theLabel10.grid(row=9, column = 0)
# theLabel02.pack()
# entry space 02
entrySpace10 = Entry(root)
entrySpace10.grid(row=9, column=1)

theLabel11 = Label(root, text=LABEL_11)
theLabel11.grid(row=10, column = 0)
# theLabel02.pack()
# entry space 02
entrySpace11 = Entry(root)
entrySpace11.grid(row=10, column=1)

# Business function

def submit():
    print('Submit')
    data = entrySpace02.get()
    print(data)

# Submit button

button = Button(root, text='Submit', command=submit)
button.grid(columnspan = 2)
# Menu bar

menu = Menu(root)
root.config(menu=menu)
# file = Menu(menu)

menu.add_command(label = 'Exit', command = lambda:exit())

# menu.add_cascade(label = 'File', menu = file)




root.mainloop()
