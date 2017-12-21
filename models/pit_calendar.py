from openerp import models, fields, api


class pit_calendar(models.Model):
    _name = "pit.calendar"
    _description = "Calendar"

    def _my_teacher(self):

        my_teacher = self.env['res.users'].browse(self._uid)
        print my_teacher.partner_id.is_teacher
        if my_teacher.partner_id.is_teacher:
            teacher = self.env['pit.teacher'].search([('partner_id', '=', my_teacher.partner_id.id)], limit=1)
            return teacher.id
        else:
            return False

    name = fields.Char('Name',compute='compute_name',store=True)
    start_date = fields.Datetime(required=True)
    end_date = fields.Datetime()
    teacher_id = fields.Many2one('pit.teacher', 'Teacher', required=True , default=_my_teacher)
    group_id = fields.Many2one('pit.school.course.group', 'Group')
    calendar_items_ids = fields.One2many('pit.calendar.item', 'calendar_id', string='Items')
    group_calendar_id = fields.Many2one('pit.school.course.calendar',string='Group Calendar')
    class_number = fields.Integer(string='Class number')
    classroom_id = fields.Many2one('pit.location.classroom','Classroom',related="group_calendar_id.classroom_id",store=True)


    @api.depends('start_date','group_id','teacher_id')
    @api.one
    def _compute_name(self):
        self.name = "%s %s %s" % (self.start_date ,self.teacher_id.name, self.group_id.name)
