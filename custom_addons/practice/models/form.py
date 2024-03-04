from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class FormDetail(models.Model):
    _name = "form.detail"
    _description = "FormDetail"

    number = fields.Char(string="Number", default="new")
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    state = fields.Selection([('confirm','confirm'),('done','done'),('cancel','cancel'),('draft','draft')],default="draft")

    @api.model
    def create(self, vals):
        if vals.get('number', _('New')) == _('New'):
            vals['number'] = self.env['ir.sequence'].next_by_code(
                'form.detail') or _('New')
        res = super(FormDetail, self).create(vals)
        return res
    def confirm_detail(self):
        for rec in self:
            if rec.state == 'draft':
                rec.write({'state' : 'confirm'})

    def done_detail(self):
        for rec in self:
            if rec.state == 'confirm':
                rec.write({'state' : 'done'})


    def cancel_detail(self):
        for rec in self:
            if rec.state in ['confirm','done']:
                raise ValidationError('Order must be cancelled or confirmed to reset.')
            rec.write({'state': 'cancel'})

    def draft_detail(self):
        self.state = 'draft'


