import math

sin=math.sin
cos=math.cos
tan=math.tan
fac=math.factorial
sqrt=math.sqrt

op=input('enter op(+,-,*,/sin,cos,tan,cot,factorial,sqrt) : ')

if op=='sin':
  a=float(input('enter number1 : '))
  r=(math.radians(a))

if op=='cos':
  a=float(input('enter number1 : ')) 
  r=cos(math.radians(a))

if op=='tan':
  a=float(input('enter number1 : '))
  r=tan(math.radians(a))

if op=='cot':
  a=float(input('enter number1 : '))
  b=tan(math.radians(a))
  r=1/b

if op=='+':
   a=float(input('enter number1 : '))
   b=float(input('enter number 2:  '))
   r=a+b

if op=='-':
   a=float(input('enter number1 : '))
   b=float(input('enter number 2:  '))
   r=a-b

if op=='/':
   a=float(input('enter number1 : '))
   b=float(input('enter number 2:  '))
if b==0:
   print('error')
else:
   r=a/b

if  op=='*':
   a=float(input('enter number1 : '))
   b=float(input('enter number 2:  '))
   r=a*b

if op=='fac':
   a=float(input('enter number1 : '))
   if a<0:
      print('error')
      r=fac(a)

if op=='sqrt':
   a=float(input('enter number1 : '))
   if a<0:
      print('error')
      r=sqrt(a)
      
print(r)
