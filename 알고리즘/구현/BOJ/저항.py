input_data = [input() for _ in range(3)]

regi = {'black': 0, 'brown': 1,
        'red': 2, 'orange': 3,
        'yellow': 4, 'green': 5,
        'blue': 6, 'violet': 7,
        'grey': 8, 'white': 9,
        }

answer = (regi[input_data[0]] * 10 + regi[input_data[1]]) * \
    (10 ** regi[input_data[2]])
print(answer)
