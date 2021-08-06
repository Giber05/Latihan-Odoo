from odoo import api, fields, models


class MataKuliah(models.Model):
    _name = 'mata.kuliah'

    name = fields.Char(string='Nama Matkul')
    kode = fields.Char(string='Kode Matkul')
    kelas_ids = fields.Many2many(
        comodel_name='kelas.kelas', 
        string='Kelas'
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Dosen Pengampu",
        domain=[("is_dosen", "=", True)],
    )

    
    
    
