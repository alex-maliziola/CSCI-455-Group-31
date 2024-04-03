import tkinter as tk
import random
import time

class FaceDrawer:
    is_talikng = False

    def __init__(self, root):


        self.root = root
        self.root.title("Robot Face Expressions")

        self.root.attributes('-fullscreen', True)

        self.canvas = tk.Canvas(root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.pack()

        self.draw_eyes()
        self.draw_mouth(smile=True)  # Start with a smile

        self.animate_eyes()

        # Talking state and animation control
        self.is_talking = False
        self.talking_state = False

        self.is_sweating = False
        self.sweat_position = 0


        # Bind key events for talking
        self.root.bind("<KeyPress-a>", self.toggle_sweating)
        self.root.bind("<KeyPress-s>", self.stop_talking)

    def draw_eyes(self, pupil_direction="center"):
        # Clear previous eyes
        self.canvas.delete("eyes")

        # Coordinates for the eyes
        x1, y1, x2, y2 = 100, 100, 300, 300

        # Draw eyes outline
        self.canvas.create_oval(x1, y1, x2, y2, tag="eyes", fill="white")
        self.canvas.create_oval(x1 + 300, y1, x2 + 300, y2, tag="eyes", fill="white")

        # Pupil coordinates based on direction
        pupil_offset = 75
        if pupil_direction == "left":
            pupil_x = x1 + 75 - pupil_offset
            pupil_y = 0

        elif pupil_direction == "right":
            pupil_x = x1 + 75 + pupil_offset
            pupil_y = 0

        elif pupil_direction == "down":
            pupil_x = x1 + 75
            pupil_y = 70


        else:  # center
            pupil_x = x1 + 75
            pupil_y = 0


        pupil_size = 20

        # Draw pupils
        self.canvas.create_oval(pupil_x - pupil_size, y1 + 100 - pupil_size + pupil_y, pupil_x + pupil_size,
                                y1 + 100 + pupil_size + pupil_y, tag="eyes", fill="blue")
        self.canvas.create_oval(pupil_x + 300 - pupil_size, y1 + 100 - pupil_size + pupil_y, pupil_x + 300 + pupil_size,
                                y1 + 100 + pupil_size +pupil_y, tag="eyes", fill="blue")

    def draw_mouth(self, smile=False, talking=False):
        # Clear previous mouth
        self.canvas.delete("mouth")

        # Draw mouth based on the state
        if talking:
            # Open mouth for talking
            self.canvas.create_oval(200, 400, 400, 450, tag="mouth", fill="black")
        elif smile:
            # Smiling mouth
            self.canvas.create_arc(200, 350, 400, 450, start=0, extent=-180, tag="mouth", style=tk.ARC)
        else:
            # Neutral mouth
            self.canvas.create_arc(200, 350, 400, 450, start=0, extent=180, tag="mouth", style=tk.ARC)

    def animate_eyes(self):
        # Animate eyes only if not talking
        if not self.is_talikng:
            directions = ["left", "right", "center", "down"]
            next_direction = random.choice(directions)
            self.draw_eyes(pupil_direction=next_direction)

        self.root.after(2000, self.animate_eyes)

    def toggle_talking(self, event=None):
        self.is_talking = not self.is_talking
        if self.is_talking:
            self.animate_talking()

    def stop_talking(self, event=None):
        self.is_talking = False

    def animate_talking(self):
        if self.is_talking:
            self.talking_state = not self.talking_state
            self.draw_mouth(talking=self.talking_state)
            self.root.after(500, self.animate_talking)




    def toggle_sweating(self, event=None):
        self.is_sweating = not self.is_sweating
        if self.is_sweating:
            self.animate_sweat()
        else:
            self.canvas.delete("sweat")
            self.sweat_position = 0  # Stop sweating and clear sweat drops

    def draw_sweat(self):
        self.canvas.delete("sweat")
          # Clear existing sweat
        # Calculate sweat drop positions (you can adjust the starting position and size)
        x, y = 50, 150 + self.sweat_position
        a, b = 650, 50 + self.sweat_position
        c, d = 200, 250 + self.sweat_position
        e, f = 550, 100 + self.sweat_position
        size = 10
        self.canvas.create_oval(x-size, y-size, x+size, y+size, fill="blue", tag="sweat")
        self.canvas.create_oval(a-size, b-size, a+size, b+size, fill="blue", tag="sweat")
        self.canvas.create_oval(c-size, d-size, c+size, d+size, fill="blue", tag="sweat")
        self.canvas.create_oval(e-size, f-size, e+size, f+size, fill="blue", tag="sweat")
        # Add more sweat drops as needed, adjust positions and sizes

    def animate_sweat(self):
        if self.is_sweating:
            self.draw_sweat()
            self.sweat_position += 5  # Move sweat down; adjust speed as needed
            if self.sweat_position > 300:  # Reset position after reaching a certain point
                self.sweat_position = 0
            self.root.after(100, self.animate_sweat)  # Adjust time for animation speed
