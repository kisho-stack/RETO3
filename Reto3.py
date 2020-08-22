#Declarar variables
contador = 1
notas_acumuladas = []
alumnos = ()

alumnos = input("Ingresar nombre del alumno : ")
#Condicion ingresar 5 notas
while contador <=5:
    
#Condicion solo se ingresan numeros
    while True:
        try:
            
            notas = int(input(f"Hola, por favor digita nota {contador} :"))
            contador = contador + 1
            notas_acumuladas.append(notas) #Almacenando numeros en una lista 
            sum(notas_acumuladas) #Sumando valores de la lista
            promedio=round(sum(notas_acumuladas)/5) #calculando promedio y redondeando
            nota_maxima = max(notas_acumuladas) #Obteniendo nota maxima
            nota_minima = min(notas_acumuladas) #Obteniendo nota minima
                        
#Mensaje solicitando ingresar dato correcto           
        except ValueError as e:
            print ("La entrada es incorrecta, ingresa un numero")
        break

print (f"El promedio del alumno {alumnos} es : {promedio}")
print (f"La nota mayor es {nota_maxima} y la nota minima es {nota_minima}" )
        


#python hackathons3.py
