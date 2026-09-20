from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/')
def home():
return "Welcome to janeza API!"
@app.route('/student')
def get_student():
return jsonify({
"student_id": "2026-00123",
"name": "Janeza Ann Arante",
"program": "BSIT",
"year": 3,
"section": "A"
})
@app.route('/hello')
def say_hello():
name = request.args.get('name', 'Student')
return jsonify({
"message": f"Hello, {name}!"
})
if __name__ == '__main__':
app.run(debug=True)
