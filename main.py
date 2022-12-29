"""
name: Michelle Jiang 
title: Wages Calculator 
date-created: 2022-12-13
"""
# Need to download Jinja and Flask beforehand
import os
from flask import Flask, render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename # security measure 
from pathlib import Path
import sqlite3

"""
Notes to self:
- every time the user uploads files, they must upload all files or it will not update
- every time the user uploads files and they work, the database will delete itself and a new database will be created 
- if these constraints are not met, nothing will happen *atomicity* 
- somehow need to get open(file) and file.readlines with flask 
"""

### VARIABLES ###
DBNAME = "wages_calculator.db"

FIRSTRUN = True
if (Path.cwd()/ DBNAME).exists():
    FIRSTRUN = False

UPLOADFOLDER = 'C:/Users/cryst/.vscode/CSE2190' # use your own file route 
ALLOWEDEXTENSIONS = {'csv', 'txt'}

app = Flask(__name__)
app.config['UPLOADFOLDER'] = UPLOADFOLDER

### FLASK ### 
@app.route("/", methods=["GET", "POST"])
def index():
    """
    renders the index.html file in flask 
    :return: renders file 
    """
    ALERT = ""
    if request.method == 'POST': 
        if ('inputRegularHours' or "inputOvertimeFile" or "inputSales" or "inputProduction" or "inputSummary" or "inputTotalHoursFile")not in request.files:
            ALERT = "Please upload all files!"
        REGULARFILE = request.files['inputRegularHours']
        if REGULARFILE.filename == '':
            ALERT = "Please select files!"
        if REGULARFILE and allowed_file(REGULARFILE.filename):
            FILENAME = secure_filename(REGULARFILE.filename)
            REGULARFILE.save(os.path.join(app.config['UPLOADFOLDER'], FILENAME))
            ALERT = "Regular Hours file uploaded!"
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

### FUNCTIONS ### 
def allowed_file(FILENAME):
    return '.' in FILENAME and \
           FILENAME.rsplit('.', 1)[1].lower() in ALLOWEDEXTENSIONS # splits the filename at the . and checks if it can be used

### SQLITE ###

# INPUTS # 

# PROCESSING # 

# OUTPUTS #

### MAIN PROGRAM CODE ### 
if __name__ == "__main__":
    app.run(debug=True)
    # INPUTS #

    # PROCESSING # 

    # OUTPUTS #