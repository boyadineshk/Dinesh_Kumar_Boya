class Calculator:
    def calculate(self, a, b, operation):
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            if b == 0:
                return "Error: Cannot divide by zero"
            return a / b
        else:
            return "Error: Invalid operation"

def main():
    calc = Calculator()
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (add/subtract/multiply/divide): ").lower()
    
    result = calc.calculate(a, b, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
