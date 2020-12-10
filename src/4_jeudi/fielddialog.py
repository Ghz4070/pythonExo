from tkinter.filedialog import *

filepath = askopenfilename(title="Ouvrir une image", filetypes=[('png files', '.png'), ('all files', '.*')])
photo = PhotoImage(file=filepath)
canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="yellow")
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()
