# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import fields
from trytond.pyson import Eval
from trytond.pool import PoolMeta

__all__ = ['SaleOpportunity']


class SaleOpportunity:
    __metaclass__ = PoolMeta
    __name__ = "sale.opportunity"
    price_list = fields.Many2One('product.price_list', 'Price List',
        domain=[('company', '=', Eval('company'))],
        states={
            'readonly': Eval('state').in_(['converted', 'lost', 'cancelled']),
            },
        depends=['state', 'company'])

    def on_change_party(self):
        super(SaleOpportunity, self).on_change_party()
        self.price_list = None
        if self.party and self.party.sale_price_list:
            self.price_list = self.party.sale_price_list

    def _get_sale_opportunity(self):
        sale = super(SaleOpportunity, self)._get_sale_opportunity()
        sale.price_list = self.price_list
        return sale
