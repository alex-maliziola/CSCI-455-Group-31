
import tkinter as tk
import face
import time
import pyttsx3
import tango
import threading
import speak

def loopR():
    count1 = 0
    while True:
        print("Hello World")
        time.sleep(1)
        count1 = count1 + 1
        print(count1)

def loop1():
    count2 = 0
    while True:
        print("Hello World1111111")
        time.sleep(1)
        count2 = count2 + 1
        print(count2)



if __name__ == "__main__":
    root = tk.Tk()
    t = tango.Tango()
    #
    # # Bind the 'a' key to the handle_key_a function
    # root.bind("<KeyPress-Right>", t.head_turn_right)
    #
    # # Bind the 'b' key to the handle_key_b function
    # root.bind("<KeyPress-Left>", t.head_turn_left)
    #t.stabalize()
    #t.project_1()


    app = face.FaceDrawer(root)

    speaker = speak.RobotSpeaker()

    # Create a thread for the speak method
    speak_thread = threading.Thread(target=loopR)
    speak_thread.daemon = True  # This makes the thread exit when the main program exits
    speak_thread.start()

    # Create a thread for the loopR function
    loopR_thread = threading.Thread(target=loop1)
    loopR_thread.daemon = True  # This makes the thread exit when the main program exits
    loopR_thread.start()

    speaking_thread = threading.Thread(target=speaker.speaking)
    speaking_thread.daemon = True  # This makes the thread exit when the main program exits
    speaking_thread.start()
    # Start the main loop
    root.mainloop()


