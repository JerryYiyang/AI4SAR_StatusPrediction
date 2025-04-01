import os
from flask import Flask, request, jsonify
from model.model import predict_status

app = Flask(__name__)

@app.route('/')
def home():
    return "AI4SAR Status Prediction API is running."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        age = float(data.get('age', 0))
        physical_fitness = data.get('physical_fitness', 'na')
        experience = data.get('experience', 'na')
        environment = data.get('environment', 'na')
        total_hours = float(data.get('total_hours', 0))

        result = predict_status(
            age=age,
            physical_fitness=physical_fitness,
            experience=experience,
            environment=environment,
            total_hours=total_hours
        )

        result['status_code'] = 'success'
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'status_code': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)