#Given n non-negative integers representing an elevation map 
# where the width of each bar is 1, compute how much water 
# it is able to trap after raining.
#
#
#
#
#          *
#     *aaa**a*
#   *a**a******
#[0,1,0,2,1,0,1,3,2,1,2,1]
class Solution(object):
    def trap(self, height):
    #que tenga más de dos elementos para calcular el area entre ambos
        if not len(height)>2:
            return 0
        sublist=list()
        #1 encontrar el elemento mas alto
        maxList=max(height)
        agua =0
        sublist.append(height.pop())    
        while height:
            print(height[-1])
        #2 . encontrar los elementos entre ambos que son los que quedan entre 
        # un numero menor al maximo o el priero de la sublista
            if height[-1]<sublist[0] and height[-1]<maxList:
                sublist.append(height.pop())
                continue
        #3. si el elemento es mayor o igual al inicial o maximo
        # hemos encontrado un borde, realizar la suma
            if height[-1]>=sublist[0] or height[-1]>=maxList:
            # el area se determina por el borde menor
            #3.a.sumar al agua el area enconrada                
                #si ay valores intermedios
                if sublist[0] >maxList:
                    agua=agua+(sublist[0] *len(sublist)-1)  
                else:
                    agua=agua+(maxList *len(sublist)-1) 
                sublist.pop(0)              
            #3.b.restar al agua los espacios ocupados dentro del area
                for elemento in sublist:
                    agua=agua-elemento
                print("reiniciando valores")
            #3.c.ubicar el inicio de la siguiente iteracion
                sublist.clear()
                sublist.append(height[-1])
                height.pop()
            #caso en que sea = max
            if height and sublist[0]==maxList:
                maxList=max(height)
            print("siguiente",height)
        return agua


if __name__ == "__main__":
	s=Solution()
	print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
