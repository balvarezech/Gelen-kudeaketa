# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class Gela(models.Model):
    _name = 'ikastetxeak.gela'
    _description = 'Ikastetxeko Gela'
    _order = 'name'

    name = fields.Char(
        string='Gela izena',
        required=True,
        help='Gelaren izena (adibidez: Ethazi)'
    )
    edukiera = fields.Integer(
        string='Edukiera',
        default=30,
        help='Gelak har dezakeen ikasle/pertsona kopurua'
    )
    baliabideak = fields.Text(
        string='Eskuragarri dauden baliabideak',
        help='Gelak dituen baliabideak (adib. proiektorea, ordenagailuak...)'
    )
    kokalekua = fields.Char(
        string='Kokalekua',
        help='Gelaren kokapena eraikinean (adibidez: lehen solairua)'
    )
    erabilgarri = fields.Boolean(
        string='Erabilgarri',
        default=True,
        help='Gela erreserbatu edo erabiltzeko moduan dagoen'
    )

    # Erlazio eremua: Gelak zein ikastetxeri dagokion
    ikastetxe_id = fields.Many2one(
        comodel_name='ikastetxeak.ikastetxea',
        string='Ikastetxea',
        required=True,
        ondelete='cascade',
        help='Gela kokatuta dagoen ikastetxea'
    )

    # Erlazionatutako eremua (Related field): Ikastetxearen kodea automatikoki lortzen du
    ikastetxe_izena = fields.Char(
        string='Ikastetxe izena',
        related='ikastetxe_id.kodea',
        store=True,
        readonly=True,
        help='Erlazionatutako ikastetxearen kodea/identifikatzailea'
    )

    def action_erreserbatu(self):
        """Zerrendako 'Erreserbatu' botoia sakatzean exekutatzen den ekintza"""
        self.ensure_one()
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Erreserba'),
                'message': _('%(gela)s gela ondo erreserbatu da!', gela=self.name),
                'type': 'success',
                'sticky': False,
            }
        }

    def action_erreserbatu_wizard(self):
        """Zerrendako 'ErreserbatuWizard' botoia sakatzean exekutatzen den ekintza"""
        self.ensure_one()
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Erreserbatu Wizard'),
                'message': _('%(gela)s gelaren erreserba laguntzailea prestatzen...', gela=self.name),
                'type': 'info',
                'sticky': False,
            }
        }
