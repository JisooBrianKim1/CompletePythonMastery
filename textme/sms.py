from twilio.rest import Client 
 
account_sid = 'AC66bfca55c37aaf76cd4566d89a2c51a3' 
auth_token = '7e38557e30563e8383e0cdee5bc962d9' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12253145542', 
                              body ='Ligma balls',       
                              to='+15622298999' 
                          ) 
 
print(message.sid)