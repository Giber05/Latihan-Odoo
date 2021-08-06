from odoo import api, fields, models


class Kelas(models.Model):
    _name = 'kelas.kelas'

    name = fields.Char(string='Daftar orang')
    partner_id = fields.One2many(
        comodel_name='res.partner',
        inverse_name='kelas_id',
        string='Nama',
    )
    wali_kelas = fields.Many2one(
        comodel_name='res.partner',
        string="Wali Kelas",
    )
    matkul_ids = fields.Many2many(
        comodel_name='mata.kuliah', 
        string='Mata Kuliah'
    )
    
