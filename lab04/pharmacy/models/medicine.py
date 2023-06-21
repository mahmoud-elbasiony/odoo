
# -*- coding: utf-8 -*-

from odoo import models, fields, api



class PharmacyMedicine(models.Model):
    _name = 'pharmacy.medicines'
    _description = 'pharmacy medicines'

    name = fields.Char(string='Medicine Name', required=True)
    type = fields.Selection(selection=[
        ("Tablet","Tablet"),
        ("Drops","Drops"),
        ("Inhalers","Inhalers"),
        ("Injections","Injections"),
    ],string='Medicine Type', required=True)

    price = fields.Float(string='Price', default=True)
    expiration_date = fields.Date(string='Medicine Expiration Date', required=True)
    stock = fields.Integer(string='Medicine stock', required=True)
    photo = fields.Binary(string='Medicine Image', required=True)

    

 