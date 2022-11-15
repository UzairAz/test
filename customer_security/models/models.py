# -*- coding: utf-8 -*-

from odoo import models, fields, api


class customer_security(models.Model):
    _inherit = 'product.product'

    user_id = fields.Many2one('res.users', string='Users', default=lambda self: self.env.user)


class CustomerSecurity(models.Model):
    _inherit = 'product.template'

    user_id = fields.Many2one('res.users', string='Users', default=lambda self: self.env.user)


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    company_id = fields.Many2one('res.company', string='Company', readonly=True, index=True,
                                 default=lambda self: self.env.company,
                                 help="Company related to this journal")