import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin = 14

GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, 1000)
pwm.start(0)
try:
    while 1:
        duty = input()
        duty = int(duty)
        pwm.ChangeDutyCycle(duty)
        print("{:.2f}".format(duty/100*3.3))
except KeyboardInterrupt:
    print('\nСтоп')
finally:
    pwm.stop
    GPIO.output(pin, 0)
    GPIO.cleanup()