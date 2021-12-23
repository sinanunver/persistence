import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('sinan.unver@gmail.com','tinocmdgvrntohks')

    subject = 'From python'

    body = 'Next time \n\n I will try to send an attachment'

    msg = f'Subject: {subject} \n\n {body}'

    smtp.sendmail('sinan.unver@gmail.com', 'sinan.unver@gmail.com', msg)
