from odoo import api, models, fields,tools,_

class Inheritance(models.Model):
    _inherit='sale.order'

    customer=fields.Integer(string='Customer')
    note = fields.Text(string='Note')
    total_product = fields.Integer(string='Total Product', compute="_compute_Product_count", store=True)

    # check = fields.(string='Check')
    @api.depends('order_line.product_id')
    def _compute_Product_count(self):
        for rec in self:
            rec.total_product=len(rec.order_line)

    def action_view(self):
        return {
                'type': 'ir.actions.act_window',
                # 'name': 'inheritance',
                'view_mode': 'form',
                'res_model': 'res.partner',
                'res_id': self.partner_id.id,
            }
    # def action_view(self):
    #     print('product')
    def check_view(self):
        print("check")