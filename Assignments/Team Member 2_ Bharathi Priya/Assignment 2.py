Build a python code, Assume u get temperature and humidity values (generated with random function 
to a variable) and write a condition to continuously detect alarm in case of high temperature.
def detect_alarm():
    print("Alarm ringing")
    
x = (random.random())*50 #in celcius
y = (random.random())*100

if(x>40):
    detect_alarm()