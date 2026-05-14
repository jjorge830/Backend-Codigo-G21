#arrays

frutas = ['Manzana','Platano','Papaya', 'pitahaya']
print(frutas[1])
frutas.append('Mandarina')

persona = {
    'nombre' : 'eduardo',
    'apellido' : 'de rivero',
    'correo' : 'ederrivero@gmail.com',
    'hobbies' : ['comer','programar','montar vici'],
    'direcciones': {
        'calle': 'calle los geraneos',
        'numero': 870,
        'postal': '04010'

    },
    'viudo': False,
    'familiares': ('Juanito Perez','Maria Aguilar','Roxana Washington')
}

print(persona['nombre'])
print(persona['hobbies'])
print(len(persona['hobbies']))
print(persona['direcciones']['calle'])