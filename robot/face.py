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

        # Bind key events for talking
        self.root.bind("<KeyPress-t>", self.toggle_talking)
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

    def speak(self):
        while True:
            print("I am a robot")
            time.sleep(.1)


