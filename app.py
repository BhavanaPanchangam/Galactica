from flask import Flask, render_template, request
from data import fetch_asteroids
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/dashboard")
def dashboard():
    asteroids = fetch_asteroids()
    return render_template("dashboard.html", asteroids=asteroids)

@app.route("/planets")
def planet():
    return render_template("planets.html")

@app.route("/filter", methods=["POST"])
def filter_data():
    asteroids = fetch_asteroids()
    
    # Handle empty or invalid inputs
    # distance_str = request.form.get("distance", "").strip()
    # distance = float(distance_str) if distance_str else float('inf')  # Use infinity as default for no max distance

    # date_str = request.form.get("date", "").strip()
    hazardous_str = request.form.get("hazardous", "").strip()

    # Initialize the filtered list
    filtered = []

    for a in asteroids:
        # asteroid_date = a["date"]  # Assuming 'date' is in 'YYYY-MM-DD' format
        # if float(a["distance"]) <= distance:
        #     if date_str:  # Check if a date filter is applied
        #         try:
        #             # Parse the input date and compare
        #             input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        #             if datetime.strptime(asteroid_date, "%Y-%m-%d").date() == input_date:
        #                 if hazardous_str == "" or (hazardous_str == "true" and a["hazardous"]) or (hazardous_str == "false" and not a["hazardous"]):
        #                     filtered.append(a)
        #         except ValueError:
        #             # Handle invalid date format
        #             continue
        #     else:
        if hazardous_str == "" or (hazardous_str == "true" and a["hazardous"]) or (hazardous_str == "false" and not a["hazardous"]):
                    filtered.append(a)  # No date filter applied

    return render_template("dashboard.html", asteroids=filtered)

if __name__ == "__main__":
    app.run(debug=True)
