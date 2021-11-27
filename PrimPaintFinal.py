#PrimPaint
#CSI 3370
#Team 1

#Python Dependencies
from tkinter import *
import tkinter as tkinter
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk,EpsImagePlugin
from urllib.request import urlopen
from tkinter import Tk, Button, Scale, Canvas, Label, StringVar, Entry, \
    Toplevel, messagebox,filedialog
import os
import time
#Default Canvas Height and WIdth
setWidth = 900
setHeight = 900
#variable used in Shape drawing
trace = 0

#Horizontal Ruler above canvas
class HRuler(Canvas):
    '''Horizontal Ruler'''

    def __init__(self, master, width, height, offset=0):
        super().__init__(master, width=width, height=height)
        self.offset = offset

        step = 10

        #Draws lines and enters text at each "step"
        for x in range(step, width, step):
            if x % 50 == 0:
                # draw longer line with text
                self.create_line(x, 20, x, 13, width=2)
                self.create_text(x, 25, text=str(x))
            else:
                self.create_line((x, 2), (x, 7))

#Vertical Ruler on the left side of canvas
class VRuler(Canvas):
    '''Vertical Ruler'''

    def __init__(self, master, width, height, offset=0):
        super().__init__(master, width=width, height=height)
        self.offset = offset

        step = 10

        #Draws lines and enters text at each "step"
        for y in range(step, height, step):
            if y % 50 == 0:
                # draw longer line with text
                self.create_line(0, y, 13, y, width=2)
                self.create_text(20, y, text=str(y), angle=90)
            else:
                self.create_line(2, y, 7, y)





