# -*- coding: utf-8 -*-
from openerp import models, fields

BRANCH = [('1', 'Invertebres'), ('2', 'Vertebres')]

class Animal(models.Model):
    _name = 'zoo.animal'

    name = fields.Char(string=u"Name", required=True)
    branch = fields.Selection(BRANCH, default='2', index=True,)
    gender = fields.Char(string=u"Gender")
