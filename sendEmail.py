import smtplib

sm = smtplib.SMTP('smtp.gmail.com',587)

sm.starttls()

sender_email = "*******@gmail.com"
receiver_email = "*******r@gmail.com"
sm.login(sender_email,"**password**")

sm.sendmail(sender_email,receiver_email,"Hello")
sm.quit()
