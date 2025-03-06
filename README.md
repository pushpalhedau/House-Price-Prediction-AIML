House Price Prediction - Flask Web Application
Project Overview
This project is a Flask-based web application that predicts house prices based on user-input features using a Random Forest Regressor machine learning model. The model is trained on a housing dataset and considers various parameters such as the number of bedrooms, bathrooms, square footage, and location to provide an estimated price.

Project Structure
php
Copy
Edit
House-Price-Prediction
│── app.py                   # Flask application to handle requests and responses
│── train_model.py           # Script to train the ML model
│── house_price_model.pkl    # Saved ML model for predictions
│── label_encoder.pkl        # Label encoder for location data
│── requirements.txt         # Required Python packages
│
├── dataset
│   ├── train.csv            # Dataset used to train the model
│
├── templates
│   ├── index.html           # HTML form for user input
│
├── static
│   ├── styles.css           # CSS file for frontend styling
How the Project Works
1. Model Training (train_model.py)
Loads train.csv from the dataset folder.
Uses a Random Forest Regressor to train the model.
Encodes location data using a Label Encoder.
Saves the trained model as house_price_model.pkl and label_encoder.pkl.
2. Web Application (app.py)
Loads the trained model and label encoder.
Accepts user input through index.html.
Processes inputs and predicts house prices using the trained model.
Returns the predicted price to the user.
Setup & Installation
Clone the repository:

sh
Copy
Edit
git clone <repository-url>
cd House-Price-Prediction
Install dependencies:

sh
Copy
Edit
pip install -r requirements.txt
Train the Machine Learning Model:

sh
Copy
Edit
python train_model.py
This will generate house_price_model.pkl and label_encoder.pkl.

Run the Flask Application:

sh
Copy
Edit
python app.py
Open the web application:

Go to http://127.0.0.1:5000/ in your browser.
Enter house details and get the predicted price.
Usage
Enter the house features (bedrooms, bathrooms, size, location) in the form.
Click on "Predict".
The predicted house price will be displayed on the screen.
Where to Paste Screenshots
Create a screenshots folder in the root directory:

bash
Copy
Edit
House-Price-Prediction
├── screenshots
│   ├── form_submission.png      # Screenshot of form input
│   ├── prediction_output.png    # Screenshot of predicted price output
Then, reference them in the README under a Screenshots section:

md
Copy
Edit
## **Screenshots**
### **Form Submission**
![Form Submission](screenshots/form_submission.png)

### **Prediction Output**
![Prediction Output](screenshots/prediction_output.png)
License
This project is for educational purposes. Feel free to modify and improve it.

