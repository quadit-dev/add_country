
from odoo import fields, models, _



class res_partner(models.Model):
    _name='res.partner'
    inherit='res.partner'


	country_id = fields.Many2one('res.partner', string='Country')

