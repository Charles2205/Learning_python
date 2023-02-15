import requests as req
user_number=input('Enter your number: ')
user_message = input('Enter your message: ')
sender_name=input('Enter sender name: ')

url = f"https://sms.arkesel.com/sms/api?action=send-sms&api_key=OnhIUGk5UG5DVkZjandoaHI=&to={user_number}&from={sender_name}&sms={user_message}"

is_sent=req.get(url)
print(is_sent.status_code)