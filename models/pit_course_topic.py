from openerp import models, fields, api


class pit_calendar_item(models.Model):
    _name = "pit.school.course.topic"
    _description = "Topic"

    name = fields.Char("Topic")