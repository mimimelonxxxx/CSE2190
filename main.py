"""
name: Michelle Jiang 
title: Wages Calculator 
date-created: 2022-12-13
"""
# Need to download Jinja and Flask beforehand
from flask import Flask, render_template, request, redirect
from pathlib import Path
import sqlite3

### VARIABLES ###
DBNAME = "wages_calculator.db"

FIRSTRUN = True
if (Path.cwd()/ DBNAME).exists():
    FIRSTRUN = False

app = Flask(__name__)
### FLASK ### 
@app.route("/index.html", methods=["GET", "POST"])
def index():
    """
    renders the index.html file in flask 
    :return: renders file 
    """
    ALERT = ""
    if request.form:
        MEMBERHOURS = request.form.get("inputMemberHours")
        OVETIME = request.form.get("inputOvertimeFile")
        TOTALHOURS = request.form.get("inputTotalHoursFile")
    return render_template("index.html")

@app.route("/data.html", methods=["GET", "POST"])
def data():
    """
    renders the data.html file in flask 
    :return: renders file 
    """
    return render_template("data.html")

### SQLITE ###
def createMemberHours():
    """
    creates table for the member hours file
    :return: None
    """
    global DBNAME
    CONNECTION = sqlite3.connect(DBNAME)
    CURSOR = CONNECTION.cursor()
    CURSOR.execute("""
        CREATE TABLE 
            member_hours (
                member_name TEXT NOT NULL,
                total_hours INTEGER NOT NULL,
            );
    """)
    CONNECTION.commit()
    CONNECTION.close()

# INPUTS # 

# PROCESSING # 

# OUTPUTS #

### MAIN PROGRAM CODE ### 
if __name__ == "__main__":
    app.run(debug=True)
    # INPUTS #

    # PROCESSING # 

    # OUTPUTS #