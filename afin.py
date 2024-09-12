def mcd(a, b):
    # Calcula el máximo común divisor de 'a' y 'b' usando el algoritmo de Euclides
    while b != 0:
        a, b = b, a % b
    return a

def encontrar_a_coprimo(n):
    # Encuentra un número 'a' que sea coprimo con 'n' (es decir, mcd(a, n) = 1)
    a = 2
    while mcd(a, n) != 1:
        a += 1
    return a

def eliminar_acentos(texto):
    # Diccionario de caracteres con acentos mapeados a sus equivalentes sin acento
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u',
        'ñ': 'ñ', 'Ñ': 'ñ'
    }
    
    # Reemplazar los caracteres acentuados por sus equivalentes sin acento
    texto_sin_acentos = ''
    for char in texto:
        if char in acentos:
            texto_sin_acentos += acentos[char]
        else:
            texto_sin_acentos += char
    return texto_sin_acentos

def limpiar_texto(texto, alfabeto):
    # Convertir el texto a minúsculas, eliminar acentos, y filtrar caracteres no presentes en el alfabeto
    texto = texto.lower()  # Convertir el texto a minúsculas
    texto = eliminar_acentos(texto)  # Eliminar los acentos
    texto_limpio = ''
    for char in texto:
        if char in alfabeto:  # Solo se queda con los caracteres del alfabeto permitido
            texto_limpio += char
    return texto_limpio

def cifrado_afin(texto, a, b, alfabeto):
    # Realiza el cifrado afín sobre el texto utilizando la fórmula: (a * índice + b) % len(alfabeto)
    texto_cifrado = ''
    for char in texto:
        if char in alfabeto:
            index = alfabeto.index(char)  
            texto_cifrado += alfabeto[(a * index + b) % len(alfabeto)]
        else:
            texto_cifrado += char  
    return texto_cifrado

def descifrar_afin(texto_cifrado, a, b, alfabeto):
    # Descifra el texto cifrado utilizando el inverso de 'a' y la fórmula inversa del cifrado afín
    a_inv = mod_inv(a, len(alfabeto))  
    texto_descifrado = ''
    for char in texto_cifrado:
        if char in alfabeto:
            index = alfabeto.index(char) 
            texto_descifrado += alfabeto[(a_inv * (index - b)) % len(alfabeto)]
        else:
            texto_descifrado += char  
    return texto_descifrado

def mod_inv(a, m):
    # Calcula el inverso modular de 'a' bajo 'm' usando el algoritmo extendido de Euclides
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m  
        m, a = a % m, m 
        x0, x1 = x1 - q * x0, x0  
    if x1 < 0:
        x1 += m0  
    return x1

def main():
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"  # Definir el alfabeto de 27 caracteres
    a = encontrar_a_coprimo(27)  # Encontrar un valor de 'a' que sea coprimo con 27
    b = 3  # Valor de 'b' (desplazamiento)

    # Imprimir los valores de 'a' y 'b'
    print(f"Valor de a: {a}")
    print(f"Valor de b: {b}")

    # Aquí se ingresa el texto directamente en el código
    texto = """El ruido visual tiene que ver con el bombardeo de imágenes con la que estamos expuestos día con día, 
               la cual, nos dispersa la atención e interpretación de los mensajes, causando así, una falta de 
               retención de información; está presente sobre todo, en el ámbito de la publicidad y al no ser 
               conscientes de su presencia será más difícil para los diseñadores y profesionales que están 
               involucrados en la creación de contenido digital, crear mensajes que sean distintivos y que capten 
               la atención de los usuarios."""

    # Limpiar el texto
    texto = limpiar_texto(texto, alfabeto)

    # Cifrar el texto
    texto_cifrado = cifrado_afin(texto, a, b, alfabeto)

    # Imprimir el texto cifrado
    print("\nTexto Cifrado:", texto_cifrado)

    # Descifrar el texto cifrado para obtener el texto original
    texto_descifrado = descifrar_afin(texto_cifrado, a, b, alfabeto)

    # Imprimir el texto descifrado
    print("\nTexto Descifrado:", texto_descifrado)

if __name__ == "__main__":
    main()
