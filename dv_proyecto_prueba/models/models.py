# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class dv_proyecto_prueba(models.Model):
#     _name = 'dv_proyecto_prueba.dv_proyecto_prueba'
#     _description = 'dv_proyecto_prueba.dv_proyecto_prueba'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