#Main Canvas and Gui
class Paint(object):
    #Set defualt Values for pen and shape creation status
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
    startShapePress = False
    startText = False

    #Method for canvas creation and GUI
    def __init__(self):
        self.root = Tk()
        
        #self.root.configure(bg='darkgray')
        self.root.title("PrimPaint")
        self.root.state('zoomed')
        #Importing and resizing image for button
        pen_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/pen.png?raw=true')))
        pen_image_resized=pen_image.resize((30,30), Image.ANTIALIAS)
        pen_new_image= ImageTk.PhotoImage(pen_image_resized) 

        #Importing and resizing image for button
        brush_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/brush.png?raw=true')))
        brush_image_resized=brush_image.resize((30,30), Image.ANTIALIAS)
        brush_new_image= ImageTk.PhotoImage(brush_image_resized)
        
        #Importing and resizing image for button   
        calligraphy_image =(Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/calligraphypen.png?raw=true')))
        calligraphy_image_resized = calligraphy_image.resize((30,30), Image.ANTIALIAS)
        calligraphy_new_image= ImageTk.PhotoImage(calligraphy_image_resized)

        #Importing and resizing image for button
        color_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/color.png?raw=true')))
        color_image_resized=color_image.resize((30,30), Image.ANTIALIAS)
        color_new_image= ImageTk.PhotoImage(color_image_resized)
        
        #Importing and resizing image for button
        eraser_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/eraser.png?raw=true')))
        eraser_image_resized=eraser_image.resize((30,30), Image.ANTIALIAS)
        eraser_new_image= ImageTk.PhotoImage(eraser_image_resized)
        
        #Importing and resizing image for button
        rectangle_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/rectangle.png?raw=true')))
        rectangle_image_resized=rectangle_image.resize((40,30), Image.ANTIALIAS)
        rectangle_new_image= ImageTk.PhotoImage(rectangle_image_resized)
        
        #Importing and resizing image for button
        oval_image= (Image.open(urlopen('https://github.com/Universal-AD1/CSI-3370-Project/blob/main/images/oval.png?raw=true')))
        oval_image_resized=oval_image.resize((40,30), Image.ANTIALIAS)
        oval_new_image= ImageTk.PhotoImage(oval_image_resized)


        # Define and display Open File button
        self.btn_open_file = Button(self.root, text="Open File", command=self.openFile)
        self.btn_open_file.place(x=0,y=0)
        
        # Define and display Save File button
        self.save_button = Button(self.root, text="Save File", command=self.save_file)
        self.save_button.place(x=65,y=0)

        # Define and display clear canvas button
        self.btn_clear = Button(self.root, text="Clear", command=self.clearCanvas)
        self.btn_clear.place(x=125,y=0)

        # Define and display Pen button
        self.pen_button = Button(self.root, text='pen',image=pen_new_image, command=self.use_pen)
        self.pen_button.place(x=0,y=30)
        
        # Define and display brush button
        self.brush_button = Button(self.root, text='brush',image=brush_new_image, command=self.use_brush)
        self.brush_button.place(x=40,y=30)
        
        # Define and display color selection button
        self.color_button = Button(self.root, text='color',image=color_new_image, command=self.choose_color)
        self.color_button.place(x=80,y=30)
        
        # Define and display eraser button
        self.eraser_button = Button(self.root, text='eraser',image=eraser_new_image, command=self.use_eraser)
        self.eraser_button.place(x=120,y=30)
        
        # Define and display calligraphy button
        self.calligraphy_button =Button(self.root, text='calligraphy',image=calligraphy_new_image,command=self.use_calligraphy)
        self.calligraphy_button.place(x=160,y=30)

        # Define and display Pen size button
        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.place(x=195,y=25)

        # Define and display Canvas Width change button and text input
        self.enter_width_text=Text(self.root, height=1, width=4)
        self.enter_width_text.place(x=250,y=5)
        self.width_set_button = Button(self.root, text="Set Width", command= lambda: self.setWidth())
        self.width_set_button.place(x=290,y=0)

        # Define and display Canvas Width change button and text input
        self.enter_height_text=Text(self.root, height=1, width=4)
        self.enter_height_text.place(x=360,y=5)
        self.height_set_button = Button(self.root, text="Set Height", command= lambda: self.setHeight())
        self.height_set_button.place(x=400,y=0)

        # Define and display rectangle drawing button
        self.drawShapeRect = Button(self.root, text = "Draw Rectangle" ,image = rectangle_new_image,command = self.setShapeRectangle)
        self.drawShapeRect.place(x=300,y=30)

        # Define and display oval drawing button
        self.drawShapeOval = Button(self.root, text = "Draw Oval" ,image = oval_new_image, command = self.setShapeOval)
        self.drawShapeOval.place(x=350,y=30)

        #Button to add textboxes
        self.textbtn = Button(self.root, text='Insert Text Box', command=self.setText) 
        self.textbtn.place(x=400,y=30)

        #Button to change background fill color
        self.backRndBtn = Button(self.root, text='Change Background Color', command=self.setBackColor) 
        self.backRndBtn.place(x=500,y=30)

        #Place Horizontal and Vertical Ruller
        hr = HRuler(self.root, setWidth, setHeight)#, offset=25)
        hr.place(x=28, y=65)
        vr = VRuler(self.root, setWidth, setHeight)#, offset=25)
        vr.place(x=0, y=95)
        #Create Canvas and place into application
        self.c = Canvas(self.root, bg='white', width=setWidth, height=setHeight)
        self.c.place(x=30, y=95)
       
        #Bind Mouse Wheel to zoom
        self.c.bind("<MouseWheel>", self.do_zoom)
        
        self.setup()
        self.root.mainloop()
    
    #Set drawing shape to Oval
    def setShapeOval(self):
        self.kinds = [self.c.create_oval]
        self.setShapeOption()
        self.activate_button(self.drawShapeOval)

    #Set drawing shape to Rectabgle
    def setShapeRectangle(self):
        self.kinds = [self.c.create_rectangle]
        self.setShapeOption()
        self.activate_button(self.drawShapeRect)

    #Set shape drawing toggle True or False
    def setShapeOption(self):
        
        if self.startShapePress == True:
            self.startShapePress = False
            self.startShape()
        else:
            self.startShapePress = True
            self.startShape()

    #Rebind mouse buttons to create shapes 
    def startShape(self):
        
        self.canvas = self.c
        self.drawn  = None
        
        

        if self.startShapePress == True:
            self.c.bind('<ButtonPress-1>', self.onStart) 
            self.c.bind('<B1-Motion>',     self.onGrow)   
            self.c.bind('<ButtonPress-3>', self.onMove)
        else:
            self.c.unbind('<ButtonPress-1>') 
            self.c.unbind('<B1-Motion>')  
            self.c.unbind('<Double-1>') 
            self.c.unbind('<ButtonPress-3>')
            self.c.bind('<B1-Motion>', self.paint)
            self.c.bind('<ButtonRelease-1>', self.reset)
    
          
    #Method used to begin drawing shape    
    def onStart(self, event):
        self.shape = self.kinds[0]
        self.kinds = self.kinds[1:] + self.kinds[:1] 
        self.start = event
        self.drawn = None
    #Method used to diplay shape as mouse moves    
    def onGrow(self, event):                         
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y)
        if trace: print (objectId)
        self.drawn = objectId  

    def onMove(self, event):
        if self.drawn:                               
            if trace: print (self.drawn)
            canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffX, diffY)
            self.start = event
    
    #Checks whether textbox button is active
    def setText(self):
        
        if self.startText == True:
            self.startText = False
            self.textPlace()
        else:
            self.startText = True
            self.textPlace()

    #if Textbox is selected rebinds mouse button to add textbox
    def textPlace(self):
        if self.startText == True:
            self.c.bind('<ButtonPress-1>', self.textBoxPlace) 
            self.c.unbind('<B1-Motion>')

        else:
            self.c.unbind('<ButtonPress-1>') 
            self.c.bind('<B1-Motion>', self.paint)
            self.c.bind('<ButtonRelease-1>', self.reset)
    
    #places text box where mouse 1 is clicked
    def textBoxPlace(self,event):
        self.entry = Entry(self.root,bd=1,font=("Purisa",15)) #can set to whatever font needed
        self.entry.place(x= event.x, y= event.y) #position of mouse click
        self.startText =  False
        self.textPlace()
        self.entry.focus_force()        


    #Method used to clear canvas using button
    def clearCanvas(self):
        self.c.delete("all")
        self.c.configure(bg = 'white')
        #self.entry.destroy()
        self.entry.place_forget()
        
    
    #Method used to change the background color
    def setBackColor(self):
        self.c.configure(bg = askcolor(color=self.color)[1])
        

    #Sets the Width of canvas to user input value
    def setWidth(self):
        widthUpdate = self.enter_width_text.get("1.0","end-1c")
        
        self.c.config(width=widthUpdate)

    #sets canvas height to user input value    
    def setHeight(self):
        heightUpdate = self.enter_height_text.get("1.0","end-1c")
        
        self.c.config(height=heightUpdate)


    # open file method
    def openFile(self):
        global opened_image
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("png files", "*.png"), ("jpeg files", "*.jpeg")))
        opened_image = ImageTk.PhotoImage(Image.open(filename))
        self.c.create_image(0,0,anchor=NW,image=opened_image, sticky=NSEW)
        lbl_image = Label(image=opened_image)
        

    # save file method
    def save_file(self):
        rectBack = self.c.create_rectangle(0, 0, self.c.winfo_reqheight(), self.c.winfo_reqwidth(), fill = self.c["background"])
        self.c.tag_lower(rectBack)

        EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs9.55.0\bin\gswin64c'
        #self.popup = FilenamePopup(self.root)
        self.save_button["state"] = "disabled"
        #self.root.wait_window(self.popup.top)

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
    
    
    #Method which controls zooming function using mouse wheel
    def do_zoom(self,event):
        x = self.c.canvasx(event.x)
        y = self.c.canvasy(event.y)
        factor = 1.001 ** event.delta
        self.c.scale(ALL, x, y, factor, factor)
    
    #Initial initialization of drawing fucntions
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.backColor = None
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    #Method which defines function of pen tool
    def use_pen(self):
        self.startShapePress = False
        self.startShape()
        self.activate_button(self.pen_button)

    #Method which defines function of Brush tool
    def use_brush(self):
        self.startShapePress = False
        self.startShape()
        self.activate_button(self.brush_button)
    
    #Method which defines function of calligraphy tool
    def use_calligraphy(self):
        self.startShapePress = False
        self.startShape()
        self.activate_button(self.calligraphy_button)
    
    #Method which defines function of color selection button
    def choose_color(self):
        self.startShapePress = False
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    #Method which defines function of eraser tool
    def use_eraser(self):
        self.startShapePress = False
        self.startShape()
        self.activate_button(self.eraser_button, eraser_mode=True)

    #Checks currently active button and visually changes the display of the buttons
    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    #Checks the type of brush/pen selected in order to allow for different drawing patterns
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