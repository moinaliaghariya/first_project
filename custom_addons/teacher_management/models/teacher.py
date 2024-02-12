from odoo import api, fields, models


class TeacherDetail(models.Model):
    _name = "teacher.detail"
    _description = "teacherDetail"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    subject = fields.Char(string="subject")
    class_ids = fields.Many2many("class.detail", string="Class")
    attendance_ids = fields.One2many("hr.detail","teacher_id", string="Attendance")


