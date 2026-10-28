# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Ikastetxea(models.Model):
    _name = 'ikastetxeak.ikastetxea'
    _description = 'Ikastetxea'
    _order = 'kodea, name'

    name = fields.Char(
        string='Ikastetxearen izena',
        required=True,
        help='Ikastetxearen izen ofiziala (adibidez: Zornotza)'
    )
    kodea = fields.Char(
        string='Ikastetxe kodea',
        required=True,
        help='Ikastetxearen kode identifikatzailea (adibidez: 102)'
    )
    helbidea = fields.Char(
        string='Helbidea',
        help='Ikastetxearen kokaleku fisikoa edo helbidea'
    )
    telefonoa = fields.Char(string='Telefonoa')
    emaila = fields.Char(string='Posta elektronikoa')
    webgunea = fields.Char(string='Webgunea')
    deskribapena = fields.Text(string='Deskribapena')

    # Erlazionatutako eremuak (Relational fields)
    gela_ids = fields.One2many(
        comodel_name='ikastetxeak.gela',
        inverse_name='ikastetxe_id',
        string='Gelak'
    )
    gela_kopurua = fields.Integer(
        string='Gela kopurua',
        compute='_compute_gela_kopurua',
        store=True,
        help='Ikastetxeak dituen gela kopuru osoa'
    )

    _sql_constraints = [
        ('kodea_unique', 'unique(kodea)', 'Ikastetxearen kodeak bakarra izan behar du!')
    ]

    @api.depends('gela_ids')
    def _compute_gela_kopurua(self):
        for record in self:
            record.gela_kopurua = len(record.gela_ids)
