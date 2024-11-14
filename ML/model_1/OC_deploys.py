from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("obesity_prediction_model.h5")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        # Validate input feature length
        input_features = np.array(data['features'])
        if input_features.shape[0] != 16:  # Replace 16 with the correct feature count
            return jsonify({"error": f"Expected 16 features, but received {input_features.shape[0]}"}), 400

        input_features = input_features.reshape(1, -1)
        prediction = model.predict(input_features)
        predicted_class = int(np.argmax(prediction, axis=1)[0])
        return jsonify({"predicted_obesity_level": predicted_class})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500)