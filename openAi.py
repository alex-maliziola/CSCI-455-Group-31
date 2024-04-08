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
  response = chatgpt.ask_chatgpt(question,q)

  print(response)




# completion = openai.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

#print(completion.choices[0].message)