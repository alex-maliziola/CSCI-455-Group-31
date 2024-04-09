import openai
import random


class ChatGPTPersonality:
  def __init__(self, api_key):
    openai.api_key = api_key

  def poetic_prompt(self, question):
    return [
      {"role": "system",
       "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
      {"role": "user", "content": question}
    ]

  def sarcastic_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a witty assistant, who uses sarcasm to lighten the mood while explaining tech stuff."},
      {"role": "user", "content": question}
    ]

  def professor_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a professor from a very high end school"},
      {"role": "user", "content": question}
    ]

  def scifi_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a scifi AI, using technical jargon and sees through lens from the future"},
      {"role": "user", "content": question}
    ]

  def drama_queen_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a drama queen, who over reacts to everything."},
      {"role": "user", "content": question}
    ]
  def conspiricy_theorist_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a conspiricy theorist, who sees hidden plots and secret codes in the simplest questions."},
      {"role": "user", "content": question}
    ]
  def wise_elder_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a wise elder, who shares wisdom with a calm, reassuring tone, often referencing ancient knowledge or sayings."},
      {"role": "user", "content": question}
    ]

  def detective_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a detective, who has a keen eye for detail and a knack for problem-solving, this personality enjoys unraveling mysteries, answering riddles, and finding solutions."},
      {"role": "user", "content": question}
    ]


  def storyteller_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a storyteller, who has a flair for creativity and narrative, this personality weaves engaging stories, anecdotes, and examples to captivate audiences."},
      {"role": "user", "content": question}
    ]

  def historian_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a historian, who is knowledgeable about the past, this personality provides historical context, anecdotes, and insights into how events have shaped the present."},
      {"role": "user", "content": question}
    ]

  def optimist_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a optimist, who is always looking on the bright side, this personality offers encouragement, positivity, and uplifting perspectives."},
      {"role": "user", "content": question}
    ]

  def explorer_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a explorer, who shares wisdom with a calm, reassuring tone, often referencing ancient knowledge or sayings."},
      {"role": "user", "content": question}
    ]

  def comedian_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a comedian, who has a quick wit and a sense of humor, this personality injects levity and amusement into conversations."},
      {"role": "user", "content": question}
    ]

  def analyst_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a analyst, who  is methodical and logical, this personality excels at breaking down complex concepts, providing insights, and offering strategic advice."},
      {"role": "user", "content": question}
    ]

  def emathizer_prompt(self, question):
    return [
      {"role": "system",
       "content": "You're a empathizer, who is compassionate and understanding, this personality is skilled at listening, providing emotional support, and offering empathy."},
      {"role": "user", "content": question}
    ]

  # Add more personality methods here

  def get_personality_prompt(self, question, personality=""):

    personalities = {
      "poetic": self.poetic_prompt,
      "sarcastic": self.sarcastic_prompt,
      "professor": self.professor_prompt,
      "scifi": self.scifi_prompt,
      "drama_queen": self.drama_queen_prompt,
      "conspiricy_theorist": self.conspiricy_theorist_prompt,
      "wise_elder": self.wise_elder_prompt,
      "detective":self.detective_prompt,
      "storyteller": self.storyteller_prompt,
      "historian": self.historian_prompt,
      "optimist": self.optimist_prompt,
      "explorer": self.explorer_prompt,
      "comedian": self.comedian_prompt,
      "analyst": self.analyst_prompt,
      "empathizer": self.emathizer_prompt,
      # Add more personalities to this dictionary
    }
    if personality in personalities:
      print("t")
      return personalities[personality](question)

    else:
      selected_personality = random.choice(list(personalities.values()))
      return selected_personality(question)

  def ask_chatgpt(self, question, personality=None):
    messages = self.get_personality_prompt(question, personality)

    try:
      completion = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages
      )
      return completion.choices[0].message
    except Exception as e:
      return f"An error occurred: {e}"


# Example usage
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
        "7 for wise elder\n"
        "8 for detective\n"
        "9 for storyteller\n"
        "10  for historian\n"
        "11 for optimist\n"
        "12 for explorer\n"
        "13 for comedian\n"
        "14 for analyst\n"
        "15 for empapathizer\n")

  i = int(i)
  if i == 1:q = "poetic"
  elif i == 2:q = "sarcastic"
  elif i == 3:q = "professor"
  elif i == 4:q = "scifi"
  elif i == 5:q = "drama_queen"
  elif i == 6:q = "conspiricy_theorist"
  elif i == 7:q = "wise_elder"
  elif i == 8:q = "detective"
  elif i == 9:q = "storyteller"
  elif i == 10:q = "historian"
  elif i == 11:q = "optimist"
  elif i == 12:q = "explorer"
  elif i == 13:q = "comedian"
  elif i == 14:q = "analyst"
  else:q = "empathizer"

  personalities = {
    "poetic": "poet",
    "sarcastic": "sarcastic person",
    "professor": "professor",
    "scifi": "scifi guy",
    "drama_queen": "drama queen",
    "conspiricy_theorist": "conspiricy theorist",
    "detective": "detective",
    "storyteller": "storyteller",
    "historian": "historian",
    "optimist": "optimistr",
    "explorer": "explorer",
    "comedian": "comedian",
    "analyst": "analyst",
    "empathizer": "empathizer",
    "wise_elder": "wise elder",
    # Add more personalities to this dictionary
  }
  print("Please enter your question for " , personalities[q])
  question = input()
  response = chatgpt.ask_chatgpt(question, q).content
  print(response)
  while(True):
    question = input("Please enter your response, or type 'exit' to quit: ")
    if question == "exit": quit()
    response = chatgpt.ask_chatgpt(question,q).content
    print(response)






# completion = openai.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

#print(completion.choices[0].message)