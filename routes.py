from flask import render_template, request, redirect
from models import Order
from mail import send_email

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

        send_email(new_order)

        return redirect('/')