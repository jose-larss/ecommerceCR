def get_current_path(request):
    string = request.get_full_path()
    path_final = ""
    for i in range (len(string)):
        if i > 10:
            path_final += string[i]
    
    print(path_final)
    return { 'path_categoria': path_final }


