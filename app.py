from flask import Flask, request, jsonify

app = Flask(__name__)

# Store a single message globally
STAGED_MESSAGE = {}

@app.route('/')
def index():
    return "Hello World",200

@app.route('/api/health', methods=['GET'])
def health_check():
    return {"status": "ok"}, 200

# POST endpoint to set the message
@app.route('/api/post_data', methods=['POST'])
def post_data():
    data = request.get_json()

    if not data:
        return {"error": "No data provided"}, 400
    
    if not all(k in data for k in ('username', 'message', 'timestamp')):
        return {"error": "Missing required fields"}, 400

    # Overwrite the global message
    STAGED_MESSAGE.clear()
    STAGED_MESSAGE.update(data)

    return {"message": "Message staged successfully"}, 201

# GET endpoint to view the staged message
@app.route('/api/staging', methods=['GET'])
def staging_area():
    if not STAGED_MESSAGE:
        return {"message": "PINGPONG"}, 200
    return jsonify(STAGED_MESSAGE), 200


if  __name__ == '__main__':
    app.run(debug=True)