def ContarPares_aux(num):
        if num==0:
            return 0
        if num%2==0:
            return 1+numeroPar(num//10)
        else:
            return 0+numeroPar(num//10)

def numeroPar(num):
    if(isinstance(num,int)and num>=0):
        if(num==0):
           return 0
        else:
           return ContarPares_aux(num)
    else:
        return'por favor ingrese un numero entero'

    
