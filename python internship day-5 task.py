Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #create a function getting two integer inputs from user & print the following:
>>> # a) Addition of two numbers is + value
>>> def addition(a,b):
	add=a+b
	print("addition of two number:",a+b)

	
>>> addition(70,60)
addition of two number: 130
>>> 
>>> # b) Subtraction of two numbers is + value
>>> def subtraction(a,b):
	sub=a-b
	print("subtraction of two numbers:",a-b)

	
>>> subtraction(70,60)
subtraction of two numbers: 10
>>> # c) Division of two numbers is + value
>>> def division(a,b):
	div=a/b
	print("division of two numbers:",a/b)

	
>>> division(70,60)
division of two numbers: 1.1666666666666667
>>> # d) Multiplication of two numbers is + value
>>> def multiplication(a,b):
	mul=a*b
	print("multiplication of two numbers:",a*b)

	
>>> multiplication(70,60)
multiplication of two numbers: 4200
>>> 
>>> #create a function covid()& it should accept patient name,and body temperature,by defining
>>> def covid(patient_name,body_temperature):
	print("covid statement:"+patient_name+","+body_temperature)

	
>>> covid('vijay','98 degree')
covid statement:vijay,98 degree
>>> #OR
>>> def covid(patient_name):
	print("Name of the patient:"+patient_name+"")

	
>>> covid('vijay')
Name of the patient:vijay
>>> def covid(body_temperature):
	print("Body temperature of the patient:"+body_temperature+"")

	
>>> covid('98 degree')
Body temperature of the patient:98 degree
>>> 
