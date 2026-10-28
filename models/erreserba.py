# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Erreserba(models.Model):
    _name = 'ikastetxeak.erreserba'
    _description = 'Gelaren Erreserba'
    _order = 'hasiera_data desc, id desc'

    name = fields.Char(
        string='Erreserba kodea',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('Berria')
    )
    gela_id = fields.Many2one(
        comodel_name='ikastetxeak.gela',
        string='Gela',
        required=True,
        ondelete='cascade',
        help='Erreserbatzen den gela'
    )
    ikastetxe_id = fields.Many2one(
        comodel_name='ikastetxeak.ikastetxea',
        string='Ikastetxea',
        related='gela_id.ikastetxe_id',
        store=True,
        readonly=True,
        help='Gelari dagokion ikastetxea'
    )
    erabiltzaile_id = fields.Many2one(
        comodel_name='res.users',
        string='Erabiltzailea',
        default=lambda self: self.env.user,
        required=True,
        help='Erreserba egin duen erabiltzailea'
    )
    hasiera_data = fields.Datetime(
        string='Hasiera data',
        required=True,
        default=fields.Datetime.now,
        help='Erreserbaren hasiera-ordua'
    )
    amaiera_data = fields.Datetime(
        string='Amaiera data',
        required=True,
        help='Erreserbaren amaiera-ordua'
    )
    oharrak = fields.Text(
        string='Oharrak / Arrazoia',
        help='Erreserbaren xedea edo xehetasunak'
    )
    state = fields.Selection([
        ('zirriborroa', 'Zirriborroa'),
        ('baieztatua', 'Baieztatua'),
        ('baliogabetua', 'Baliogabetua')
    ], string='Egoera', default='baieztatua', required=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals.get('name') == _('Berria'):
                vals['name'] = self.env['ir.sequence'].next_by_code('ikastetxeak.erreserba') or f"ERR-{fields.Datetime.now().strftime('%Y%m%d-%H%M%S')}"
        return super().create(vals_list)

    @api.constrains('hasiera_data', 'amaiera_data')
    def _check_dates(self):
        for rec in self:
            if rec.hasiera_data and rec.amaiera_data and rec.hasiera_data >= rec.amaiera_data:
                raise ValidationError(_('Amaiera-datak hasiera-dataren ondorengoa izan behar du!'))

    def action_baieztatu(self):
        self.write({'state': 'baieztatua'})

    def action_baliogabetu(self):
        self.write({'state': 'baliogabetua'})

    def action_zirriborroa(self):
        self.write({'state': 'zirriborroa'})
