from openerp import models, fields, api


class pit_calendar_item(models.Model):
    _name = "pit.calendar.item"
    _description = "Calendar Item"
    calendar_id = fields.Many2one('pit.calendar', 'Calendar')
    topic_id = fields.Many2one('pit.school.course.topic', 'Topic')
    material_id = fields.Many2one('pit.calendar.material', 'Material')
