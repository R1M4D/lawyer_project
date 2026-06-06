from flask import render_template, request, url_for, redirect, jsonify, session
from flask_login import login_user, current_user, logout_user
from models import Order


def register_routes(app, db, bcrypt):

    @app.route('/')
    def index():
        return render_template('landing.html')



    @app.route('/order', methods=['POST'])
    def create_order():
        new_order = Order(
            name=request.form.get('name'),
            phone=request.form.get('phone'),
            email=request.form.get('email'),
            service_type=request.form.get('service'),
            situation=request.form.get('message')
        )

        db.session.add(new_order)
        db.session.commit()


        print(new_order)

        return redirect('/')