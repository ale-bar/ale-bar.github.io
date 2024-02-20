import tkinter as tk
from PIL import Image, ImageTk

class MapInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Map Interface")
        
        # Load the map image
        self.map_image_path = "scripts/cumap.png"
        self.map_image = Image.open(self.map_image_path)
        self.map_image.thumbnail((800, 600))  # Resize the image if needed
        self.tk_image = ImageTk.PhotoImage(self.map_image)

        # Create a canvas to display the map image
        self.canvas = tk.Canvas(self, width=self.map_image.width(), height=self.map_image.height())
        self.canvas.pack()
        
        # Add the map image to the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        
        # Bind events for moving the map
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move)
        
        # Bind events for zooming the map
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        
        self.start_x = None
        self.start_y = None
        
    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_move(self, event):
        if self.start_x and self.start_y:
            x_move = event.x - self.start_x
            y_move = event.y - self.start_y
            self.canvas.move(tk.ALL, x_move, y_move)
            self.start_x = event.x
            self.start_y = event.y

    def on_mousewheel(self, event):
        scale = 1.1 if event.delta > 0 else 0.9
        self.canvas.scale(tk.ALL, event.x, event.y, scale, scale)


MapInterface().mainloop()

