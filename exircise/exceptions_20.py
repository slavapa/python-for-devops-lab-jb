def find_id(name):
    ret_val = None

    try:
        f = open("Cust.csv")

        for x in f:
            str_arr = x.split(",")

            if str_arr[1] == name:
                ret_val = str_arr[0]
                break
    except:
        print("cannot open and read file Cust.csv")
    finally:
        f.close()

    return ret_val


def find_all_orders(cust_id):
    ret_val = []

    try:
        f = open("Orders.csv")

        for x in f:
            str_arr = x.split(",")

            if str_arr[1] == cust_id:
                ret_val.append(str_arr)
    except:
        print("cannot open and read file Orders.csv")
    finally:
        f.close()

    return ret_val


def total_orders(name):
    orders = []
    person_id = find_id(name)
    total = 0

    if person_id is not None:
        orders = find_all_orders(person_id)

        for order in orders:
            total = float(order[3].strip())

    ret_res = {"orders": orders, "total_sum": total, "length": len(orders)}

    return ret_res


def main():
    while True:
        name = input("Enter a name(q to exit): ")
        if name == "q":
            break

        tot_ords = total_orders(name)
        print(f"The total orders: {tot_ords}")

    return


if __name__ == '__main__':
    main()
    # print(find_id("dani"))
    # print(find_all_orders("10"))
    # print(total_orders("eli"))
