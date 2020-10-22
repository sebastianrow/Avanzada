from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template("Menu.html")

@app.route('/Alvarado')
def sebas():
    return render_template('Alvarado/CV.html')

@app.route('/DatosA')
def sebasd():
    return render_template('Alvarado/CV2.html')

@app.route('/FormaciónA')
def sebasf():
    return render_template('Alvarado/CV3.html')

@app.route('/InteresesA')
def sebasi():
    return render_template('Alvarado/CV4.html')
@app.route('/Gonzalez')
def gonza():
    return render_template('Gonzalez/CVG.html')

@app.route('/DatosG')
def gonzad():
    return render_template('Gonzalez/CVG2.html')

@app.route('/FormaciónG')
def gonzaf():
    return render_template('Gonzalez/CVG3.html')

@app.route('/InteresesG')
def gonzai():
    return render_template('Gonzalez/CVG4.html')

@app.route('/Mechi')
def mechi():
    return render_template('Mechi/HojaVida.html')

@app.route('/DatosM')
def mechid():
    return render_template('Mechi/Hoja2.html')

@app.route('/FormaciónM')
def mechif():
    return render_template('Mechi/Hoja3.html')

@app.route('/InteresesM')
def mechint():
    return render_template('Mechi/Hoja4.html')

if __name__ == '__main__':
   app.run(debug = True)