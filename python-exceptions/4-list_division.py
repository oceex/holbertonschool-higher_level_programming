#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    x, tmp = 0, 0.0
    new = []
    while not list_length == x:
        try:
            tmp = 0.0
            tmp = my_list_1[x]/my_list_2[x]

        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
            break
        except Exception:
            break
        finally:
            new.append(tmp)
            x += 1
    return new
