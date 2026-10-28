# -*- coding: utf-8 -*-
{
    'name': 'Gelen Kudeaketa - Ikastetxeak eta Gelak',
    'version': '17.0.1.0.0',
    'category': 'Education',
    'summary': 'Ikastetxeen, gelen eta erreserben kudeaketa integrala (Odoo 17)',
    'description': """
Ikastetxeen eta Gelen Kudeaketa (Ikastetxeak_Kudeatu)
=====================================================
- Ikastetxeak, Gelak eta Erreserbak modeloak.
- Ikastetxeen zerrenda eta formulario bistak.
- Gelen zerrenda eta formulario bistak (Erreserbatu eta ErreserbatuWizard botoiekin).
- Erreserben zerrenda, formulario eta egutegi bistak.
- Erreserba morroia (Wizard).
- Menu nagusia (Ikastetxeak_Kudeatu) eta azpimenuak (Ikastetxeak, Gelak -> Erreserbak, Gela zerrenda).
- Erlazionatutako eremuak formularioetan (Many2one, One2many, Related eremuak).
    """,
    'author': 'balvarezech',
    'website': 'https://github.com/balvarezech/Gelen-kudeaketa',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ikastetxea_views.xml',
        'views/gela_views.xml',
        'views/erreserba_views.xml',
        'views/erreserba_wizard_views.xml',
        'views/menu_views.xml',
        'data/demo_data.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
