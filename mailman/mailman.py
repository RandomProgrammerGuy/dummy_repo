import smtplib

# -- Define SMTP Server -- #
server = smtplib.SMTP('smtp.gmail.com', 587)

# -- Login to Gmail account with SMTP -- #
server.login('farjamautomatedsender@gmail.com', 'VerySecurePassword!')

# -- Recieve destination and message -- #
print('Send to: ')
to = input()

print('\n Message: ')
message = input()
