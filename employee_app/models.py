from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    name = models.CharField(_('Name of Department'), max_length=255)
    floor = models.IntegerField(_('Floor of the Department'))

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(_('Programming Language'), max_length=255)

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(_('First Name'), max_length=255)
    last_name = models.CharField(_('Last Name'), max_length=255)
    age = models.PositiveSmallIntegerField(_('Age'))
    department = models.ForeignKey('employee_app.Department', verbose_name=_('Department of the employee_app'),
                                   related_name='employees',
                                   on_delete=models.CASCADE)
    programming_language = models.ForeignKey('employee_app.Language', verbose_name=_('Language of the employee_app'),
                                             related_name='employees', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})
