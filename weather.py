import tkinter as tk
HEIGHT = 500
WIDTH = 600
def test_function(entry):
	print("Test :", entry)
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT,width=WIDTH)
canvas.pack()

bg_image=tk.PhotoImage(file='landscape.png')
bg_image_label = tk.Label(root,image=bg_image)
bg_image_label.place(x=0,y=0,relheight=1,relwidth=1)

frame = tk.Frame(root, bg="#80c1ff", bd=10)
frame.place(relx=0.5,rely=0.1, relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame, font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda:test_function("hello"))
button.place(relx=0.7, relwidth=0.3,relheight=1)


lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5,rely=0.25, relwidth=0.75,relheight=0.6,anchor='n')


label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
