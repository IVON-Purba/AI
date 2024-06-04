from flask import Flask, jsonify, request
import requests
import subprocess

app = Flask(__name__)

@app.route('/receiveRequest', methods=['POST'])
def receive_request():
    file = request.files['file'] 
    file.save('Save Photo path') 

    result = subprocess.run(['python', 'OCR path'], capture_output=True, text=True)
    print(result)
    
    result2 = subprocess.run(['python', 'purba_gpt path'], capture_output=True, text=True)
    print(result2)

    return result2.stdout

if __name__ == '__main__':
    app.run(debug=True)




