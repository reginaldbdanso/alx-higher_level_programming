if __name__ == __main__:
#!/usr/bin/python3
import sys
if sys.argc != 3:
print("Usage: ./100-my_calculator.py <a> <operator> <b>")
exit(1)
the operator is not one of the above:
print Unknown operator. Available operators: +, -, * and / followed with a new line
exit with the value 1
You can cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)
The result should be printed like this: <a> <operator> <b> = <result>, followed by a new line
