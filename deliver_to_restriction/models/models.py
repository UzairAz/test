from odoo import api, fields, models
from odoo.addons.purchase.models.purchase import PurchaseOrder as Purchase


class ResConfigSettingModel(models.Model):
    _inherit = 'res.users'

    deliver_to = fields.Many2many('stock.picking.type', string='Deliver To')
    default_deliver_to = fields.Many2one('stock.picking.type', string='Default Deliver To',
                                         domain=lambda self: self._get_domain())
    is_readonly = fields.Boolean("Readonly")

    def _get_domain(self):
        return [("id", "in", self.env.user.deliver_to.ids)]


class InheritPurchaseOrder(models.Model):
    _inherit = "purchase.order"

    is_readonly = fields.Boolean("Is Readonly", compute='_get_value')

    @api.depends('picking_type_id')
    def _get_value(self):
        self.is_readonly = self.env.user.is_readonly

    @api.model
    def _default_picking_type(self):
        return self._get_picking_type(self.env.context.get('company_id') or self.env.company.id)

    @api.model
    def _get_picking_type(self, company_id):
        return self.env.user.default_deliver_to.id

    def _get_default(self):
        return self.env.user.deliver_to.id

    def _get_domain(self):
        return [("id", "in", self.env.user.deliver_to.ids)]

    picking_type_id = fields.Many2one('stock.picking.type', 'Deliver To', states=Purchase.READONLY_STATES,
                                      required=True, default=_default_picking_type,
                                      domain=lambda self: self._get_domain(),
                                      help="This will determine operation type of incoming shipment")
