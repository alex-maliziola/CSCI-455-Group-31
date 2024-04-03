from flask import Flask, request, jsonify
from maestro import Controller

app = Flask(__name__)

class Tango:
    def __init__(self):
        self.head_loc = 5900
        self.tango = Controller()
        self.tango.setTarget(4, 5900)
        self.tango.setTarget(3, 5900)
        self.tango.setTarget(2, 7900)
        self.tango.setTarget(5, 0)
        self.tango.setTarget(11, 0)
        self.tango.setTarget(0, 0)
        self.tango.setTarget(1, 0)

t = Tango()

# Allow requests from any origin (for testing in a controlled local environment)
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    return response

def map_value(value, in_min, in_max, out_min, out_max):
    in_range = in_max - in_min
    out_range = out_max - out_min
    scaled = float(value-in_min) / float(in_range)

    result = out_min + (scaled * out_range)
    return int(result)

# Define a route to receive control commands
@app.route('/control', methods=['POST', 'OPTIONS'])
def control():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({'message': 'Options received'})
        return add_cors_headers(response), 200

    data = request.json
    control = data['control']
    value = data['value']

    if control == 'head-pan':
        if value =='5':
            t.head_loc = 3900
            t.tango.setTarget(4, t.head_loc)
        elif value == '4':
            t.head_loc = 4300
            t.tango.setTarget(4, t.head_loc)
        elif value == '3':
            t.head_loc = 4700
            t.tango.setTarget(4, t.head_loc)
        elif value == '2':
            t.head_loc = 5100
            t.tango.setTarget(4, t.head_loc)
        elif value == '1':
            t.head_loc = 5500
            t.tango.setTarget(4, t.head_loc)
        elif value == '0':
            t.head_loc = 5900
            t.tango.setTarget(4, t.head_loc)
        elif value == '-1':
            t.head_loc = 6300
            t.tango.setTarget(4, t.head_loc)
        elif value == '-2':
            t.head_loc = 6700
            t.tango.setTarget(4, t.head_loc)
        elif value == '-3':
            t.head_loc = 7100
            t.tango.setTarget(4, t.head_loc)
        elif value == '-4':
            t.head_loc = 7500
            t.tango.setTarget(4, t.head_loc)
        elif value == '-5':
            t.head_loc = 7900
            t.tango.setTarget(4, t.head_loc)

    elif control == 'head-tilt':
        if value =='-5':
            t.head_loc = 3900
            t.tango.setTarget(3, t.head_loc)
        elif value == '-4':
            t.head_loc = 4300
            t.tango.setTarget(3, t.head_loc)
        elif value == '-3':
            t.head_loc = 4700
            t.tango.setTarget(3, t.head_loc)
        elif value == '-2':
            t.head_loc = 5100
            t.tango.setTarget(3, t.head_loc)
        elif value == '-1':
            t.head_loc = 5500
            t.tango.setTarget(3, t.head_loc)
        elif value == '0':
            t.head_loc = 5900
            t.tango.setTarget(3, t.head_loc)
        elif value == '1':
            t.head_loc = 6300
            t.tango.setTarget(3, t.head_loc)
        elif value == '2':
            t.head_loc = 6700
            t.tango.setTarget(3, t.head_loc)
        elif value == '3':
            t.head_loc = 7100
            t.tango.setTarget(3, t.head_loc)
        elif value == '4':
            t.head_loc = 7500
            t.tango.setTarget(3, t.head_loc)
        elif value == '5':
            t.head_loc = 7900
            t.tango.setTarget(3, t.head_loc)

    elif control == 'waist-pan':
        if value =='5':
            t.head_loc = 3900
            t.tango.setTarget(2, t.head_loc)
        elif value == '4':
            t.head_loc = 4300
            t.tango.setTarget(2, t.head_loc)
        elif value == '3':
            t.head_loc = 4700
            t.tango.setTarget(2, t.head_loc)
        elif value == '2':
            t.head_loc = 5100
            t.tango.setTarget(2, t.head_loc)
        elif value == '1':
            t.head_loc = 5500
            t.tango.setTarget(2, t.head_loc)
        elif value == '0':
            t.head_loc = 5900
            t.tango.setTarget(2, t.head_loc)
        elif value == '-1':
            t.head_loc = 6300
            t.tango.setTarget(2, t.head_loc)
        elif value == '-2':
            t.head_loc = 6700
            t.tango.setTarget(2, t.head_loc)
        elif value == '-3':
            t.head_loc = 7100
            t.tango.setTarget(2, t.head_loc)
        elif value == '-4':
            t.head_loc = 7500
            t.tango.setTarget(2, t.head_loc)
        elif value == '-5':
            t.head_loc = 7900
            t.tango.setTarget(2, t.head_loc)

    elif control == 'Joystick':
        print("BRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
        x, y = value.split(',')
        x = float(x)
        y = float(y)
        mapped_x = map_value(x, 25, 175, 7900, 3900)
        mapped_y = map_value(y, 25, 175, 3900, 7900)
        print(mapped_x)
        print(mapped_y)
        t.tango.setTarget(1, mapped_x)
        t.tango.setTarget(0, mapped_y)

    # Print the received control and value
    print("Control:", control)
    print("Value:", value)

    # Respond with a message
    response = jsonify({'message': 'Control received'})
    return add_cors_headers(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
