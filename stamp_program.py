"""
start
get the numbers of sheets
sheets / 5
round answer to next number
output the resul to the user
end
"""
import math


def calculate(sheet):
    answer = sheet / 5
    rounded = math.ceil(answer)
    print("sheet is : ", sheet)
    print("The answer is: ", answer)
    print("rounded is: ", rounded)
    print("================================")
    return rounded

output = calculate(16)

print("The number of stamps needed is: ", output)