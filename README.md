
# 🏡 House Price Prediction - Flask Web Application

## 📌 Project Overview

This project is a Flask-based web application that predicts house prices based on user-input features using a Random Forest Regressor machine learning model. The model is trained on a housing dataset and considers parameters such as:

✔️ Number of bedrooms

✔️ Number of bathrooms

✔️ Square footage

✔️ Location

## 📂 Project Structure

```Folder Structure
  House-Price-Prediction
│── app.py                   # Flask application (API to handle requests & responses)
│── train_model.py           # Script to train the ML model
│── house_price_model.pkl    # Saved trained model
│── label_encoder.pkl        # Encoded location data for the model
│── requirements.txt         # Required Python packages
│
├── dataset
│   ├── train.csv            # Dataset used for training
│
├── templates
│   ├── index.html           # HTML form for user input
│
├── static
│   ├── styles.css           # CSS file for frontend styling
│
├── screenshots              # Folder for project screenshots (to be added)
│   ├── form_submission.png  
│   ├── prediction_output.png
```
## 🚀 How the Project Works
1️⃣ Model Training (train_model.py)

🔹 Loads train.csv from the dataset folder

🔹 Uses Random Forest Regressor to train the model

🔹 Encodes location data using Label Encoder

🔹 Saves the trained model as house_price_model.pkl and label_encoder.pkl


2️⃣ Web Application (app.py)

🔹 Loads the trained model and label encoder

🔹 Accepts user input through index.html

🔹 Processes inputs and predicts house prices using the trained model

🔹 Returns the predicted price to the user

## 🛠️ Setup & Installation
1️⃣ Clone the repository
```sh
git clone <repository-url>
cd House-Price-Prediction
```
2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```
3️⃣ Train the Machine Learning Model
```sh
python train_model.py
```

✅ This will generate house_price_model.pkl and label_encoder.pkl.

4️⃣ Run the Flask Application
```sh
python app.py
```
5️⃣ Open the Web Application
Go to http://127.0.0.1:5000/ in your browser.

## 🖥️ Usage
1. Enter the house details (bedrooms, bathrooms, size, location) in the form.

2. Click "Predict" to get the estimated house price.

3. The predicted price will be displayed on the screen.

## 📸 Screenshots

📌 Form Submission

📌 Prediction Output

💡 Make sure to add screenshots inside the screenshots/ folder before pushing to GitHub!
##
✨ Star ⭐ this repository if you found it useful!

📩 Feel free to contribute or report issues!
