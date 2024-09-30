def add(a, b):
    return a + b 
def subtract(a, b):
    return a - b

x = int(input("첫번쨰 숫자를 입력하세요: "))
y = int(input("두번째 숫자를 입력하세요: "))

print(f"Sum: {add(x, y)}")
print(f"Difference: {subtract(x, y)}")