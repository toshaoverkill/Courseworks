import time
try:
    import GPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
print("LDR pin")
LDR_pin = int(input())
print("DIODE pin")
DIODE_pin = int(input())
GPIO.setwarnings(False)
GPIO.setup(DIODE_pin,GPIO.OUT)
print("value")
value = int(input())
def Ctime(pin):
    reading = 0;
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.5)
    GPIO.setup(pin,GPIO.IN, pull_up_down = GPIO.PUD_UP)
    while (GPIO.input(pin) == GPIO.LOW):
        reading+=1;
    return reading
def LED_on():
    global DIODE_pin
    print ("LED on")
    GPIO.output(DIODE_pin,GPIO.HIGH)
def LED_off():
    global DIODE_pin
    print ("LED off")
    GPIO.output(DIODE_pin,GPIO.LOW)
try:
    while True:
        if Ctime(LDR_pin) < value:
            LED_on()
        else:
            LED_off()
        time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()
