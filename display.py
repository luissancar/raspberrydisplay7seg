import time

import RPi.GPIO as GPIO


A=17
B=27
C=22
D=18
E=23
F=24
G=25

P=9



GPIO.setmode(GPIO.BCM)
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(P, GPIO.OUT)


def ponBlanco():
	GPIO.output(A, GPIO.LOW)
	GPIO.output(B, GPIO.LOW)
	GPIO.output(C, GPIO.LOW)
	GPIO.output(D, GPIO.LOW)
	GPIO.output(E, GPIO.LOW)
	GPIO.output(F, GPIO.LOW)
	GPIO.output(G, GPIO.LOW)
	GPIO.output(P, GPIO.LOW)

def ponNumero(num):
	ponBlanco()
	if num == 0:
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.HIGH)
		GPIO.output(E, GPIO.HIGH)
		GPIO.output(F, GPIO.HIGH)
		GPIO.output(A, GPIO.HIGH)
	if num == 1:
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
	if num == 2:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(G, GPIO.HIGH)
		GPIO.output(E, GPIO.HIGH)
		GPIO.output(D, GPIO.HIGH)
	if num == 3:
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.HIGH)
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(G, GPIO.HIGH)
	if num == 4:
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(F, GPIO.HIGH)
		GPIO.output(G, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
	if num == 5:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(F, GPIO.HIGH)
		GPIO.output(G, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.HIGH)
	if num == 6:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.HIGH)
		GPIO.output(E, GPIO.HIGH)
		GPIO.output(F, GPIO.HIGH)
		GPIO.output(G, GPIO.HIGH)
	if num == 7:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(B, GPIO.HIGH)
	if num == 8:
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)
		GPIO.output(D, GPIO.HIGH)
		GPIO.output(E, GPIO.HIGH)
		GPIO.output(F, GPIO.HIGH)
		GPIO.output(A, GPIO.HIGH)	
		GPIO.output(G, GPIO.HIGH)	
	if num == 9:
		GPIO.output(A, GPIO.HIGH)
		GPIO.output(B, GPIO.HIGH)
		GPIO.output(F, GPIO.HIGH)
		GPIO.output(G, GPIO.HIGH)
		GPIO.output(C, GPIO.HIGH)


while True:
	for i in range(10):
		ponNumero(i)
		print(i)
		time.sleep(0.3)

	
GPIO.cleanup()	



