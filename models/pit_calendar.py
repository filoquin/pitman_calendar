from openerp import models, fields, api
from openerp.tools.translate import _


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

    name = fields.Char('Name',compute='_compute_name',store=True)
    start_date = fields.Datetime(required=True)
    end_date = fields.Datetime()
    teacher_id = fields.Many2one('pit.teacher', 'Teacher', required=True , default=_my_teacher)
    asistant_ids = fields.Many2many('pit.teacher',string='asistant')
    group_id = fields.Many2one('pit.school.course.group', 'Group')
    calendar_items_ids = fields.One2many('pit.calendar.item', 'calendar_id', string='Items')
    group_calendar_id = fields.Many2one('pit.school.course.calendar',string='Group Calendar')
    class_number = fields.Integer(string='Class number')
    classroom_id = fields.Many2one('pit.location.classroom','Classroom',related="group_calendar_id.classroom_id",store=True)

    #Attendance
    atte_state = fields.Selection([('draft','draft'),('start','start'),('done','done'),('cancel','cancel')], 'State' , default='draft')
    attendance_line_ids = fields.One2many('pit.calendar.attendance', 'calendar_id',string='Lines')


    active = fields.Boolean('Active', default=True)

    @api.one
    def do_start_attendance(self):
        lines =[]
        for enroll in self.group_id.enrollment_ids :
            if enroll.state == 'active':
                self.env['pit.calendar.attendance'].create({'calendar_id':self.id,'student_id':enroll.student_id.id})
        self.atte_state = 'start'


    @api.depends('start_date','group_id','teacher_id')
    @api.one
    def _compute_name(self):
        self.name = "%s %s %s" % (self.group_id.name, self.start_date ,self.teacher_id.name)


    @api.multi
    def open_atte_register(self):
        self.ensure_one()
        if self.atte_state =="draft":
            self.do_start_attendance()
        view_id = self.env['ir.model.data'].get_object('pitman_calendar','view_pit_attendance_form').id

        view = { 
            'name': _('Attendance register'),
            'view_mode': 'form',
            'view_id': view_id,
            'view_type': 'tree',
            'res_model': 'pit.calendar',
            'res_id': self.id,
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'new',
            'flags': {'action_buttons': True},

        }
        return view
