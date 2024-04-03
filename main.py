
import tkinter as tk
import face
import time
#import pyttsx3
import tango
import threading
import speak


if __name__ == "__main__":
    root = tk.Tk()
    app = face.FaceDrawer(root)

    t = tango.Tango(app)
    #
    # # Bind the 'a' key to the handle_key_a function
    # root.bind("<KeyPress-Right>", t.head_turn_right)
    #
    # # Bind the 'b' key to the handle_key_b function
    # root.bind("<KeyPress-Left>", t.head_turn_left)
    #t.stabalize()
    #t.project_1()




    speaker = speak.RobotSpeaker(app)
    #root.bind("<KeyPress-a>", t.head_turn_right)


    speaking_thread = threading.Thread(target=speaker.speaking)
    speaking_thread.daemon = True  # This makes the thread exit when the main program exits
    speaking_thread.start()

    speaker.speak_async("Hello, my name is terry, i am a robot")
    # Start the main loop
    root.mainloop()

