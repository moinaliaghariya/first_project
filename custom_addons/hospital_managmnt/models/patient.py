from odoo import api, fields, models


class PatientDetail(models.Model):
    _name = "patient.detail"
    _description = "PatientDetail"
    _rec_name = "name"

    name = fields.Char(string="Name")
    gender = fields.Selection( string="Gender",related='select_doctor.gender',)
    ref = fields.Char(string="Reference")
    age = fields.Integer(string="Age")
    blood_group = fields.Selection(
        [('a+', 'A+'), ('b+', 'B+'), ('o+', 'O+'), ('o-', 'O-'), ('ab+', 'AB+'), ('ab-', 'AB-')], string="Blood Group")
    mobile_no = fields.Char(string="Mobile No")
    address = fields.Char(string="Address")
    select_doctor = fields.Many2one('doctor.detail', string="Select Doctor")
    select_room_id = fields.Many2one('rooms.detail', string="Select Room")
    amount = fields.Float(related="select_room_id.amount", string="Amount")
    days = fields.Integer(string="Days")
    total_amount = fields.Integer(string="Total Amount", compute="_compute_total_days_bill")

    @api.depends('amount','days')
    def _compute_total_days_bill(self):
        for x in self:
            if x.amount and x.days:
                x.total_amount = (x.amount * x.days)
            else:
                x.total_amount = False


    @api.onchange('select_doctor')
    def onchange_select_doctor(self):
        self.ref =self.select_doctor.ref

    def obj_test(self):
        print("Button Clicked")