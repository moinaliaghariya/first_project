from odoo import api, fields, models


class StudentInfo(models.Model):
    _name = "student.info"
    _description = "studentInfo"

    name = fields.Char(string="Name")
    standard_id = fields.Many2one("class.detail" ,string="Standard")
    division = fields.Char(related="standard_id.division" ,string="Division")
    subject1 = fields.Boolean(string="Maths")
    subject2 = fields.Boolean(string="Gujrati")
    subject3 = fields.Boolean(string="Science")
    subject4 = fields.Boolean(string="Hindi")