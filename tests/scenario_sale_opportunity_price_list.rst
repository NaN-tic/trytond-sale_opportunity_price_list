====================================
Sale Opportunity Price List Scenario
====================================

Imports::

    >>> from proteus import config, Model, Wizard

Create a database::

    >>> config = config.set_trytond()
    >>> config.pool.test = True

Install sale_opportunity_price_list::

    >>> Module = Model.get('ir.module')
    >>> module, = Module.find([
    ...         ('name', '=', 'sale_opportunity_price_list'),
    ...         ])
    >>> Wizard('ir.module.install_upgrade').execute('upgrade')
