from odoo import models, fields

class DCStockiest(models.Model):
    _name = 'dc.stockiest'

    jenis_barang = fields.Char()
    tipe = fields.Char()
    jumlah = fields.Integer()
    kadaluarsa = fields.Date()