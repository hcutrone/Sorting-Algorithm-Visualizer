import tkinter as tk

window = tk.Tk()

c = tk.Canvas()

a = c.create_rectangle(5, 5, 50, 50, fill = "red")
b = c.create_rectangle(5, 50, 50, 100, fill = "blue")
rectangles = [a, b]

x0, y0, x1, y1 = c.coords(a)   						    					## Get coords of first rectangle
x2, y2, x3, y3 = c.coords(b)					     						## Get coords of second rectangle
c.coords(a, x2, y2, x3, y3)  												## Set coords of first rectangle to that of the second
c.coords(b, x0, y0, x1, y1)

#c.delete(rectangles[0])

c.pack()
window.mainloop()
