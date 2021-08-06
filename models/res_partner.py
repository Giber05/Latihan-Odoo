from odoo import api, fields, models
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(string='Age')
    kelas_id = fields.Many2one(
        comodel_name='kelas.kelas',
        string="Kelas",
    )
    is_dosen = fields.Boolean(string='Dosen')