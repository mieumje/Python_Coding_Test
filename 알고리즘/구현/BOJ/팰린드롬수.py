while True:
    input_data = int(input())
    if input_data == 0:
        break

    tmp = str(input_data)
    tmp_reverse = ""
    for i in range(1, len(tmp) + 1):
        tmp_reverse += tmp[-i]

    if input_data == int(tmp_reverse):
        print("yes")
    else:
        print("no")
