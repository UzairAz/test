from odoo import api, fields, models
from odoo.addons.purchase.models.purchase import PurchaseOrder as Purchase


class ResConfigSettingModel(models.Model):
    _inherit = 'res.users'

    deliver_to = fields.Many2many('stock.picking.type', string='Deliver To')


class InheritPurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def _default_picking_type(self):
        return self._get_picking_type(self.env.context.get('company_id') or self.env.company.id)

    def _get_domain(self):
        return [("id", "in", self.env.user.deliver_to.ids)]

    picking_type_id = fields.Many2one('stock.picking.type', 'Deliver To', states=Purchase.READONLY_STATES,
                                      required=True, default=_default_picking_type,
                                      domain=lambda self: self._get_domain(),
                                      help="This will determine operation type of incoming shipment")
