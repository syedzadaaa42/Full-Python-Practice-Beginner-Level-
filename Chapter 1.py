import http.client # Q3
print("Hello World")

# Q1 Write a program to print twinkle twinkle little star in python  
# print("Twinkle Twinkle Little star, how i wonder what you are")
print("======================================================")

 #Q2 Use REPLE and print the table of 5 using it:
for i in range(1,11):  #This is a for loop where i is in range between 1 and 10
    print(f"5 x {i} = {5*i}")  #This print the table of 5 against the loop 

#Q3 Install an external module and use it to perform an operation of your interest.

#Lets create a connection
#the code below will create a connection to the specified server such as (google.com)
connection = http.client.HTTPSConnection("www.youtube.com")
# Now send a GET request to the root path ('/') of the server (google.com)
connection.request("GET", "/")
# Now get the response from the server.
response = connection.getresponse()
# now print the status and response
print("Status:", response.status)
print("Reason:", response.reason)

# Now read the content of the response:
data = response.read()

#try decoding witht he utf-8, fallback to iso-8859-1 if it fails 
try:
    content = data.decode('utf-8') # This tries to decode the repsonse using the utf-8 
except UnicodeDecodeError:
    content = data.decode('iso-8859-1') # if the utf-8 doesnt work then this line of code 

# now print the content of the response
print("Content:", data.decode())

# now close the conneciton:
connection.close()