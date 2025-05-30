from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("house_price_model.pkl")
encoder = joblib.load("label_encoder.pkl")

places = ['Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr', 'Crawfor', 'Edwards', 'Gilbert', 'IDOTRR', 'MeadowV', 'Mitchel', 'NAmes', 'NPkVill', 'NWAmes', 'NoRidge', 'NridgHt', 'OldTown', 'SWISU', 'Sawyer', 'SawyerW', 'Somerst', 'StoneBr', 'Timber', 'Veenker']

@app.route('/', methods=["POST", "GET"])
def test():
    if request.method == "POST":
        bed = request.form.get('bed')
        bath = request.form.get('bath')
        kitchen = request.form.get('kitchen')
        troom = request.form.get('troom')
        tarea = request.form.get('tarea')
        garea = request.form.get('garea')
        neighbor = request.form.get('neighbor')

        try:
            bed = int(bed)
            bath = int(bath)
            kitchen = int(kitchen)
            troom = int(troom)
            tarea = int(tarea)
            garea = int(garea)
        except (ValueError, TypeError):
            return render_template('index.html', prediction="Fill All Numerical Values", places=places)

        if neighbor not in encoder.classes_:
            return render_template('index.html', prediction="Fill Neighborhood Value Correctly", places=places)

        loc_encoder = encoder.transform([neighbor])[0]

        user_input = np.array([[bed, bath, kitchen, troom, tarea, garea, loc_encoder]])

        prediction = model.predict(user_input)[0]

        return render_template('index.html', prediction=f"Predicted Price: $ {round(prediction, 2)} approx.", places=places)

    return render_template('index.html', places=places)

if __name__ == "__main__":
    app.run(debug=True)

