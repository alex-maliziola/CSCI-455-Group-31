import time

class RobotSpeaker:

    def __init__(self):
        pass
        ##self.engine = pyttsx3.init()
        ##self.engine.setProperty('rate', 150)  # Adjust speaking rate
        ##self.engine.setProperty('volume', 0.9)  # Adjust volume

    def _speak(self, text):
        """Private method to speak the text."""
        ##self.engine.say(text)
        ##self.engine.runAndWait()

    def speak_async(self, text):
        """Public method to speak text in a separate thread."""
        ##threading.Thread(target=self._speak, args=(text,), daemon=True).start()

    def speaking(self):
        count3 = 0
        while True:
            print("Hello World3333333")
            time.sleep(1)
            count3 = count3 + 1
            print(count3)