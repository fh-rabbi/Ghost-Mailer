# Author: Fazle Rabbi
# Date: 13 December, 2022
# Don't change my credit
# Changing credit don't made you a coder!
# This source code is open so that you can gain some knowledge from this code.
# WARNING: This tool is just for fun & educational purpose.
# So, I will not be responsible if you use this tool for bad purpose.Keep in mind!
from flask import *
from flask_mail import *
from time import sleep
from getpass import getpass
import os
app = Flask(__name__)

# Colors
red = '\033[1;91m'
green = '\033[1;92m'
yellow = '\033[1;93m'
blue = '\033[1;94m'
cyan = '\033[1;96m'
white = '\033[1;0m'

os.system('clear')

# Banner
def banner():
   print(f"""{green}

   _____  _                  _   
  / ____|| |                | |  
 | |  __ | |__    ___   ___ | |_ 
 | | |_ || '_ \  / _ \ / __|| __|
 | |__| || | | || (_) |\__ \| |_ 
  \_____||_| |_| \___/ |___/ \__|
                _  _             
     /\/\    __ _ (_)| |  ___  _ __ 
    /    \  / _` || || | / _ \| '__|
   / /\/\ \| (_| || || ||  __/| |   
   \/    \/ \__,_||_||_| \___||_|   
                                 
{white}💻 {yellow}Coded By Fazle Rabbi{white}
{white}🌐 {yellow}https://github.com/fh-rabbi{white}
   """)

# Menu
def menu():
   email = input(f'{white}[?] {green}Your Gmail:{white}')
   print('\n')
   print(f'{red}🚨 NOTE: \033[31m Don\'t use your gmail account password.You need to use App Password.For generate App Password visit bellow link and read the instruction: {white}')
   print('🌐 https://fh-rabbi.github.io/Ghost-Mailer')
   print('\n')
   password = getpass(f'[?] {green}Your Password:{white}')
   name = input(f'[?] {green}Your Name:{white}')
   subject = input(f'[?] {green}Email Subject:{white}')
   message = input(f'[?] {green}Your Message:{white}')
   target = input(f'[?] {green}Target Email:{white}')
   amount = input(f'[?] {green}Amount Of Email:{white}')
   print(f'[*] {yellow}Sending Email Please Wait...')
   # Configure the Flask Mail
   app.config.update(
         MAIL_SERVER = 'smtp.gmail.com',
         MAIL_PORT = 465,
         MAIL_USERNAME = email,
         MAIL_PASSWORD = password,
         MAIL_USE_SSL = True
   )
   # Instantiate the Mail class.
   mail = Mail(app)
   sendMail(email,password,name,subject,message,target,mail,amount)
   
# Send Mail
def sendMail(email,password,name,subject,message,target,mail,amount):
   with app.app_context():
      try:
         for i in range(0,int(amount)):
            mail.send_message(
               subject,
               sender = name,
               recipients = [target],
               body = message
            )
            print(f'{white}[✓] {green}Message Sent Successful ➡️ {white} {i+1}')
         opt = input(f"{white}[*] {yellow}Press Enter For Continue:")
         if opt or opt == '':
            os.system('clear')
            os.system('python app.py')
      except:
            print(f'{red}[!]Oops! Something went wrong')
            sleep(1)
            os.system('clear')
            os.system('python app.py')
         
        
banner()
menu()