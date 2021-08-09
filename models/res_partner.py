from odoo import api, fields, models
from odoo.exceptions import UserError
from datetime import date


class ResPartner(models.Model):
    _inherit = 'res.partner'

    tanggal_lahir = fields.Date(string='Tanggal Masuk',default=fields.Date.today(),)
    age = fields.Integer(
        string='Age',
        compute='_compute_age',
        inverse='_inverse_age',
        search='_search_age',
        readonly=True,
        store=False,
        compute_sudo = True,
    )
    kelas_id = fields.Many2one(
        comodel_name='kelas.kelas',
        string="Kelas",
    )
    is_dosen = fields.Boolean(string='Dosen')


    @api.depends('tanggal_lahir')
    def _compute_age(self):
        delta = date.today()- self.tanggal_lahir
        self.age = delta.days/365

    @api.constrains('tanggal_lahir')
    def check_tanggal_lahir(self):
        if self.tanggal_lahir> date.today():
            raise models.ValidationError("Tanggal lahir harus berasal dari masalalu")
    
    
