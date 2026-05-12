from flask import render_template, request, url_for, redirect, jsonify, session
from flask_login import login_user, current_user, logout_user

def register_routes(app, db, bcrypt):

    @app.route('/')
    def index():
        return render_template('landing.html')