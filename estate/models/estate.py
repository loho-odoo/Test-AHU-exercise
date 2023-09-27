from odoo import models, fields

class Estate(models.Model):
    _name= "estate"
    _description= "Estate"

    name = fields.Char(default="Unknown")
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    number_of_bedrooms=fields.Integer(default=2)

