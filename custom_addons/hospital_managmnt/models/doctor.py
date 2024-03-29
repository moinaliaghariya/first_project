from datetime import date
from odoo import api, models, fields


class DoctorDetail(models.Model):
    _name = "doctor.detail"
    _description = "DoctorDetail"
    _rec_name = "specialist"

    name = fields.Char(string="Name")
    ref = fields.Char(string="Reference")
    specialist = fields.Selection([('mbbs', 'MBBS'), ('md', 'MD'), ('sergen', 'Sergen')], string="Specialist")
    birth_date = fields.Date(string="Birth Date")
    age = fields.Integer(string="Age", compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority')
    salary = fields.Float(string="Salary")
    bonus = fields.Float(string="Bonus")
    total_salary = fields.Float(string="Total salary")

    def doctor_salary(self):
        for rec in self:
            rec.total_salary = rec.salary + rec.bonus

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year
            else:
                rec.age = 0
            # return (today.year - rec.birth_date.year)
            #         # - ((today.month, today.day) < (rec.birth_date.month, rec.birth_date.day)))
