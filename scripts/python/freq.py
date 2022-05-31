texto='''At Google, we don’t 
just accept difference — we celebrate it, we support it, 
and we thrive on it for the benefit of our employees, our products, 
and our community. Apprentices become part of our mission to build 
great products for every user, and their different experiences help 
ensure that our products are as diverse as our users.'''

def analiza(texto):
    ocurrencias={}
    for c in texto:
        c=c.lower()
        if c == ' ':
            continue
        if c in ocurrencias:
            ocurrencias[c]+=1
            continue
        ocurrencias[c]=1
    return ocurrencias


componentes= analiza(texto)

for c in componentes:
    print("letra ",c, " se repite ", componentes[c])

# unpacking
letras='ana paola'
a,n,a1,s,p,a2,o,l,a3= letras
print(a,n,a1,s,p,a2,o,l,a3)
a,*otras,b= letras
print (otras)
 

 