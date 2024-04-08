import speak
if __name__ == "__main__":
  q = ""
  key =""
  chatgpt = ChatGPTPersonality(key)
  i = input("Who would you like to speak to?\n"
        "1 for poet\n"
        "2 for sarcastic person\n"
        "3 for professor\n"
        "4 for scifi guy\n"
        "5 for drama queen\n"
        "6 for conspiricy theorist \n"
        "7 for wise elder\n")

  if i == 1:q = "poetic"
  elif i == 2:q = "sarcastic"
  elif i == 3:q = "professor"
  elif i == 4:q = "scifi"
  elif i == 5:q = "drama_queen"
  elif i == 6:q = "conspiricy_theorist"
  else: q = "wise_elder"

  personalities = {
    "poetic": "poet",
    "sarcastic": "sarcastic person",
    "professor": "professor",
    "scifi": "scifi guy",
    "drama_queen": "drama queen",
    "conspiricy_theorist": "conspiricy theorist",
    "wise_elder": "wise elder",
    # Add more personalities to this dictionary
  }
  print("Please enter your question for " , personalities[q])
  question = input()
  response = chatgpt.ask_chatgpt(question,q).content

  print(response)

speak = speak.RobotSpeaker()
speak._speak(response)
