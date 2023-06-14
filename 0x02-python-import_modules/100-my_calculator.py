if __name__ == "__main__":
#!/usr/bin/python3
import sys
import 1-calculator.py
if sys.argc != 3:
print("Usage: ./100-my_calculator.py <a> <operator> <b>")
exit(1)
if operator is not +,-,*,/:
print("Unknown operator. Available operators: +, -, * and /")
exit(1)
a, b, operator = int(sys.argv[1]), int(sys.argv[3], sys.argv[2]
result = a operator b
You can cast a and b i int() (you can assume that all arguments will be castable into integers)
print(f" {a} {operator} {b} = {result}")
