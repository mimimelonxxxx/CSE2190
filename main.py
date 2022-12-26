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
@app.route("/", methods=["GET", "POST"])
def index():
    """
    renders the index.html file in flask 
    :return: renders file 
    """
    ALERT = ""
    if request.files:
        MEMBERHOURS = request.files.get("inputMemberHours")
        OVERTIME = request.files.get("inputOvertimeFile")
        TOTALHOURS = request.files.get("inputTotalHoursFile")
        if MEMBERHOURS != "" and OVERTIME != "" and TOTALHOURS != "":
            ALERT = "Successfully added files into database! "
        else:
            ALERT = "Please upload the correct number of files! "
    return render_template("index.html", alert=ALERT)

@app.route("/data.html", methods=["GET", "POST"])
def data():
    """
    renders the data.html file in flask 
    :return: renders file 
    """
    return render_template("data.html")

@app.route("/member.html", methods=["GET", "POST"])
def member():
    """
    renders the member.html file in flask 
    :return: renders file 
    """
    return render_template("member.html")

### SQLITE ###
def createAllTables():
    """
    creates member hours table, overtime table, total hours table using respective files
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
    CURSOR.execute("""
        CREATE TABLE
            overtime (
                event_name TEXT NOT NULL,
                overtime INTEGER NOT NULL,
                total_duration INTEGER NOT NULL
            );
    """)
    CURSOR.execute("""
        CREATE TABLE
            total_hours (
                total_hours REAL NOT NULL
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