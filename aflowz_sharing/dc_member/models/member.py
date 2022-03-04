from odoo import fields, models

class DCMember(models.Model):
    _name = 'dc.member'

    image = fields.Binary()
    name = fields.Char()
    phone = fields.Char(string="Nomor HP")
    email = fields.Char()
    alamat = fields.Text()
    jenis_kelamin = fields.Selection([
        ('pria', "Pria"),
        ('wanita', "Wanita")
    ])
    tanggal_lahir = fields.Date()