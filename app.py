"""
This API mocks the data
"""
import random
import threading
import time
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})

data = {
    'eth0': {
    "packetsPerSec": 0.0,
    "bytesPerSec": 0.0
  },
      "eth1": {
    "packetsPerSec": 0.0,
    "bytesPerSec": 0.0
  },
  "eth2": {
    "packetsPerSec": 0.667,
    "bytesPerSec": 91.667
  }
}

def update_data():
    """
    updated data
    """
    global data
    while True:
        # Update the values of the data object with random values
        data['eth0']["packetsPerSec"] = random.randint(0, 100)
        data['eth1']["packetsPerSec"] = random.randint(0, 100)
        data['eth2']["packetsPerSec"] = random.randint(0, 100)
        data['eth0']["bytesPerSec"] = random.randint(0, 100)
        data['eth1']["bytesPerSec"] = random.randint(0, 100)
        data['eth2']["bytesPerSec"] = random.randint(0, 100)
        time.sleep(30)  # Wait for 1 seconds before updating again

# Start the timer to update the data object
timer = threading.Thread(target=update_data)
timer.start()

@app.route('/api/data', methods=['GET'])
def get_data():
    """
    get data
    """
    # Return the data object as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
