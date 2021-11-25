from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk,EpsImagePlugin
from urllib.request import urlopen
from tkinter import Tk, Button, Scale, Canvas, Label, StringVar, Entry, \
    Toplevel, messagebox,filedialog
import os
import time
setWidth = 900
setHeight = 900
trace = 0

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
    startShapePress = False

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
        
        calligraphy_image =(Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/calligraphypen.png?raw=true')))
        calligraphy_image_resized = calligraphy_image.resize((30,30), Image.ANTIALIAS)
        calligraphy_new_image= ImageTk.PhotoImage(calligraphy_image_resized)


        color_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/color.png?raw=true')))
        color_image_resized=color_image.resize((30,30), Image.ANTIALIAS)
        color_new_image= ImageTk.PhotoImage(color_image_resized)

        eraser_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/eraser.png?raw=true')))
        eraser_image_resized=eraser_image.resize((30,30), Image.ANTIALIAS)
        eraser_new_image= ImageTk.PhotoImage(eraser_image_resized)

        rectangle_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/rectangle.png?raw=true')))
        rectangle_image_resized=rectangle_image.resize((40,30), Image.ANTIALIAS)
        rectangle_new_image= ImageTk.PhotoImage(rectangle_image_resized)

        oval_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/oval.png?raw=true')))
        oval_image_resized=oval_image.resize((40,30), Image.ANTIALIAS)
        oval_new_image= ImageTk.PhotoImage(oval_image_resized)




        self.hidden_button= Button(self.root,)
        self.hidden_button.grid(row=0, column=0)

        l0 = Label(self.root, width=3, height=4,)
        l0.grid(column=0, row=0)

        
        #lbl_filename_display = Label(self.root)
        #lbl_filename_display.place(x=500,y=0)

        # display file button
        self.btn_open_file = Button(self.root, text="Open File", command=self.openFile)
        self.btn_open_file.place(x=0,y=0)
        # display file button
        self.save_button = Button(self.root, text="Save File", command=self.save_file)
        self.save_button.place(x=65,y=0)

        # exit button
        self.btn_exit = Button(self.root, text="Exit", command=exit)
        self.btn_exit.place(x=125,y=0)
       
        self.pen_button = Button(self.root, text='pen',image=pen_new_image, command=self.use_pen)
        #self.pen_button.grid(row=0, column=0)
        self.pen_button.place(x=0,y=30)

        self.brush_button = Button(self.root, text='brush',image=brush_new_image, command=self.use_brush)
        #self.brush_button.grid(row=0, column=1)
        self.brush_button.place(x=40,y=30)

        self.color_button = Button(self.root, text='color',image=color_new_image, command=self.choose_color)
        #self.color_button.grid(row=0, column=2)
        self.color_button.place(x=80,y=30)

        self.eraser_button = Button(self.root, text='eraser',image=eraser_new_image, command=self.use_eraser)
        #self.eraser_button.grid(row=0, column=3)
        self.eraser_button.place(x=120,y=30)

        self.calligraphy_button =Button(self.root, text='calligraphy',image=calligraphy_new_image,command=self.use_calligraphy)
        self.calligraphy_button.place(x=160,y=30)


        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        #self.choose_size_button.grid(row=0, column=4)
        self.choose_size_button.place(x=195,y=25)

        
        self.enter_width_text=Text(self.root, height=1, width=4)
        self.enter_width_text.place(x=250,y=5)
        self.width_set_button = Button(self.root, text="Set Width", command= lambda: self.setWidth())
        self.width_set_button.place(x=290,y=0)


        self.enter_height_text=Text(self.root, height=1, width=4)
        self.enter_height_text.place(x=360,y=5)
        self.height_set_button = Button(self.root, text="Set Height", command= lambda: self.setHeight())
        self.height_set_button.place(x=400,y=0)


        self.drawShapeRect = Button(self.root, text = "Draw Rectangle" ,image = rectangle_new_image,command = self.setShapeRectangle)
        self.drawShapeRect.place(x=480,y=30)

        self.drawShapeRect = Button(self.root, text = "Draw Oval" ,image = oval_new_image, command = self.setShapeOval)
        self.drawShapeRect.place(x=580,y=30)


        self.c = Canvas(self.root, bg='white', width=setWidth, height=setHeight)
        self.c.grid(row=2, column=0, sticky=N+S+E+W)
        

        #self.c.bind("<MouseWheel>", self.do_zoom)
        #self.c.bind('<ButtonPress-1>', lambda event: self.c.scan_mark(event.x, event.y))
        #self.c.bind("<B1-Motion>", lambda event: self.c.scan_dragto(event.x, event.y, gain=1))

    
        
        self.setup()
        self.root.mainloop()
    
    def setShapeOval(self):
        self.kinds = [self.c.create_oval]
        self.setShapeOption()


    def setShapeRectangle(self):
        self.kinds = [self.c.create_rectangle]
        self.setShapeOption()


    def setShapeOption(self):
        
        if self.startShapePress == True:
            self.startShapePress = False
            self.startShape()
        else:
            self.startShapePress = True
            self.startShape()

    def startShape(self):
        
        self.canvas = self.c
        self.drawn  = None
        
        

        if self.startShapePress == True:
            self.c.bind('<ButtonPress-1>', self.onStart) 
            self.c.bind('<B1-Motion>',     self.onGrow)  
            self.c.bind('<Double-1>',      self.onClear) 
            self.c.bind('<ButtonPress-3>', self.onMove)
        else:
            self.c.unbind('<ButtonPress-1>') 
            self.c.unbind('<B1-Motion>')  
            self.c.unbind('<Double-1>') 
            self.c.unbind('<ButtonPress-3>')
            self.c.bind('<B1-Motion>', self.paint)
            self.c.bind('<ButtonRelease-1>', self.reset)
    
          
        
    def onStart(self, event):
        self.shape = self.kinds[0]
        self.kinds = self.kinds[1:] + self.kinds[:1] 
        self.start = event
        self.drawn = None
    def onGrow(self, event):                         
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y)
        if trace: print (objectId)
        self.drawn = objectId
        

    def onClear(self, event):
        event.widget.delete('all')   

    def onMove(self, event):
        if self.drawn:                               
            if trace: print (self.drawn)
            canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffX, diffY)
            self.start = event



    def setWidth(self):
        widthUpdate = self.enter_width_text.get("1.0","end-1c")
        
        self.c.config(width=widthUpdate)
        
    def setHeight(self):
        heightUpdate = self.enter_height_text.get("1.0","end-1c")
        
        self.c.config(height=heightUpdate)


    # open file method
    # image will not yet display
    def openFile(self):
        global opened_image
        # we can change initialdir to create a prepopulated primart image folder to test with
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("png files", "*.png"), ("jpeg files", "*.jpeg")))
        #self.lbl_filename_display.configure(text="File Opened: " + filename)
        opened_image = ImageTk.PhotoImage(Image.open(filename))
        # need to get the image display to work correctly
        self.c.create_image(0,0,anchor=NW,image=opened_image)
        lbl_image = Label(image=opened_image)
        

    # save file method
    def save_file(self):
        
        EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs9.55.0\bin\gswin64c'
        #self.popup = FilenamePopup(self.root)
        self.save_button["state"] = "disabled"
        #self.root.wait_window(self.popup.top)

        #filepng = self.popup.filename + '.png'
        filepnginitial = filedialog.asksaveasfilename(filetypes=(("png files", "*.png"),("jpeg files", "*.jpeg")))
        filepng= filepnginitial + '.png'
        print (filepng)
        self.filename = filepnginitial
        print (self.filename)

        if not os.path.exists(filepng) or \
                  messagebox.askyesno("File already exists", "Overwrite?"):
            fileps = self.filename + '.eps'
            

            self.c.postscript(file=fileps)
            with  Image.open(fileps) as img:
                img.save(filepng, 'png')
            
            os.remove(fileps)

            self.save_button["state"] = "normal"

            messagebox.showinfo("File Save", "File saved!")
        else:
            messagebox.showwarning("File Save", "File not saved!")

        self.save_button["state"] = "normal"    
    
    
    
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
        self.startShapePress = False
        self.startShape()
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.startShapePress = False
        self.startShape()
        self.activate_button(self.brush_button)
    
    def use_calligraphy(self):
        self.startShapePress = False
        self.startShape()
        self.activate_button(self.calligraphy_button)
    
    def choose_color(self):
        self.startShapePress = False
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.startShapePress = False
        self.startShape()
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        
        if self.active_button == self.brush_button:
         if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width+5, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
         self.old_x = event.x
         self.old_y = event.y
        if self.active_button == self.calligraphy_button:
         if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x+5, event.y+5,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
         self.old_x = event.x
         self.old_y = event.y
        else:
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
