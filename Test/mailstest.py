import smtplib

smtp_object = smtplib.SMTP_SSL('smtp.office365.com',587)

print(type(smtp_object))
print(smtp_object.ehlo())