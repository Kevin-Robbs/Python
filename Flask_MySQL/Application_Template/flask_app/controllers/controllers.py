from flask_app import app
import flask_app.Models
from flask import render_template, redirect, request, session, flash

@app.route('/')
def indexRoute():
    render_template('index.html')