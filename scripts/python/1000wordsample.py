#dado un texto de mil palabras, obtener el diccionario de las repeticiones y dar el top 10 de las menos frecuentes 
#que sean capitalized. se proporciona un archivo con 1000 palabras mas comunes, para ayudar a la búsqueda
#1.leer el archivo
#2.remover la puntuacion y guardar la lista de palabras
def remove_punct(texto, case="l"):
    import string 
    for c in string.punctuation:
        texto=texto.replace(c,'')
    if case=='a':#normal
        return text.split()
    if case=='l':#lowercase
        st=st.lower()
        return texto.split()
    if case== 'u':#uppercase
        title_words=[]
        for word in texto.split():
            if word.istitle():
                title_words.append(word)
        return title_words
    return texto.split()
    
#3.filtrar las que no estén capitalized

#4.Crear el diccionario donde cada palabra es un ke y y el value el numero de repeticiones
def frequency_dict(words_list):
    freq_dict={}
    freq_set=[]
    #podrias poner las palabras en un set para que elimine los repetidos
    # iterar sobre el set, haciendo count sobre el texto, así reduces el # de iteraciones
    for word in words_list:
        freq_set.append(word)
    for word in freq_set:
        freq_dict[word]=words_list.count(word)
    return freq_dict
#5.Filtrar eliminar las más comunes dadas en el archivo
def strip_common_words(words):
    uniques=[]
    common_words=open("1000words.txt",r)
    common_words= common_words.read
    keys=dict.keys(words)
    #for word in words:
    #    uniques.append(word)
    return uniques-keys
#6.Imprimir el top 100 de las palabras
def print_ranked_dict(dictionary, top_n=2):
    ranked_list= sorted(dictionary, key=dictionary.get, reverse=True)
    for i in range (0,top_n):
        print(ranked_list[i],"repeats",dictionary[ranked_list[i]],"times")
def main():
    #1
    text= open ("/media/an-b3z/Windows/files/harry.txt","r")
    text=text.read()
    #2
    word_list=remove_punct(text,"u")
    print (word_list)
    #4
    dictionary=frequency_dict(word_list)
    #6
    print_ranked_dict(dictionary)
main()
def lectura_standar_archivos():
    with open("archivo","r+") as f:
        content= f.read()
        print(content)
    with open("file") as f:
        for line in f:
            print (line)
    #al terminar el loop whie se cierra el archivo
    with open ('file',"r+") as f:
        mock_data_reader= csv.reader(f)
        line_count=1
        for row in mock_data_reader:
            if line_c>1:
                print(row)
                line_count+=1
    with open ('file',"r+") as f:
        import json
        data= json.loads(f.read())
        print(data)
        print(type(data))


charac= string.whitespace()
str.isalpha(2)

str.upper()
