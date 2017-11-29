from openerp import models, fields, api


class pit_calendar(models.Model):
    _name = "pit.calendar"
    _description = "Calendar"

    start_date = fields.Date()
    end_date = fields.Date()
    teacher_id = fields.Many2one('pit.teacher', 'Teacher', required=True)
    group_id = fields.Many2one('pit.school.course.group', 'Group')
    calendar_items_ids = fields.One2many('pit.calendar.item', 'calendar_id', string='Items')