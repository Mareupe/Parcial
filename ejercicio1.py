
vector = ['Luke', 'Darth Vader', 'Yoda','Leia Organa', 'Han Solo']

# def barrido(vec):
#     if(len(vec) == 1):
#         print(vec[0])
#     else:
#         print(vec[-1])
#         barrido(vec[0:-1])

# # barrido(vector)

pos = 0
def busqueda_recursiva(vec, dato, pos):
    if dato == 'Yoda':
        if vec[pos] > -1:
            print('esta')
        else:
            print('no esta')
        print(vec[pos])
    else:
        return (0)