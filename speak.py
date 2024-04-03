import pyttsx3
import threading
import time

class RobotSpeaker:

    def __init__(self,face):
        self.engine = pyttsx3.init("espeak")
        self.engine.setProperty('rate', 150)  # Adjust speaking rate
        self.engine.setProperty('volume', 1)  # Adjust volume
        self.face = face

    def _speak(self, text):
        """Private method to speak the text."""
        self.face.toggle_talking()
        self.engine.say(text)
        self.engine.runAndWait()
        self.face.toggle_talking()
        self.face.draw_mouth(smile=True)

    def speak_async(self, text):
        """Public method to speak text in a separate thread."""
        
        threading.Thread(target=self._speak, args=(text,), daemon=True).start()
        


    def speaking(self):
        count3 = 0
        while True:
            print("Hello World3333333")
            time.sleep(1)
            count3 = count3 + 1
            print(count3)
