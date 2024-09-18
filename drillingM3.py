
nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

magos = ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]

def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = 'El gran ' + magos[i]

def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

print("Lista completa de nombres antes de ser modificada:")
imprimir_nombres(nombres)

hacer_grandioso(magos)

print("Magos grandiosos:\n")
imprimir_nombres(magos)

print("Científicos:\n")
imprimir_nombres(cientificos)

print("Otros:\n")
imprimir_nombres(otros)
