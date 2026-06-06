import smtplib
from email.mime.text import MIMEText

def send_email(order):
    smtp_server = "smtp.yandex.ru"
    smtp_port = 465

    sender_email = "eibragimoov@yandex.ru"
    sender_password = "vlkyprkypnrkxsty"

    msg = MIMEText(
        f"""
        Новый заказ:

        Имя: {order.name}
        Телефон: {order.phone}
        Email: {order.email}
        Услуга: {order.service_type}
        Сообщение: {order.situation}
        """
    )

    msg["Subject"] = "Новый заказ"
    msg["From"] = sender_email
    msg["To"] = order.email


    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)