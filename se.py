from flask import Flask, request

app = Flask(__name__)

messages = []

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    messages.append(f"{data['sender']}: {data['message']}")
    return {"status": "Message received"}

@app.route('/get', methods=['GET'])
def get_messages():
    return {"messages": messages}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
