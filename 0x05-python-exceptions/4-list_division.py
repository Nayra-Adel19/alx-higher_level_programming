#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    newli = []

    for ww in range(list_length):
        dd = 0
        try:
            dd = my_list_1[ww] / my_list_2[ww]

        except TypeError:
            print("wrong type")

        except ZeroDivisionError:
            print("division by 0")

        except IndexError:
            print("out of range")

        finally:
            newli.append(dd)

    return newli
