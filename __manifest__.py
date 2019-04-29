# -*- coding: utf-8 -*-
# Copyright <2019> <Quadit S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "add_country ",
    'version': '"12.0.1.0.0"',
    'summary': """ module for add country in the website""",
    'author': 'Leticia Gonzalez Contreras, Quadit, S.A. de C.V.',
    'company': 'Quadit, S.A. de C.V',
    'website': "https://www.quadit.mx",
    'category': 'website',
    'depends': ["account",
                "website_crm",
		'website_form', 
		'website_partner', 
		'crm'],
    'data': [
        'views/add_country.xml',
            ],
    'demo': [],
    'images': [],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
