# -*- coding: utf-8 -*-
from datetime import timedelta
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

    # Erreserben zerrenda eta kopurua
    erreserba_ids = fields.One2many(
        comodel_name='ikastetxeak.erreserba',
        inverse_name='gela_id',
        string='Erreserbak'
    )
    erreserba_kopurua = fields.Integer(
        string='Erreserba kopurua',
        compute='_compute_erreserba_kopurua',
        store=True
    )

    @api.depends('erreserba_ids')
    def _compute_erreserba_kopurua(self):
        for rec in self:
            rec.erreserba_kopurua = len(rec.erreserba_ids)

    def action_erreserbatu(self):
        """Zerrendako 'Erreserbatu' botoia sakatzean zuzenean erreserba bat sortzen du (1 ordukoa)"""
        self.ensure_one()
        now = fields.Datetime.now()
        end = now + timedelta(hours=1)
        erreserba = self.env['ikastetxeak.erreserba'].create({
            'gela_id': self.id,
            'hasiera_data': now,
            'amaiera_data': end,
            'oharrak': f'{self.name} gelaren erreserba azkarra',
            'state': 'baieztatua',
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Gela Erreserbatua!'),
                'message': _('%(gela)s gela ondo erreserbatu da (Kodea: %(kodea)s)!',
                             gela=self.name, kodea=erreserba.name),
                'type': 'success',
                'sticky': False,
            }
        }

    def action_erreserbatu_wizard(self):
        """Zerrendako 'ErreserbatuWizard' botoia sakatzean erreserba morroia irekitzen du"""
        self.ensure_one()
        now = fields.Datetime.now()
        end = now + timedelta(hours=2)
        return {
            'name': _('Erreserbatu: %s') % self.name,
            'type': 'ir.actions.act_window',
            'res_model': 'ikastetxeak.erreserba.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_gela_id': self.id,
                'default_hasiera_data': now,
                'default_amaiera_data': end,
            }
        }

    def action_view_erreserbak(self):
        """Gelaren erreserba guztiak ikusteko ekintza (Stat button)"""
        self.ensure_one()
        return {
            'name': _('Erreserbak: %s') % self.name,
            'type': 'ir.actions.act_window',
            'res_model': 'ikastetxeak.erreserba',
            'view_mode': 'tree,form,calendar',
            'domain': [('gela_id', '=', self.id)],
            'context': {'default_gela_id': self.id},
        }
