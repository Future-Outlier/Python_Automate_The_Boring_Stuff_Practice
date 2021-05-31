import smtplib
smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
# https://www.serversmtp.com/smtp-server-address/
# todo the above will show you the SMTP server address
print(smtpObj.ehlo()) # a rule to say hello

smtpObj.starttls() # to Encrypt
account = input("account") # for gmail.com emails
password = input("passowrd")
smtpObj.login(account, password)
smtpObj.sendmail(account, "ericchen1201@yahoo.com.tw", "Subject: So long.\n"
                "Dear Alice, so long and thanks for all the fish. Sincerely, Bob")
smtpObj.quit()
#https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
# todo the above can fix your problem.