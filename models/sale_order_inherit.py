from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    _description = "inherit sale order"

    @api.model
    def create(self,vals):
        record = super(SaleOrderInherit, self).create_mo(vals)
        for record in self:
            if self.env['mrp.bom'].search([('product_tmpl_id', '=', record.order_line.product_id.product_tmpl_id.id)]):
                self.env['mrp.production'].write({'bom_id':self.env['mrp.bom'].search([('product_tmpl_id', '=', record.order_line.product_id.product_tmpl_id.id)]).id,
                                                   'product_qty':record.order_line.product_uom_qty,
                                                   'product_id':record.order_line.product_id.id,
                                                   'date_planned_start':datetime.now()})
                                                   
                return record
                # raise ValidationError(_("Product %s already have BoM" % record.order_line.product_id.name))
