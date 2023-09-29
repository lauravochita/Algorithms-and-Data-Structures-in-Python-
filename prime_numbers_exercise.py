#Excercise 2

sequence = input("Enter a sequence of positive numbers:")
numbers_str = sequence.split()

numbers = [ ]
for num_str in numbers_str:
    num = int(num_str)
    numbers.append(num)

def is_prime(number):
     if number <= 1:
         return False

     if number % 2 == 0:
         return False

     if number %3 == 0:
         return False

     for n in range (3, ):
         while n * n <= number:
             if number % n == 0:
                 return False
             else:
                 print (number)
is_prime(numbers)









