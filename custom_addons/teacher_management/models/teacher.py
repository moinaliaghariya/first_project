from odoo import api, fields, models


class TeacherDetail(models.Model):
    _name = "teacher.detail"
    _description = "teacherDetail"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    class_ids = fields.Many2many("class.detail", string="Class")
    # t_present = fields.One2many("hr.detail","teacher_id",string="T present")
    # teacher_present = fields.Boolean(string="Teacher present", compute="_compute_teacher_present")



    # # @api.depends('checkedin')
    # def _compute_teacher_present(self):
    #     for record in self:
    #         if record.checkedin:
    #             record.teacher_present=True
    #         else:
    #             record.teacher_present=False
    #








