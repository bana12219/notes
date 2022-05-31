#Google final
#paso 1 entender el problema
#wordcloud, es una imagen creada con palabras de diferentes tamaños, 
#usualmente el tamaño se determina por cuantas veces la palabra aparece en un texto input
#el modulo se llamará wordcloud
#no punctuation 
#deberá contar cuantas veces aparece cada palabra
#discriminar palabras comunes o irrelevantes como like, the, if
#El input será un textfile
##Things to remember 
#    Before processing any text, you need to remove all the punctuation marks.
#     To do this, you can go through each line of text, character-by-character, 
#     using the isalpha() method. This will check whether or not the character is a letter.
#    To split a line of text into words, you can use the split() method.
#    Before storing words in the frequency dictionary, check if they’re part of the 
#    "uninteresting" set of words (for example: "a", "the", "to", "if").
#     Make this set a parameter to your function so that you can change it if necessary.
#Input file
#For the input file, you need to provide a file that contains text only. 
#For the text itself, you can copy and paste the contents of a website you like. 
#Or you can use a site like Project Gutenberg to find books that are available online. 
#You could see what word clouds you can get from famous books, 
#like a Shakespeare play or a novel by Jane Austen.
#paso2 research, ver que recursos tenemos a la mano
    #   1.usar dictionary
    #   3.deberá contar cuantas veces aparece cada palabra
    #   4.Rankear el tamaño de la palabra
    #   5.escribir la imagen
    #   6.Archivo con texto input
    #   7.palabras comunes
    #   8.Signos de puntuación
    #   9.
#paso3.Planning:
    # funcion de lectura de texto/obtener el texto
    #filtrar puntuacion/palabras comunes
    #Split de texto
    #
    #Conteo de palabras
    #imprimir file
import datetime
class WordCloud:
    frequent_words=set()
    #def __init__(self):
        #self.texto=""
    def load_text(self):
        """Text loading"""
        #Next lines  could change in another text source is needed
        self.texto= open ("/media/an-b3z/Windows/files/harry.txt","r")
        self.texto=self.texto.read()
        #import urllib
        #link = "https://tools.ietf.org/html/rfc8200"
        #f = urllib.request.urlopen(link)
        #self.texto= f.read()
        #import requests 
        #resp=requests.get('https://www.gutenberg.org/browse/scores/top')
        #if resp.status_code==200:
        #    self.texto= resp.text
        #else: 
        #    print("Error",resp.status_code) 
    def filtrar_texto(self): 
        """Filtering text from noncharacter and conventional words and formatting """
        if len(self.texto)==0:
            print("Error: no content")
            return
        import string
        #filtering from non valid characters this could be just puntuation or excluding also digits
        for c in string.punctuation+string.digits:
            #replace punctuation with space considering cases like URL https://www.bbvanexttechnologies.com/
            self.texto=self.texto.replace(c," ")
        #making the list of words lowercase
        self.texto=self.texto.lower().split()
        #filtering common words
        aux=set(self.texto)
        aux.difference_update(self.frequent_words)
        #setting common words as key
        self.dictionary=dict.fromkeys(aux,0)
    def filtrar_texto2(self): 
        """Filtering text from noncharacter and conventional words and formatting """
        if len(self.texto)==0:
            print("Error: no content")
            return
        import string
        #filtering from non valid characters this could be just puntuation or excluding also digits
        for c in string.punctuation+string.digits:
            #replace punctuation with space considering cases like URL https://www.bbvanexttechnologies.com/
            self.texto=self.texto.replace(c," ")
        #making words list lowercase
        self.texto=self.texto.lower().split()
    def load_commons(self):
        """loading english common words to discard """
        self.frequent_words.update({
            "the","at","there","some","my","of","be","use","her","than","and","this","an","would","first","a","have","each","make","water",
            "to","from","which","like","been","in","or","she","him","call","is","one","do","into","who","you","had","how","time","oil","that",
            "by","their","has","its","it","word","if","look","now","he","but","will","two","find","was","not","up","more","long","for","what",
            "other","write","down","on","all","about","go","day","are","were","out",'see', 'did', 'as', 'we', 'many', 'number', 'get', 'with', 
            'when', 'then', 'no', 'come', 'his', 'your', 'them', 'way', 'made', 'they', 'can', 'these', 'could', 'may', 'i', 'said', 'so', 
            'people', 'part'})
    def word_counting(self):
        """Counting common words"""
        for word in self.dictionary.keys():
            self.dictionary[word]=self.texto.count(word)
    def word_counting2(self):
        """Counting common words"""
        for word in self.texto:
            if word in self.dictionary.keys():
                self.dictionary[word]=self.dictionary[word]+1
    def word_counting3(self):
        for w in self.texto:
            if w not in self.frequent_words:
                self.dictionary[w]=self.dictionary.get(w,0)+1
    def generate_from_frequencies(self,frequencies):
        """Generate reapeated words dictionary """
        import datetime
        start=datetime.datetime.now()
        self.load_commons()
        self.load_text()
        self.filtrar_texto()
        self.word_counting()
        print(datetime.datetime.now()-start)
        #0:00:01.379036
    def generate_from_frequencies2(self,frequencies):
        """Generate reapeated words dictionary """
        import datetime
        start=datetime.datetime.now()
        self.load_commons()
        self.load_text()
        self.filtrar_texto()
        self.word_counting2()
        print(datetime.datetime.now()-start)
        #0:00:01.273235
    def generate_from_frequencies3(self,frequencies):
        """Generate reapeated words dictionary """
        import datetime
        start=datetime.datetime.now()
        self.load_commons()
        self.load_text()
        self.filtrar_texto2()
        self.word_counting3()
        print(datetime.datetime.now()-start)
