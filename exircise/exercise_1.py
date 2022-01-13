import subprocess, sys

import docker
from tabulate import tabulate


def exercise_1():
    print(f"6 + 2 = {6 + 2}")
    print(f"6 - 2 = {6 - 2}")
    print(f"6 * 2 = {6 * 2}")
    return


def exercise_2():
    print(f"6 / 2 = {6 / 2}")
    print(f"6 // 2 = {6 // 2}")
    print(f"6 % 2 = {6 % 2}")
    return


def exercise_3():
    print(f"2 / 5 = {2 / 5}")
    print(f"2 // 5 = {2 // 5}")
    print(f"2 % 5 = {2 % 5}")
    return


def exercise_4():
    a, b, c, d, e, f = (1, 1, 1, 1, 1, 1)

    a, b = int(input("enter two values for a,b: "))
    b = int(input("Enter a number a: "))

    c = a + b
    d = a - b
    e = a * b
    f = a / b

    print(a, b, c, d, e, f)
    return


def exercise_5():
    headers = ("a", "b", "c=a+b", "d=a-b", "e=a*b", "f=a/b")
    a, b, c, d, e, f = (1, 1, 1, 1, 1, 1)

    a, b = input("enter two values for a,b: ").split()

    a = int(a)
    b = int(b)

    print("calculating c,d,e,f ...")

    c = a + b
    d = a - b
    e = a * b
    f = a / b

    result_tup = [a, b, c, d, e, f]
    result_strings = [[str(x) for x in result_tup]]
    # print(*result_tup)
    print_data(headers, result_tup)
    print_data(headers, result_strings, "t")

    # print("{0:<5}  {1:<5}  {2:<6}  {3:<5}  {4:<10}  {5:<15}".format(*headers))
    # print("{0:>5}  {1:>5}  {2:>5}  {3:>5}  {4:>10}  {5:>15}".format(*result_tup))
    # print("{0:<5}  {1:<5}  {2:<5}  {3:<5}  {4:<10}  {5:<15}".format(*result_tup))

    return


def print_data(headers_arg, data, format_type="d"):

    if format_type == "d" or format_type is None:
        print("{0:<5}  {1:<5}  {2:<6}  {3:<5}  {4:<10}  {5:<15}".format(*headers_arg))
        print("{0:<5}  {1:<5}  {2:<6}  {3:<5}  {4:<10}  {5:<15}\n\n".format(*data))
        # print("{0:>5}  {1:>5}  {2:>6}  {3:>5}  {4:>10}  {5:>15}".format(*data))
    else:
        # https://www.delftstack.com/howto/python/data-in-table-format-python/
        print(tabulate(data, headers=headers_arg))

    return


def exercise_6():
    headers = ("a", "b", "c=a+b", "d=a-b", "e=a*b", "f=a/b")
    a, b = input("enter two values for a,b: ").split()

    a = int(a)
    b = int(b)

    print("calculating c,d,e,f ...")
    result_tup = [a, b]

    c = a + b
    result_tup.append(c)

    c = a - b
    result_tup.append(c)

    c = a * b
    result_tup.append(c)

    c = a / b
    result_tup.append(c)

    result_strings = [[str(x) for x in result_tup]]
    print_data(headers, result_tup)
    print_data(headers, result_strings, "t")

    return


def exercise_7():
    a, b, c = input("enter two values for a, b, c: ").split()
    result = int(a) + int(b) + int(c)

    print(f"The summary of the a = {a}, b = {b} c = {c} is: {result}")
    return

def exercise_8():
    arr = input("enter two values for a, b, c: ").split()
    result = int(arr[0]) + int(arr[1]) + int(2)

    print(f"The summary of the a = {arr[0]}, b = {arr[1]} c = {arr[2]} is: {result}")
    return


def exercise_9():
    s = 0
    a = int(input("enter num :"))
    s+=a
    a = int(input("enter num :"))
    s+=a
    a = int(input("enter num:"))
    s+=a
    a = int(input("enter num:"))
    s+=a
    a = int(input("enter num:"))
    s+=a
    print(s)
    return


def exercise_10():
    # (a+b-c)*d/c
    arr = input("(a+b-c)*d/c - Enter values for a, b, c, d, c : ").split()
    result = (int(arr[0])+int(arr[1])-int(arr[2]))*int(arr[3])/int(arr[4])
    print(f"The result of the  (a+b-c)*d/c is :{result}")
    return


def exercise_12():
    # (a+b-c)*d/c
    num = int(input("Enter a number : "))
    print(f"The square of a number {num} is: {num*num}")
    return


def exercise_14():
    # X | X*X
    head_arr = ("Num", "Num * Num")
    # arr = input("Enter a 3 numbers : ").split()
    arr = ["1", "2", "10"]

    result_arr = [[int(arr[0]), int(arr[0]) * int(arr[0])], [int(arr[1]), int(arr[1]) * int(arr[1])],
                  [int(arr[2]), int(arr[2]) * int(arr[2])]]

    print(tabulate(result_arr, headers=head_arr, tablefmt="grid"))

    return


def exercise_15():
    # X | X*X
    head_arr = ("Num", "Num * Num")
    # arr = input("Enter 2 dimensions in a right-angled triangle : ").split()
    arr = ["15", "22"]
    sq = (int(arr[0]) * int(arr[1]))/2
    print(f"The Area of the right-angled triangle with the dimensions {arr[0]} and {arr[1]} is: {sq}")
    return


def exercise_16():
    # price = input("Enter a price : ").split()
    price = float("5645.336")
    vat = price*0.17
    print(f"The VAT for the price {price:.2f} is: {vat:.2f}")
    return


def exercise_17():
    # price = input("Enter a price : ")
    price = float("100")
    vat = price*0.17
    print(f"The VAT for the price {price:.2f} is: {vat:.2f}. The total price is: {price+vat:.2f}")
    return


def exercise_18_19():
    # price = input("Enter a price : ")
    price = float("100")
    print(f"The neto price {price*0.83:.2f}, the vat is: {price*0.17:.2f}. The total price is: {price:.2f}")
    return

def exercise_20():
    grade_arr = ["80", "85", "75", "90", "87"]
    tot = 0

    for grade in grade_arr:
        tot += int(grade)

    print(f"The average is: {tot/5:.2f}")

    print(res)

    return


def output(cmd):
    cmd_l = cmd.split()
    output1 = subprocess.Popen(cmd_l, stdout=subprocess.PIPE).communicate()[0]
    output1 = output1.decode("utf-8")
    return output1


def exercise_my_1():
    client = docker.from_env()
    res = client.containers.run("ubuntu:latest", "echo hello world")
    # client.containers.run("ubuntu:latest", detach=True)
    print(res)

    res = client.containers.run("bfirsh/reticulate-splines", detach=True)
    print(res)

    res = output("docker ps")
    print(f"Print out docker ps\n{res}")

    res = output("docker images")
    print(f"Print out images\n{res}")

    ls = client.containers.list()
    print(f"Containers list: {ls}")

    return


if __name__ == "__main__":
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    # exercise_7()
    # exercise_8()
    # exercise_9()
    # exercise_10()
    # exercise_12()
    # exercise_14()
    # exercise_15()
    # exercise_16()
    # exercise_17()
    # exercise_18_19()
    # exercise_20()
    exercise_my_1()
