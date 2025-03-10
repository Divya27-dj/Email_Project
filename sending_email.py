import random
import smtplib


def send_mail():
    try:
        f=open("customer_mails.txt", "r")
        customer_mails=f.read()

        customer_mails = customer_mails.split(",")
        print(customer_mails)
    except:
        print("File not Available")

    sender_email="div******1@gmail.com"

    for i in customer_mails:
        otp_number = random.randint(00000,9999)
        print(otp_number)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, "egas********kbmu")
        message = f"Hi your OTP number is {otp_number}"

        try:
            s.sendmail(sender_email, i, message)
            print("mail sent successfully")
            s.quit()
        except:
            print("mail not sent")

send_mail()
        