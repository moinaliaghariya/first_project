from odoo import api, fields, models

class HrDetail(models.Model):
    _name = "hr.detail"
    _description = "HrDetail"

    teacher_id = fields.Many2one("teacher.detail" , string="Teacher Name")
    checkedin = fields.Datetime(string="Checked In ")
    checkedout = fields.Datetime(string="Checked Out ")
    total_working_hours = fields.Float(string="Total Working Hour", compute="_compute_worked_hours" ,store=True)

    @api.depends('checkedin','checkedout')
    def _compute_worked_hours(self):
        for rec in self:
            if rec.checkedin and rec.checkedout:
                rec.total_working_hours = (rec.checkedout - rec.checkedin).total_seconds()/3600

            else:
                rec.total_working_hours = 0.0

