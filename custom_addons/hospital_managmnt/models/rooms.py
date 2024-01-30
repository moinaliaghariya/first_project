from odoo import api , fields , models

class RoomsDetail(models.Model):
    _name = "rooms.detail"
    _description = "RoomsDetail"
    _rec_name = "room"


    # select_room= fields.Selection([('general_room1','General Room-1'),('general_room2','General Room-2'),('special_Room1','Special Room-1'),('special_Room2','Special Room-2'),('special_Room3','Special Room-3'),('icu1','ICU-1'),('icu2','ICU-2')],string="Select Room")
    # icu = fields.Selection([('icu','ICU'),('picu','PICU'),('surgical icu','Surgical ICU')],string="ICU")
    # special_room = fields.Selection([('room1','Room1'),('room2','Room-2'),('room3','Room-3')],string="Special Room")
    # special = fields.Selection([('room1','Room1'),('room2','Room-2'),('room3','Room-3')],string="Special")

    room = fields.Char(string="Enter Room ")
    amount = fields.Float(string="Enter Amount")
