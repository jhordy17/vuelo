
vuelo = {'Aerolinea': 'Avianca',
    'Vuelo': 'AV3102',
    'Origen': 'CTG',
    'Destino': 'MDE',
    'Tipo_Maleta': ['Cabina', 'Mano', 'Bodega']
}

print("/////Diccionario:////")
for key, value in vuelo.items():
    print(f"{key}")

print("\n Tipo de maleta:")
for maleta in vuelo['Tipo_Maleta']:
    print(maleta)