#asegurarte que existe un textfile
#eliminar palabras irrelevantes

    def to_file(self,file_name):
        from PIL import Image, ImageDraw,ImageFont
        try:  
            
            img = Image.new('RGB', (100, 100), color = (73, 109, 137))
            background_color = "white"
        except IOError: 
            print("Error al procesar imagen")
        pass
######################################################################final##########################################################################################

class WordCloud:
    frequent_words=set()
    def load_text(self):
        """Text loading"""
        import requests 
        resp=requests.get('https://www.gutenberg.org/browse/scores/top')
        if resp.status_code==200:
            self.texto= resp.text
        else: 
            print("Error",resp.status_code) 


    def filtrar_texto(self): 
        """Filtering text from noncharacter and conventional words and formatting """
        if len(self.texto)==0:
            print("Error: no content")
            return
        #import string
        #filtering non valid characters this could be just puntuation or excluding also digits
        for c in string.punctuation+string.digits:
            #replace punctuation with space considering cases like URL https://www.bbvanexttechnologies.com/
            self.texto=self.texto.replace(c," ")
        #making words list lowercase
        self.texto=self.texto.lower().split()


    def load_commons(self):
        """loading english common words to discard """
        self.frequent_words.update({
            "the","at","there","some","my","of","be","use","her","than","and","this","an","would","first","a","have","each","make","water",
            "to","from","which","like","been","in","or","she","him","call","is","one","do","into","who","you","had","how","time","oil","that",
            "by","their","has","its","it","word","if","look","now","he","but","will","two","find","was","not","up","more","long","for","what",
            "other","write","down","on","all","about","go","day","are","were","out",'see', 'did', 'as', 'we', 'many', 'number', 'get', 'with', 
            'when', 'then', 'no', 'come', 'his', 'your', 'them', 'way', 'made', 'they', 'can', 'these', 'could', 'may', 'i', 'said', 'so', 
            'people', 'part'})

            
    def word_counting(self):
        for w in self.texto:
            if w not in self.frequent_words:
                self.dictionary[w]=self.dictionary.get(w,0)+1
    def calculate_frequencies(self):
        """Generate reapeated words dictionary """
        #import datetime
        #start=datetime.datetime.now()
        self.load_commons()
        self.load_text()
        self.filtrar_texto2()
        self.word_counting3()
        #print(datetime.datetime.now()-start)
        return self.dictionary


cloud = WordCloud()
cloud.load_text()
cloud.filtrar_texto()
cloud.generate_from_frequencies("frequencies")
cloud.to_file("myfile.jpg")

cloud = WordCloud()
cloud.generate_from_frequencies("frequencies")

cloud.generate_from_frequencies2("frequencies")

cloud.generate_from_frequencies3("frequencies")


