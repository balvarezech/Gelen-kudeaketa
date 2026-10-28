# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ErreserbaWizard(models.TransientModel):
    _name = 'ikastetxeak.erreserba.wizard'
    _description = 'Gela Erreserbatzeko Morroia (Wizard)'

    gela_id = fields.Many2one(
        comodel_name='ikastetxeak.gela',
        string='Gela',
        required=True,
        readonly=True
    )
    ikastetxe_id = fields.Many2one(
        comodel_name='ikastetxeak.ikastetxea',
        string='Ikastetxea',
        related='gela_id.ikastetxe_id',
        readonly=True
    )
    erabiltzaile_id = fields.Many2one(
        comodel_name='res.users',
        string='Erabiltzailea',
        default=lambda self: self.env.user,
        required=True
    )
    hasiera_data = fields.Datetime(
        string='Hasiera data',
        required=True,
        default=fields.Datetime.now
    )
    amaiera_data = fields.Datetime(
        string='Amaiera data',
        required=True
    )
    oharrak = fields.Text(
        string='Erreserbaren azalpena / Oharrak'
    )

    @api.constrains('hasiera_data', 'amaiera_data')
    def _check_dates(self):
        for rec in self:
            if rec.hasiera_data and rec.amaiera_data and rec.hasiera_data >= rec.amaiera_data:
                raise ValidationError(_('Amaiera-datak hasiera-dataren ondorengoa izan behar du!'))

    def action_erreserbatu(self):
        """Morroiaren bidez erreserba berria sortu"""
        self.ensure_one()
        erreserba = self.env['ikastetxeak.erreserba'].create({
            'gela_id': self.gela_id.id,
            'erabiltzaile_id': self.erabiltzaile_id.id,
            'hasiera_data': self.hasiera_data,
            'amaiera_data': self.amaiera_data,
            'oharrak': self.oharrak,
            'state': 'baieztatua',
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Erreserba Burutua!'),
                'message': _('%(gela)s gela ondo erreserbatu da (Kodea: %(kodea)s)!',
                             gela=self.gela_id.name, kodea=erreserba.name),
                'type': 'success',
                'sticky': False,
            }
        }
