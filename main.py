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
@app.route("/")
def index():
    return render_template("index.html")

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