from odoo import api, fields, models, tools, _


class CustomerDtail(models.Model):
    _name = "customer.name"
    _description = "CustomerDtail"

    first_name = fields.Char(string="First Name", store = True)
    middle_name=fields.Char(string="Middle Name")
    product_id = fields.Many2one('product.name',string="Product")
    last_name = fields.Char(string="Last Name")
    birth_date = fields.Date(string="Birth Date")
    address = fields.Text(string="Adress" ,)
    phone_no = fields.Integer(string="Phone No.")
    email = fields.Char(string="Email Id")
    blood_group = fields.Selection([('a','A'),('b','B'),('a+', 'A+'), ('b+', 'B+'), ('ab+', 'AB+'), ('ab-', 'AB-')],
                                   string='Blood Group')
    status = fields.Selection([('married', 'married'), ('single', 'single')], string="Status")
    Image = fields.Binary(string='upload Image', store=True, attachment=True)
