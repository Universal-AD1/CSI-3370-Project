
from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk
from urllib.request import urlopen


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        
    
        self.root.title("PrimPaint")
        self.root.state('zoomed')

        pen_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/pen.png?raw=true')))
        pen_image_resized=pen_image.resize((30,30), Image.ANTIALIAS)
        pen_new_image= ImageTk.PhotoImage(pen_image_resized) 


        brush_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/brush.png?raw=true')))
        brush_image_resized=brush_image.resize((30,30), Image.ANTIALIAS)
        brush_new_image= ImageTk.PhotoImage(brush_image_resized)


        color_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/color.png?raw=true')))
        color_image_resized=color_image.resize((30,30), Image.ANTIALIAS)
        color_new_image= ImageTk.PhotoImage(color_image_resized)

        eraser_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/eraser.png?raw=true')))
        eraser_image_resized=eraser_image.resize((30,30), Image.ANTIALIAS)
        eraser_new_image= ImageTk.PhotoImage(eraser_image_resized)

        self.hidden_button= Button(self.root,)
        self.hidden_button.grid(row=0, column=0)

        l0 = Label(self.root, width=3, height=3,)
        l0.grid(column=0, row=0)

        self.pen_button = Button(self.root, text='pen',image=pen_new_image, command=self.use_pen)
        #self.pen_button.grid(row=0, column=0)
        self.pen_button.place(x=0,y=0)

        self.brush_button = Button(self.root, text='brush',image=brush_new_image, command=self.use_brush)
        #self.brush_button.grid(row=0, column=1)
        self.brush_button.place(x=40,y=0)

        self.color_button = Button(self.root, text='color',image=color_new_image, command=self.choose_color)
        #self.color_button.grid(row=0, column=2)
        self.color_button.place(x=80,y=0)

        self.eraser_button = Button(self.root, text='eraser',image=eraser_new_image, command=self.use_eraser)
        #self.eraser_button.grid(row=0, column=3)
        self.eraser_button.place(x=120,y=0)
        
        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        #self.choose_size_button.grid(row=0, column=4)
        self.choose_size_button.place(x=175,y=0)

        
        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=2, column=0, sticky=N+S+E+W)


        self.c.bind("<MouseWheel>", self.do_zoom)
        self.c.bind('<ButtonPress-1>', lambda event: self.c.scan_mark(event.x, event.y))
        self.c.bind("<B1-Motion>", lambda event: self.c.scan_dragto(event.x, event.y, gain=1))

    
        
        self.setup()
        self.root.mainloop()

        
    def do_zoom(self,event):
        x = self.c.canvasx(event.x)
        y = self.c.canvasy(event.y)
        factor = 1.001 ** event.delta
        self.c.scale(ALL, x, y, factor, factor)
    

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    

    
    


if __name__ == '__main__':
    Paint()
