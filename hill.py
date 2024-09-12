alfabeto = "abcdefghijklmnñopqrstuvwxyz"

def eliminar_acentos(texto):
    # Reemplaza caracteres con acento por sus versiones sin acento.
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u',
        'ñ': 'ñ', 'Ñ': 'ñ'
    }
    texto_sin_acentos = ''
    for char in texto:
        if char in acentos:
            texto_sin_acentos += acentos[char]
        else:
            texto_sin_acentos += char
    return texto_sin_acentos

def mod_inv(a, m):
    # Encuentra el inverso modular de 'a' bajo 'm' usando el algoritmo extendido de Euclides.
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

def filtrar_texto(texto):
    # Filtra el texto para contener solo caracteres del alfabeto permitido.
    return ''.join([char for char in texto if char in alfabeto])

def matriz_multiplicacion(A, B, mod):
    # Multiplica dos matrices A y B, y devuelve la matriz resultado bajo módulo 'mod'.
    resultado = [[sum(A[i][k] * B[k][j] for k in range(len(B))) % mod for j in range(len(B[0]))] for i in range(len(A))]
    return resultado

def matriz_inversa_2x2(K, mod):
    # Calcula la inversa de una matriz 2x2 bajo módulo 'mod'.
    det = (K[0][0] * K[1][1] - K[0][1] * K[1][0]) % mod
    det_inv = mod_inv(det, mod)
    if det_inv == 0:
        raise ValueError("La matriz no tiene inversa en este módulo.")
    K_inv = [
        [K[1][1] * det_inv % mod, -K[0][1] * det_inv % mod],
        [-K[1][0] * det_inv % mod, K[0][0] * det_inv % mod]
    ]
    for i in range(2):
        for j in range(2):
            K_inv[i][j] = K_inv[i][j] % mod
    return K_inv

def texto_a_vectores(texto, n):
    # Convierte el texto en una lista de vectores de tamaño 'n'.
    vectores = [alfabeto.index(char) for char in texto]
    return [vectores[i:i+n] for i in range(0, len(vectores), n)]

def vectores_a_texto(vectores):
    # Convierte una lista de vectores a texto usando el alfabeto.
    return ''.join(alfabeto[num] for vector in vectores for num in vector)

def cifrar_hill(texto, K):
    # Cifra el texto utilizando la matriz de cifrado 'K'.
    n = len(K)
    texto = texto.replace(" ", "").lower()
    texto = eliminar_acentos(texto)
    texto = filtrar_texto(texto)
    if len(texto) % n != 0:
        texto += 'x' * (n - len(texto) % n)
    vectores = texto_a_vectores(texto, n)
    cifrado_vectores = matriz_multiplicacion(vectores, K, 27)
    cifrado_texto = vectores_a_texto(cifrado_vectores)
    return cifrado_texto

def descifrar_hill(texto, K):
    # Descifra el texto cifrado utilizando la matriz inversa de 'K'.
    K_inv = matriz_inversa_2x2(K, 27)
    n = len(K)
    vectores = texto_a_vectores(texto, n)
    descifrado_vectores = matriz_multiplicacion(vectores, K_inv, 27)
    descifrado_texto = vectores_a_texto(descifrado_vectores)
    return descifrado_texto

def imprimir_matriz(K):
    # Imprime la matriz de cifrado 'K'.
    print("Matriz de cifrado K:")
    for fila in K:
        print(fila)

# Ejemplo de uso
K = [[3, 2], [2, 5]]  # Matriz de cifrado
imprimir_matriz(K)  # Imprimir la matriz en la terminal

texto = """El ruido visual tiene que ver con el bombardeo de imágenes con la que estamos expuestos día con día, 
           la cual, nos dispersa la atención e interpretación de los mensajes, causando así, una falta de 
           retención de información; está presente sobre todo, en el ámbito de la publicidad y al no ser 
           conscientes de su presencia será más difícil para los diseñadores y profesionales que están 
           involucrados en la creación de contenido digital, crear mensajes que sean distintivos y que capten 
           la atención de los usuarios."""

texto = texto.lower()  # Convertir a minúsculas
texto_cifrado = cifrar_hill(texto, K)
texto_descifrado = descifrar_hill(texto_cifrado, K)

print("\nTexto Cifrado:", texto_cifrado)
print("\nTexto Descifrado:", texto_descifrado)
