# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class pitman_calendar(models.Model):
#     _name = 'pitman_calendar.pitman_calendar'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100