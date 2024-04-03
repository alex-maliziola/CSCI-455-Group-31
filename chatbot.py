import random
import re
import shlex
import speech_recognition as sr

class Parser:
    def __init__(self):
        self.concepts = {}
        self.rules = {}
        self.nested_rules = {}
        self.variables = {}
        self.last_input = "none"
        self.last_u = "none"

    def parse_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        self.parse_lines(lines)

        listening = True

        while listening:
            with sr.Microphone() as source:
                r= sr.Recognizer()
                r.adjust_for_ambient_noise(source)
                r.dyanmic_energythreshhold = 3000
                try:
                    #print("I'm listening.")
                    audio = r.listen(source)
                    #print("Ah, I heard you!")
                    word = r.recognize_google(audio)
                    print(f"You: {word}")
                    if word.lower() == "exit":
                        print("Goodbye!")
                        break
                    print("Bot: " + self.handle_input(word))
                except sr.UnknownValueError:
                    print("I didn't quite catch that.")

    def parse_lines(self, lines):
        for line in lines:
            if line.strip().startswith('#') or not line.strip():
                continue
            if len(line.strip().split(':')) != 3 and not line.strip().startswith('~'):
                print(f'Error. Rule "{line.strip()}" formatted improperly.')
                continue
            if len(line.strip().split(':')) != 2 and line.strip().startswith('~'):
                print(f'Error. Concept "{line.strip()}" formatted improperly.')
                continue
            self.parse_line(line.strip())

    def parse_line(self, line):
        if line.startswith('~'):
            self.parse_concept(line)
        elif line.startswith('u'):
            if line[1].isdigit():
                self.extract_rule(line)
            elif line[1] == ':':
                self.extract_rule(line)

    def parse_concept(self, line):
        concept_name, phrases = self.extract_concept(line)
        self.concepts[concept_name] = phrases

    def extract_concept(self, line):
        parts = line.split(':')
        concept_name = parts[0].strip('~ ')
        phrases = parts[1].strip(" ")
        if phrases.startswith('['):
            phrases = phrases.strip("[]")
            phrases = shlex.split(phrases)
        return concept_name, phrases

    def extract_rule(self, line):
        parts = line.split(':')
        u_key = 0
        if parts[0] == "u":
            most_recent_key = "none"
            #print(f"{parts[1]} is a mainline with {parts[2]}.")
            input_val = parts[1].strip(" () ")
            output = parts[2].strip(" ")
            #if input_val.startswith('~'):
            #    input_val = input_val.strip("~")
            if input_val.startswith('['):
                input_val = input_val.strip("[]")
                input_val = shlex.split(input_val)
                input_val = tuple(input_val)
            #if output.startswith('~'):
            #    output = output.strip("~")
            if output.startswith('['):
                output = output.strip("[]")
                output = shlex.split(output)
            u_key = str(u_key)
            if isinstance(input_val, tuple):
                input_val = str(input_val)
            #input_val = ','.join([input_val, u_key])
            input_val = ','.join([input_val, most_recent_key])
            input_val = input_val.lower()
            #print(f"Writing to main dictionary. {input_val} is the key; its u-index is: {u_key}; it outputs: {output}. Its trigger key is: {most_recent_key}")
            self.rules[input_val] = (u_key, output, most_recent_key)
            self.last_u_key = input_val
        else:
            input_val = parts[1].strip(" () ")
            output = parts[2].strip(" ")
            u_key = int(parts[0].strip("u"))
            #print(f"({input_val}) is in layer ({u_key}), returning ({output}).")

            prev_u_key = u_key - 1
            most_recent_output = None
            most_recent_key = None
            if prev_u_key > 0:
                for key, (key_u, key_output, last_input) in reversed(self.rules.items()):
                    if int(key_u) == int(prev_u_key):
                        most_recent_output = key_output
                        most_recent_key = key
                        #print(f"Setting most recent key to {most_recent_key}, in accordance with {self.rules}")
                        break
            else:
                for key, (key_u, key_output, last_input) in reversed(self.rules.items()):
                    #print(f"Checking if {key_u} matches {prev_u_key}")
                    if int(key_u) == int(prev_u_key):
                        most_recent_output = key_output
                        most_recent_key = key
                        #print(f"Setting most recent key to {most_recent_key}, in accordance with {self.rules}")
                        break

            #if input_val.startswith('~'):
            #    input_val = input_val.strip("~")
            if input_val.startswith('['):
                input_val = input_val.strip("[]")
                input_val = shlex.split(input_val)
                input_val = tuple(input_val)
            #if output.startswith('~'):
            #    output = output.strip("~")
            if output.startswith('['):
                output = output.strip("[]")
                output = shlex.split(output)
            u_key = str(u_key)
            if isinstance(input_val, tuple):
                input_val = str(input_val)
            #input_val = ','.join([input_val, u_key])
            input_val = ','.join([input_val, most_recent_key])
            input_val = input_val.lower()
            #print(f"Writing to dictionary. {input_val} is the key; its u-index is: {u_key}; it outputs: {output}; and its trigger key is: {most_recent_key}.")
            self.rules[input_val] = (u_key, output, most_recent_key)
            self.last_u_key = input_val

    def handle_input(self, user_input):
        error_msg = "Sorry, I didn't understand that."
        user_input = user_input.lower()
        pattern = r'([^,()]+|\([^)]+\))'

        def process_input(input_str):
            for key, value in self.rules.items():
                result = re.findall(pattern, key)
                result = [x.strip() for x in result]
                if input_str == result[0]:
                    if value[2] == self.last_input:
                        self.last_input = key
                        return self.process_response(value[1])
                if result[0].startswith('~'):
                    for concept_key, values_list in self.concepts.items():
                        for value_concept in values_list:
                            if input_str == value_concept and result[0].strip('~') == concept_key:
                                if value[2] == self.last_input:
                                    self.last_input = key
                                    return self.process_response(value[1])
                if result[0].startswith("(") and result[0].endswith(")"):
                    result = result[0].strip(" () ")
                    result = result.replace("'", "")
                    values_list = [value.strip() for value in result.split(',')]
                    for list_value in values_list:
                        if input_str == list_value:
                            if value[2] == self.last_input:
                                self.last_input = key
                                return self.process_response(value[1])
                key_parts = result[0].split('_')
                if len(key_parts) == 2:
                    if key_parts[0] in input_str and key_parts[1] in input_str:
                        if value[2] == self.last_input:
                            splitvals = value[1].split(' ')
                            for splitval in splitvals:
                                if splitval.startswith("$"):
                                    modified_string = input_str.replace(key_parts[0], "").replace(key_parts[1], "")
                                    self.variables[splitval] = modified_string
                            self.last_input = key
                            return self.process_response(value[1])

            return None

        output = process_input(user_input)
        if output is None and self.last_input != "none":
            self.last_input = "none"
            output = process_input(user_input)

        if output is not None:
            return output

        self.last_input = "none"
        return error_msg

    def process_response(self, response):
        if isinstance(response, list):
            return random.choice(response)
        elif isinstance(response, str):
            if response.startswith('~'):
                for key, values_list in self.concepts.items():
                    if response.strip("~") == key:
                        return random.choice(values_list)
            variable_respo = response.split(' ')
            for respo_word in variable_respo:
                if respo_word.startswith("$"):
                    if respo_word in self.variables:
                        response = response.replace(respo_word, self.variables[respo_word])
                        return response
                    else:
                        return "You haven't told me that information yet!"
            return response


if __name__ == "__main__":
    parser = Parser()
    parser.parse_file("dialog_rules.txt")
