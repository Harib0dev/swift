from flask import Flask, request

app = Flask(__name__)

@app.route('/save_scooter', methods=['POST'])
def save_scooter():
    scooter_number = request.json.get('scooter_number')
    if scooter_number:
        with open('scooter_numbers.txt', 'a') as f:
            f.write(f"{scooter_number}\n")
        return {"status": "success", "message": "Scooter number saved!"}, 200
    return {"status": "error", "message": "No scooter number provided!"}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
