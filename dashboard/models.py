from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

ICYICIRO = (
    ('', 'Choose...'),
    ('one', '1'),
    ('two', '2'),
    ('three', '3')
)


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class District(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_sectors')

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"

    def __str__(self):
        return self.name


###################################

class Department(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class Cell(models.Model):
    name = models.CharField(max_length=200)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cell'
        verbose_name_plural = 'Cells'

    def __str__(self):
        return self.name


class Village(models.Model):
    name = models.CharField(max_length=200)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Village'
        verbose_name_plural = 'Villages'

    def __str__(self):
        return self.name


class KPI(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "KPI"
        verbose_name_plural = "KPIs"
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique')
        ]

    def __str__(self):
        return self.name


#-------------------------- snipets for validating indangamuntu field in umuryango model ---------------------------#3

#######################################################################################################################


class Umuryango(models.Model):
    PENDING = 0
    ACHIEVED = 1
    R_CHOICES = (
        (PENDING, 0), (ACHIEVED, 1))

    TARGET = 1
    R1_CHOICES = ((TARGET, 1), (TARGET, 1))

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    IKICIRO = ((ONE, 1), (TWO, 2), (THREE, 3), (FOUR, 4))

    name = models.CharField(max_length=200)
    number_of_member = models.PositiveIntegerField()
    icyiciro = models.PositiveIntegerField(choices=IKICIRO)
    irangamuntu = models.CharField(max_length=16)
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE, default=None, related_name='kpi_name')
    target = models.PositiveSmallIntegerField(choices=R1_CHOICES, default=1)
    achieved = models.PositiveSmallIntegerField(choices=R_CHOICES, default=0)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='village_cell')
    image = models.FileField(upload_to='progress', default='default.png')

    def __str__(self):
        return self.name

    def clean(self):
        if len(self.irangamuntu) < 16:
            raise ValidationError('Indangamuntu you entered is less than 16')


