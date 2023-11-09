from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load your trained model (adjust the path as necessary)
with open('models/your_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify({'label': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
