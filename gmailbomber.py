sender_email=input("ENTER SENDER EMAIL:")
rec_email=input("ENTER RECEIVER EMAIL:")
password=input("ENTER SENDER EMAIL PASSWORD:")
massage=input("ENTER MASSAGE:")
ran_ge=int(input("HOW MANY MASSAGE YOU WANT TO SENT:"))

import smtplib
for b in range(ran_ge):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print("login successed")
    server.sendmail(sender_email, rec_email, massage)
    print("Email has been sent to", rec_email)

















