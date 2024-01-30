from odoo import api, fields, models


class ClassDetail(models.Model):
    _name = "class.detail"
    _description = "classDetail"

    name = fields.Char(string="Standard")
    division = fields.Char(string="Division")
    student_ids = fields.One2many("student.info","standard_id",string="Student Detail")
    teacher_ids = fields.Many2many("teacher.detail",string="Teacher")
