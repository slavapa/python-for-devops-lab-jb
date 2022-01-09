import math
import cmath


def determine_even_number(num):
    ret_val = 0
    remainder = num % 2

    if remainder == 0:
        ret_val = 1

    return ret_val


def exercise_1():
    num = int(input("Enter a number: "))
    res = determine_even_number(num)

    if num == 1:
        print(f"The number {num} is even")
    else:
        print(f"The number {num} is odd")

    return num


def mypow(x, y):
    s = 1
    for i in range(y):
        s *= x

    return s


def pow_2(num, power):
    return num ** power


def exercise_2_pow(num=None):
    if num is None:
        num = int(input("Enter a number: "))
    power = int(input("Enter a power number: "))

    res = pow_2(num, power)
    print(f"The power of the {num} is:  {res}")

    return num


def calc_discount(price, discount=float(-1)):
    if discount <= 0:
        discount = float(input("Enter a discount: "))

    price = (price / 100) * (100 - discount)
    ret_val = (price, discount)

    return ret_val


def exercise_3():
    price = float(input("Enter a price: "))
    price_params = ()

    if price > 100:
        price_params = calc_discount(price)
    else:
        price_params = calc_discount(price, 10)

    print(f"The final price after discount {price_params[1]}%  is: {price_params[0]}")

    return price_params


def exercise_5_print_menu():
    msg = "Choose from the menu a letter\n"
    msg += "a - the biggest divider\n"
    msg += "b - the smallest divider\n"
    msg += "c - the result of pow(a,b)\n"
    msg += "d - the result of sqrt(a)-sqrt(b)]\n"
    msg += "e - exit\n"

    ret_res = input(msg)
    return ret_res


def bigest_divider(num1, num2):
    if num1 > num2:
        return num1

    return num2


def smallest_divider(num1, num2):
    if num1 < num2:
        return num1

    return num2


def sqrt(num):
    return math.sqrt(num)


def sqdiff(a, b):
    return pow(a, 0.5) - pow(b, 0.5)


def exercise_5():
    a = num1 = float(input("Enter a first number: "))
    b = num2 = float(input("Enter a second number: "))

    d = {'a': biggest, 'b': smalldiv, 'c': mypow, 'd': sqdiff}

    while True:
        print("a- the biggest divider")
        print("b- the smallest divider")
        print("c- the result of pow(a,b)")
        print("d- the result of sqrt(a)-sqrt(b)")
        print("e- exit")
        c = input("")
        if c == 'e':
            break
        print(d[c](a, b))
        # choice = exercise_5_print_menu()
        #
        # if choice == "a":
        #     ret_val = bigest_divider(num1, num2)
        #     print(f"The biggest divider from(a={num1}, b={num2}) is: {ret_val}")
        # elif choice == "b":
        #     ret_val = smallest_divider(num1, num2)
        #     print(f"The smallest divider from(a={num1}, b={num2}) is: {ret_val}")
        # elif choice == "c":
        #     ret_val = pow_2(num1, num2)
        #     print(f"The a={num1} to the power of, b={num2}) is: {ret_val}")
        # elif choice == "d":
        #     ret_val = sqrt(num1) - sqrt(num2)
        #     print(f"the result of sqrt(a={num1})-sqrt(b={num2})] is: {ret_val}")
        # elif choice == "e":
        #     break

    return


def smalldiv(a, b):
    m = min(a, b)
    for i in range(2, m):
        if (a % i == 0) and (b % i == 0):
            return i
        return 1


def biggest(a, b):
    m = min(a, b)
    for i in range(m, 1, -1):
        if (a % i == 0) and (b % i == 0):
            return i
        return 1


def eq_zero(num):
    if num == 0:
        return True

    return False


def square_equation(a, b, c):
    # calculate the discriminant: https://www.programiz.com/python-programming/examples/quadratic-roots
    # ax2 + bx + c = 0, where a, b and c are real numbers and a ≠ 0
    d = (b ** 2) - (4 * a * c)

    if d < 0:
        print("The the discriminant d = (b**2) - (4*a*c) should be Greater than or equal to 0")
        return ()
    else:
        # find two solutions
        sol1 = (-b - cmath.sqrt(d)) / (2 * a)
        sol2 = (-b + cmath.sqrt(d)) / (2 * a)
        ret_result = (sol1, sol2)

        return ret_result


def exercise_4():
    print("ax2+bx+c=0")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    if not eq_zero(a):
        #     print("The zero value for a is forbidden")
        # else:
        ret_result = square_equation(a, b, c)

        if isinstance(ret_result, tuple) and len(ret_result) > 0:
            print('The solution are {0} and {1}'.format(ret_result[0], ret_result[1]))

    return


def test():
    return


def main():
    # num = exercise_1()
    exercise_2_pow()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    test()


if __name__ == '__main__':
    main()
