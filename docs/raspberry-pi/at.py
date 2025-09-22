#!/usr/bin/python

import RPi.GPIO as GPIO
import serial
import time

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
ser.flushInput()

powerKey = 4
command_input = ''
rec_buff = ''

def powerOn(powerKey):
    print('SIM7080X is starting:')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(powerKey, GPIO.OUT)
    time.sleep(0.1)
    GPIO.output(powerKey, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(powerKey, GPIO.LOW)
    time.sleep(5)

def powerDown(powerKey):
    print('SIM7080X is logging off:')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(powerKey, GPIO.OUT)
    GPIO.output(powerKey, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(powerKey, GPIO.LOW)
    time.sleep(5)
    print('Good bye')

def send_at_command(cmd, delay=1):
    ser.write((cmd + '\r\n').encode())
    time.sleep(delay)
    resp = b""
    while ser.inWaiting() > 0:
        resp += ser.read(ser.inWaiting())
        time.sleep(0.1)
    return resp.decode(errors='ignore')

def checkStart():
    while True:
        ser.write('AT\r\n'.encode())
        time.sleep(1)
        ser.write('AT\r\n'.encode())
        time.sleep(1)
        ser.write('AT\r\n'.encode())
        time.sleep(1)
        if ser.inWaiting():
            time.sleep(0.01)
            recBuff = ser.read(ser.inWaiting())
            print('SOM7080X is ready\r\n')
            print('try to start\r\n' + recBuff.decode())
            if 'OK' in recBuff.decode():
                break
        else:
            powerOn(powerKey)

def print_device_info():
    print("SIM Card status:")
    print(send_at_command('AT+CPIN?'))

    print("Signal quality:")
    print(send_at_command('AT+CSQ'))

    print("Network registration:")
    print(send_at_command('AT+CGREG?'))

    print("System info:")
    print(send_at_command('AT+CPSI?'))

    print("Activate PDP context:")
    print(send_at_command('AT+CNACT=0,1', delay=3))

    print("Check IP address:")
    print(send_at_command('AT+CNACT?'))

try:
    checkStart()
    print_device_info()

    while True:
        command_input = input('Please input the AT command, press Ctrl+C to exit:')
        ser.write((command_input + '\r\n').encode())
        time.sleep(0.1)
        if ser.inWaiting():
            time.sleep(0.01)
            rec_buff = ser.read(ser.inWaiting())
            if rec_buff:
                print(rec_buff.decode())

except KeyboardInterrupt:
    print("Exiting...")

finally:
    if ser is not None:
        ser.close()
    powerDown(powerKey)
    GPIO.cleanup()
