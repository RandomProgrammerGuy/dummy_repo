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

# -- Confirm send and send method -- #
print('\n You want to send the message "' + message + '" to ' + to + ". Is that correct? \n Press Y to confirm, N to deny")
confirm = input()
if confirm == 'y' or confirm == 'Y':
    server.sendmail('farjamautomatedsender@gmail.com', to , message)
    print("Mail has been (hopefully) sent")
else:
    print('Mail send declined')