n1 = int(input("test "))
n2 = int(input("tes "))

try:
    print("Division ", n1/n2)
except ZeroDivisionError as e:
    print("Div by 0 not possible")
finally: #used to close files, runs in case of error too
    print("tschuss")