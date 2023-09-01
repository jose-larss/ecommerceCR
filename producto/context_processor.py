def get_current_path(request):
    path_final = ""
    path_final_total = ""

    string = request.get_full_path()

    for i in range (len(string)):
        if i > 10:
            path_final += string[i]
    
    """
    print(path_final)
    posicion_final = len(path_final)-1
    posicion_anterior = len(path_final)-8
    print(posicion_final)
    print(posicion_anterior)

    try:
        caracter_final = int(path_final[posicion_final]) > 0
        caracter_anterior = int(path_final[posicion_anterior]) > 0
    except:
        caracter_final = None
        caracter_anterior = None
    print(len(path_final)-7)
    if caracter_final and caracter_anterior:
        print("los 2 caracteres son numeros")
        for i in range(len(path_final)-7):
            path_final_total += path_final[i]

    print(path_final_total)
    """

    return { 'path_categoria': path_final }


