import smtplib, ssl, os, time, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

start = time.time()

print('''
███╗░░░███╗░█████╗░░██████╗░██████╗  ███╗░░░███╗░█████╗░██╗██╗░░░░░███████╗██████╗░
████╗░████║██╔══██╗██╔════╝██╔════╝  ████╗░████║██╔══██╗██║██║░░░░░██╔════╝██╔══██╗
██╔████╔██║███████║╚█████╗░╚█████╗░  ██╔████╔██║███████║██║██║░░░░░█████╗░░██████╔╝
██║╚██╔╝██║██╔══██║░╚═══██╗░╚═══██╗  ██║╚██╔╝██║██╔══██║██║██║░░░░░██╔══╝░░██╔══██╗
██║░╚═╝░██║██║░░██║██████╔╝██████╔╝  ██║░╚═╝░██║██║░░██║██║███████╗███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝ 
''')

if not os.path.isfile('./emails.txt'):
    print('\n[!] "emails.txt" does not exist')
    sys.exit(1)

if not os.path.isfile('./body.txt'):
    print('\n[!] "body.txt" does not exist')
    sys.exit(1)

if len(sys.argv) > 1:
    html = True
else:
    html = False

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

load_dotenv()
email_from = os.getenv('FROM_ADDRESS')
password = os.getenv('PASSWORD')
email_list = (open('emails.txt', 'r').read()).split('\n')

printProgressBar(0, len(email_list), prefix = 'Progress:', suffix = 'Complete', length = 50)
for i in range(len(email_list)):
    email_to = email_list[i]
    email_message = MIMEMultipart()
    email_message['From'] = email_from
    email_message['To'] = email_to
    email_message['Subject'] = f'Report email'

    body = open('./body.txt', 'r').read()
    if html:
        email_message.attach(MIMEText(body, "html"))
    else:
        email_message.attach(MIMEText(body, "plain"))
    email_string = email_message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        try:
            server.login(email_from, password)
            server.sendmail(email_from, email_to, email_string)
        except:
            print('\n[!] Invalid Username or Password')
            sys.exit(1)
    printProgressBar(i + 1, len(email_list), prefix = 'Progress:', suffix = 'Complete', length = 50)

end = time.time()
total = start - end
print(f'\nExecution Time: ${str(total)}')