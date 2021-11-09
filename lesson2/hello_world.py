

def print_hello_world():
    print('Hello World!')


def my_print(msg):
    print(msg)

# my_print('Hello Cyber!')

def add(a, b):
    return a + b


a = 5
b = 3
print(f'the sum of {a} + {b} is {add(a,b)}')

c = 7
if add(a,b) > c:
    print(f'{add(a,b)} is greater than {c}')
elif add(a,b) > 10:
    print(f'{add(a,b)} is greater than 10') 
else:
    print('Other')

for i in range(10):
    print(i * 10)




