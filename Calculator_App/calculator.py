class calculator:
    def __init__(self):
        self.num1 = int(input("Enter First number:"))
        self.num2 = int(input("Enter Second number:"))

    def add(self):
        r = self.num1 + self.num2
        result = f"The sum of {str(self.num1)} and {str(self.num2)} is {str({r})}"
        print(result)

    def substract(self):
        r = self.num1 - self.num2
        result = f"The difference of {str(self.num1)} and {str(self.num2)} is {str({r})}"
        print(result)

    def multiply(self):
        r = self.num1 * self.num2
        result = f"The product of {str(self.num1)} and {str(self.num2)} is {str({r})}"
        print(result)

    def divide(self):
        r = self.num1 / self.num2
        result = f"The division of {str(self.num1)} and {str(self.num2)} is {str({r})}"
        print(result)

if __name__ == '__main__':
    cal = calculator()
    cal.add()
    cal.substract()
    cal.multiply()
    cal.divide()