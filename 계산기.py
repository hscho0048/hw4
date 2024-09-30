def add(a, b):
    return a + b + 10 #아무거나 더하기
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로는 못 나눔"
    return a / b


x = int(input("첫번쨰 숫자를 입력하세요: "))
y = int(input("두번째 숫자를 입력하세요: "))

print(f"Multiplication: {multiply(x, y)}")
print(f"Division: {divide(x, y)}")
print(f"Sum: {add(x, y)}")
print(f"Difference: {subtract(x, y)}")