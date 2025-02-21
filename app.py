from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__, template_folder="templates")

# Ruta del archivo Excel
EXCEL_FILE = "C:/flask_app/clientes.xlsx"

def cargar_datos():
    """Carga los datos del Excel."""
    return pd.read_excel(EXCEL_FILE, engine="openpyxl")

def guardar_datos(df):
    """Guarda los datos actualizados en el Excel."""
    df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")

@app.route("/", methods=["GET", "POST"])
def index():
    df = cargar_datos()

    if request.method == "POST":
        for index, row in df.iterrows():
            key = f"suplementado_{index}"
            if key in request.form:
                df.at[index, "Suplementado"] = request.form[key]

        guardar_datos(df)
        return redirect(url_for("index"))

    return render_template("form.html", clientes=df.iterrows())

if __name__ == "__main__":
    app.run(debug=True)
