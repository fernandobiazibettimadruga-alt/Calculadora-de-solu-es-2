from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_volume(dose, concentracao):
    return dose / concentracao

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = None
    if request.method == "POST":
        medicamento = request.form["medicamento"]
        dose = float(request.form["dose"])

        if medicamento == "Ampicilina":
            concentracao = 250
            tempo = "5 min"
            diluente = "SF 0,9% ou SG 5%"
        elif medicamento == "Gentamicina":
            concentracao = 20
            tempo = "30 min"
            diluente = "SF 0,9% ou SG 5%"
        elif medicamento == "Metronidazol":
            concentracao = 5
            tempo = "60 min"
            diluente = "Puro"
        elif medicamento == "Cafeína":
            concentracao = 20
            tempo = "30 min (ataque) / 10 min (manutenção)"
            diluente = "Puro"
        else:
            concentracao = 1
            tempo = "-"
            diluente = "-"

        volume = calcular_volume(dose, concentracao)
        resultado = {
            "medicamento": medicamento,
            "dose": dose,
            "concentracao": concentracao,
            "volume": round(volume, 2),
            "tempo": tempo,
            "diluente": diluente
        }

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)