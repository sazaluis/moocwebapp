#listas, tuplas y diccionarios

ejemplo = [1, ["otra", "lista"], ("una", "tupla")]
"ejemplo tiene una lista [] y una tupla ()"
mi_lista = ["Primer elemento", 2, 3.14]
mi_lista[0] = "Nuevo primer elemento" # estamos cambiando el valor del primer elemento
print(mi_lista[-1]) # imprime 3.14

mi_diccionario = {"clave1": "valor1", "pi": 3.14, 1:2}
print(mi_diccionario["pi"]) #imprime 3.14
print(mi_diccionario[1]) # imprime 2
# recuerda que el índice de un diccionario es una clave, no una posición

print(ejemplo[2][1]) #"accede a la lista ejemplo y luego dentro a tupla, las tuplas no son modificables, tronco"

lista = ["uno","dos"]
lista[0] = "cerete"
print(lista)



