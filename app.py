import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Load model
model = joblib.load('insurance_cost_model.pkl')

# Region mapping
region_map = {'southwest': 1, 'southeast': 2, 'northwest': 3, 'northeast': 4}

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # ✅ Validate required keys and collect missing ones
    required_keys = ["age", "sex", "bmi", "children", "smoker", "region"]
    missing_keys = [key for key in required_keys if key not in data]
    
    if missing_keys:
        return jsonify({"error": f"Missing keys: {', '.join(missing_keys)}"}), 400

    try:
        # Extract and convert data
        age = float(data['age'])
        sex = 1 if data['sex'].lower() == 'male' else 0
        bmi = float(data['bmi'])
        children = int(data['children'])
        smoker = 1 if data['smoker'].lower() == 'yes' else 0
        region = region_map.get(data['region'].lower())

        if region is None:
            return jsonify({"error": f"Invalid region: {data['region']}"}), 400

        # Create DataFrame for prediction
        input_df = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                                columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

        prediction = model.predict(input_df)[0]

        return jsonify({"predicted_cost": round(prediction, 2)})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
