from odoo import api, fields, models, tools, _


class ProductDetail(models.Model):
    _name = "product.name"
    _description = "ProductDeatail"
    # _rec_name="name"


    name = fields.Char(string="Product Name")