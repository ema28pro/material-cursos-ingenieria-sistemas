import re

def limpiar_clase(entrada):
    salida = []
    
    # Eliminar saltos de línea múltiples
    entrada = re.sub(r'\n\s*\n+', '\n', entrada.strip())

    # Buscar encabezados
    encabezados = re.finditer(r'(?:#\s*)?(Clase|Examen)[^\n]*', entrada, re.IGNORECASE)
    bloques = []

    # Dividir en bloques por encabezados
    for match in encabezados:
        inicio = match.start()
        if bloques:
            bloques[-1]['fin'] = inicio
        bloques.append({'inicio': inicio, 'fin': None})
    
    if bloques:
        bloques[-1]['fin'] = len(entrada)

        for bloque in bloques:
            texto = entrada[bloque['inicio']:bloque['fin']]
            
            # Obtener título del bloque (encabezado)
            titulo = re.search(r'(?:#\s*)?(Clase|Examen)[^\n]*', texto, re.IGNORECASE)
            if titulo:
                salida.append(f"# {titulo.group().strip('# ').strip()}")

            # Buscar enlaces con formato [![...](img_url)nombre.ext](url "titulo")
            # Patrón mejorado para capturar enlaces con imágenes
            patron_enlaces = r'\[\s*(?:!\[[^\]]*\]\([^)]+\))?\s*([^\]]+?)\s*\]\(([^\s]+)\s+"([^"]+)"\)'
            enlaces = re.findall(patron_enlaces, texto, re.DOTALL)

            for nombre, url, titulo_link in enlaces:
                # Limpiar el nombre del archivo (quitar saltos de línea y texto extra)
                nombre_limpio = re.sub(r'\n+', ' ', nombre.strip())
                nombre_limpio = re.sub(r'\s*Microsoft\s+(Word|PowerPoint|Excel).*', '', nombre_limpio).strip()
                
                if nombre_limpio and not nombre_limpio.startswith('http'):
                    salida.append(f"[{nombre_limpio}]({url} \"{titulo_link.strip()}\")")

    return '\n\n'.join(salida)

# === PRUEBA ===
entrada = """

"""

print(limpiar_clase(entrada))
