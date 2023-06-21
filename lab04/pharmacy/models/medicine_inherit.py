
# -*- coding: utf-8 -*-

from odoo import models, fields, api



class PharmacyMedicine(models.Model):
    _inhert = 'pharmacy.medicines'
    _description = 'pharmacy medicines'

    name = fields.Image(string='Medicine Image', required=True)
    # image=fields.Binary()
    