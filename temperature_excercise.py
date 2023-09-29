
 #Excercise 1

text = input()
temperature = text[ :-1]
scale = text[-1]
temperature_num = int(temperature)

if scale == 'C':
    temperature_num1 = (temperature_num *9/5) +32
    temperature_num1= str(int(temperature_num1))
    scale1 = 'F'
    temperature_num2 = temperature_num + 273.15
    temperature_num2= str(int(temperature_num2))
    scale2 = 'K'

elif scale == 'K':
    temperature_num1 = (temperature_num * 9/5) -459.67
    temperature_num1 = str(int(temperature_num1))
    scale1 = 'F'
    temperature_num2 = temperature_num - 273.15
    temperature_num2 = str(int(temperature_num2))
    scale2 = 'C'


elif scale == 'F':
    temperature_num1 = (temperature_num * -32) * 5/9
    temperature_num1 = str(int(temperature_num1))
    scale1 = 'C'
    temperature_num2 = (temperature_num + 459.67) *5/9
    temperature_num2 = str(int(temperature_num2))
    scale2 = 'K'

print (temperature_num1 + scale1, temperature_num2 +scale2)















