from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    _description = "inherit sale order"

    def create_mo(self):
        for record in self:
            if self.env['mrp.bom'].search([('product_tmpl_id', '=', record.product_id.product_tmpl_id.id)]):
                raise ValidationError(_("Product %s already have BoM" % record.product_id.name))
