def cm(semilla, n):
    actual = semilla
    d = len(str(semilla))
    
    for i in range(n):
        # Elevar al cuadrado
        cuadrado = actual ** 2
        
        # Convertir a texto y rellenar con ceros
        texto = str(cuadrado).zfill(2 * d)
        
        # Extraer dígitos del medio
        inicio = (len(texto) - d) // 2
        actual = int(texto[inicio:inicio + d])
        
        print(f"{i+1}: {actual}")

# Ejemplo de uso
cm(1234, 5)