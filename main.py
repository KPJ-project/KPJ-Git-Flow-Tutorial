from my_add import *
from my_minus import *
from my_multiple import *
from my_divide import *


if __name__ == "__main__":

    two_numbers=[int(ele) for ele in input("두개의 수를 입력하세요.\nex)3 4\n").split(" ")]
    num1,num2 = two_numbers

    print(my_add(num1,num2))
    print(my_minus(num1,num2))
    print(my_multiple(num1,num2))
    print(my_divide(num1,num2))

