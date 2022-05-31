#files
#file.open()
#read
#readline
#readlines
#write
#seek

#open (name_ofFile, model)
text = open('HarryPotter.txt',"r")
text=text.read()
print(text)
sentences= text.split('.')
