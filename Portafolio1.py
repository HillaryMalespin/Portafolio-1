"""
Entrada: Un número entero positivo
Salida: Divisores del numero
Restricciones:Tienen que ser un numero entero positivo
Función que imprime los divisores de un numero.
Nombre: Divisores.
"""
def divisores(num):
    if(isinstance(num,int)):
        if num%2==0:
            return num/2
        else:
            return divisoresDeUnNumero_aux(num-1)/2


def divisoresDeUnNumero_aux(num):
    if(isinstance(num,int)):
        if num==0:
            return 0
        else:
            return divisoresDeUnNumero_aux(num-1)
    


##########################################################################################################################################################
"""
Entrada: Dos números enteros positivos
Salida: Resultado de la multiplicación de estos
Restricciones: Tienen que ser numeros enteros
Función que hace multiplicaciones sin usar el operador de multiplicación.
Nombre: Multiplicar recursivo.
"""
def multiplicarRecursivo(num,factor):
    if (isinstance(num,int)):
        if factor==0:
            return 0
        elif factor==1:
            return num
        else:
            return num + multiplicarRecursivo(num,factor-1)
############################################################################################################################################################
"""
Entrada: Dos números enteros positivos
Salida: Resultado de la división de estos
Restricciones: Tienen que ser numeros enteros positivos
Función que hace divisiones sin usar el operador de division.
Nombre: division recursivo.
"""
def divisionRecursivo(divisor,dividendo):
    if isinstance(divisor,int) and isinstance(dividendo,int):
        if (dividendo<divisor):
            return 0
        else:
            return 1 + divisionRecursivo(dividendo-divisor,divisor)
##################################################################################
"""
Entrada: Un numero punto decimal positivo
Salida: Un numero entero positivo
Restricciones: Tienen que ser numeros positivos
Función que convierte numeros de punto decimal a enteros.
Nombre: Corriendo a entero.
"""
def corrimientoAentero(num):
    if isinstance(num,float)and(num>0):
        if (num==0):
            return 0
        else:
            return (corrimientoAentero(num*10*1)) 
    else:
        return 0
##############################################################################
"""
Entrada: Un numero punto decimal cualquiera
Salida: Un numero entero 
Restricciones: Tienen que ser numeros punto decimal
Función que convierte numeros de punto decimal a enteros.
Nombre: Contar digitos flotantes
"""
def contarDigitosFlotante(num):
    
##############################################################################

 """
Entrada: Un numero y un indice.
Salida: Un numero segun el indice indicado.
Restricciones: Los numeros deben ser enteros positivos
Nombre:indiceNumero
Función que devuelve un digito según su indice.
"""
def contarDigito(num):
    if(isinstance(num,int)== False):
        return print("Error tipo de dato, no es entero")
    elif (num==0):
        return 1
    else:
        return contarDigitos_aux(num)

def contarDigitos_aux(n):
    if(n==0):
        return 0
    else:
        return 1 + contarDigitos_aux(n//10)
    
def reversonumero(num):
    if isinstance(num, int):
        if (num>=0):
            if (num<=10):
                return num
            else:
                return reversonumero_aux(num,contarDigito(num))
        else:
            print("El numero debe ser positivo")
    else:
        print("Error: el  numero no es entero")

def reversonumero_aux(num, largo):
    if largo == 0:
        return 0
    else:
        return (num%10)*(10**(largo-1))+reversonumero_aux(num//10, largo-1)

def indiceNumeroAux(num):
    if(isinstance(num,int)):
       return (num//10)

def indice(num,indice):
    if indice==0:
        return num%10
    if indice==1:
        return ((num%10**2)//10)
    if indice==2:
        return ((num%10**3)//10**2)
    if indice==3:
        return ((num%10**4)//10**3)
    if indice==4:
        return ((num%10**5)//10**4)
    if indice==5:
        return ((num%10**6)//10**5)
    if indice==6:
        return ((num%10**7)//10**6)
    if indice==7:
        return ((num%10**8)//10**7)
    if indice==8:
        return ((num%10**9)//10**8)
    if indice==9:
        return ((num%10**10)//10**9)
    if indice==10:
        return ((num%10**11)//10**10)
##########################################################################
"""
Entrada: Un numero y un indice.
Salida: Devuelve un numero segun el indice indicado.
Restricciones: Los numeros deben ser enteros positivos
Nombre:cortarNumero
Función que corta un digito según su indice.
"""

def contarDigito(num):
    if(isinstance(num,int)== False):
        return print("Error tipo de dato, no es entero")
    elif (num==0):
        return 1
    else:
        return contarDigitos_aux(num)

def contarDigitos_aux(n):
    if(n==0):
        return 0
    else:
        return 1 + contarDigitos_aux(n//10)
    
def reversonumero(num):
    if isinstance(num, int):
        if (num>=0):
            if (num<=10):
                return num
            else:
                return reversonumero_aux(num,contarDigito(num))
        else:
            print("El numero debe ser positivo")
    else:
        print("Error: el  numero no es entero")

def reversonumero_aux(num, largo):
    if largo == 0:
        return 0
    else:
        return (num%10)*(10**(largo-1))+reversonumero_aux(num//10, largo-1)

def indiceNumeroAux(num):
    if(isinstance(num,int)):
       return (num//10)

def indice(num,indice):
    if indice==0:
        return num%10
    if indice==1:
        return ((num%10**2)//10)
    if indice==2:
        return ((num%10**3)//10**2)
    if indice==3:
        return ((num%10**4)//10**3)
    if indice==4:
        return ((num%10**5)//10**4)
    if indice==5:
        return ((num%10**6)//10**5)
    if indice==6:
        return ((num%10**7)//10**6)
    if indice==7:
        return ((num%10**8)//10**7)
    if indice==8:
        return ((num%10**9)//10**8)
    if indice==9:
        return ((num%10**10)//10**9)
    if indice==10:
        return ((num%10**11)//10**10)

def indice2(num,indice):
    if indice2==0:
        return num%10
    if indice2==1:
        return ((num%10**2)//10)
    if indice2==2:
        return ((num%10**3)//10**2)
    if indice2==3:
        return ((num%10**4)//10**3)
    if indice2==4:
        return ((num%10**5)//10**4)
    if indice2==5:
        return ((num%10**6)//10**5)
    if indice2==6:
        return ((num%10**7)//10**6)
    if indice2==7:
        return ((num%10**8)//10**7)
    if indice2==8:
        return ((num%10**9)//10**8)
    if indice2==9:
        return ((num%10**10)//10**9)
    if indice2==10:
        return ((num%10**11)//10**10)

def cortarNumero(num,indice,indice2):
    if isinstance (num,int):
        return cortarNumero(0,indice,indice2)
