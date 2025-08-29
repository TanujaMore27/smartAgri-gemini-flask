from flask import Flask, render_template, redirect, url_for, session
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__, template_folder='templates')
app.secret_key = "376a52cfa1067b8c91dc2e691d710e9f97e14504"  # Change this for security

# Firebase Initialization
cred = credentials.Certificate("farm-12b0c-firebase-adminsdk-fbsvc-376a52cfa1.json")  # Replace with your Firebase service account JSON
firebase_admin.initialize_app(cred)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/crop_management')
def crop_management():
    return render_template('cropmanagement.html')  # Make sure this file exists

@app.route('/SEASONS')
def seasons_planting():
    return render_template('SEASONS.html')  # Make sure this file exists
@app.route('/seed_planting')
def seed_planting():
    return render_template('SEASONS.html')  # Make sure this file exists

@app.route('/summerseeds')
def summerseeds():
    return render_template('summerseeds.html')  # Make sure this file exists

@app.route('/monsoonseeds')
def monsoonseeds():
    return render_template('monsoonseeds.html')  # Make sure this file exists

@app.route('/winterseeds')
def winterseeds():
    return render_template('winterseeds.html')  # Make sure this file exists

@app.route('/tea')
def tea_management1():
    return render_template('teaC.html')  # Make sure this file exists
@app.route('/sugarcane')
def sugarcane_management():
    return render_template('sugarcaneC.html')  # Make sure this file exists
@app.route('/tomato')
def tomato_management1():
    return render_template('tomatoC.html')  # Make sure this file exists
@app.route('/orange')
def orange_management1():
    return render_template('orangeC.html')  # Make sure this file exists
@app.route('/cotton')
def cotton_management1():
    return render_template('cottonC.html')  # Make sure this file exists
@app.route('/rice')
def rice_management1():
    return render_template('riceC.html')  # Make sure this file exists
@app.route('/maize')
def maize_management1():
    return render_template('maizeC.html')  # Make sure this file exists
@app.route('/mango')
def mango_management1():
    return render_template('mangoC.html')  # Make sure this file exists
@app.route('/barley')
def barley_management1():
    return render_template('barleyC.html')  # Make sure this file exists
@app.route('/mustard')
def mustard_management1():
    return render_template('mustardC.html')  # Make sure this file exists
@app.route('/wheat')
def wheat_management1():
    return render_template('wheatC.html')  # Make sure this file exists
@app.route('/guava')
def guava_management1():
    return render_template('guavaC.html')  # Make sure this file exists

# -------------------------------------------- CROP

@app.route('/teaS')
def teaS():
    return render_template('teaS.html')  # Make sure this file exists
@app.route('/sugarcaneS')
def sugarcaneS():
    return render_template('sugarcaneS.html')  # Make sure this file exists
@app.route('/tomatoS')
def tomatoS():
    return render_template('tomatoS.html')  # Make sure this file exists
@app.route('/orangeS')
def orangeS():
    return render_template('orangeS.html')  # Make sure this file exists
@app.route('/cottonS')
def cottonS():
    return render_template('cottonS.html')  # Make sure this file exists
@app.route('/riceS')
def riceS():
    return render_template('riceS.html')  # Make sure this file exists
@app.route('/maizeS')
def maizeS():
    return render_template('maizeS.html')  # Make sure this file exists
@app.route('/mangoS')
def mangoS():
    return render_template('mangoS.html')  # Make sure this file exists
@app.route('/barleyS')
def barleyS():
    return render_template('barleyS.html')  # Make sure this file exists
@app.route('/mustardS')
def mustardS():
    return render_template('mustardS.html')  # Make sure this file exists
@app.route('/wheatS')
def wheatS():
    return render_template('wheatS.html')  # Make sure this file exists
@app.route('/guavaS')
def guavaS():
    return render_template('guavaS.html')  # Make sure this file exists

# -------------------------------------------- seeds
@app.route('/financial_analysis')
def financial_analysis():
    return render_template('financeanalysis.html')  # Make sure this file exists

@app.route('/finance')
def finance():
    return render_template('finance.html')

@app.route('/progressReport')
def progressReport():
    return render_template('progressReport.html')

@app.route('/seedsown')
def seedsown():
    return render_template('seedsown.html')

@app.route('/harvest')
def harvest():
    return render_template('harvest.html')

@app.route('/fertilizer')
def fertilizer():
    return render_template('fertilizertrack.html')

@app.route('/cropgrowth')
def cropgrowth():
    return render_template('cropgrowth.html')

@app.route('/predict')
def predict():
    return redirect("https://aistudio.google.com/prompts/new_chat?model=gemini-2.0-flash-exp")

if __name__ == '__main__':
    app.run(debug=True)
