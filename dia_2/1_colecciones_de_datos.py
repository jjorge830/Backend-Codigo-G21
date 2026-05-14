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

curso = {
    'nombre': 'Backend',
    'duracion': '10 semanas',
    'fecha_inicio': '2024-11-11',
    'fecha_fin': '2025-01-30',
    'topics': ['Python', 'Express', 'Django', 'Flask'],
    'semanas': [
        {
            'nombre': 'semana 01',
            'descripcion': 'intro a python'
        },
        {
            'nombre': 'semana 02',
            'descripcion': 'base de datos'
        }
    ],
    'habilidades': ('logica de programacion', 'manejo de eventos', 'despliegue en servidores'),
    'finalizado': False,
    'profesores': {
        'Arnold Gallegos', 'Eduardo de Rivero'
    },
    'costo': 550.76,
    'descanso': 'a veces'
}