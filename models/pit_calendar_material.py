from openerp import models, fields, api


class pit_calendar_material(models.Model):
    _name = "pit.calendar.material"
    _description = "Material"

    name = fields.Char('Material')