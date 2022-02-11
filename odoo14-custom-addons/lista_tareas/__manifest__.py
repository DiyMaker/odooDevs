# -*- coding: utf-8 -*-
{
    'name': "MyList",

    'summary': """
    Sencilla Lista de tareas""",

    'description': """
    Sencilla lista de tareas utilizadas para crear un nuevo módulo con un nuevo modelo de datos
    """,

    'author': "Alejandro Gonzalez Hermoso",
    'website': "https://github.com/DiyMaker/odooDevs.git",
    #Indicamos que es una aplicación
    'application': True,

    # En la siguiente URL se indica que categorias pueden usarse
    # https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # Vamos a utilizar la categoria Productivity
    'category': 'Productivity',
    'version': '0.1',

    # Indicamos lista de modulos necesarios para que este funcione correctamente
    # En este ejemplo solo depende del modulo "base"
    'depends': ['base'],

    # Esto siempre se carga
    'data': [
        #Este primero indica la politica de acceso del modulo
        'security/ir.model.access.csv',
        #Cargamos las vistas y las plantillas
        'views/views.xml',
    ]
}
