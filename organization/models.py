from django.db import models


class Direction(models.Model):
    """Модель направления обучения"""

    class Meta:
        verbose_name = 'Direction'
        verbose_name_plural = 'Directions'

    name = models.CharField(max_length=300, unique=True, verbose_name='Direction name')
    curator = models.ForeignKey(
        to='users.User',
        on_delete=models.SET_NULL,
        related_name='directions',
        null=True,
        verbose_name='Curator',
    )
    disciplines = models.ManyToManyField(
        to='organization.Discipline',
        through='organization.DirectionDiscipline',
        through_fields=('direction', 'discipline'),
        related_name='directions',
        verbose_name='Disciplines'
    )

    def __str__(self):
        return self.name


class Discipline(models.Model):
    """Модель дисциплины"""

    class Meta:
        verbose_name = 'Discipline'
        verbose_name_plural = 'Disciplines'

    name = models.CharField(max_length=300, unique=True, verbose_name='Discipline name')

    def __str__(self):
        return self.name


class DirectionDiscipline(models.Model):
    """Модель связи многие-ко-многим Направлений и Дисциплин"""

    class Meta:
        verbose_name = 'Direction discipline'
        verbose_name_plural = 'Direction disciplines'
        unique_together = ['direction', 'discipline', 'semester']

    direction = models.ForeignKey(
        to='organization.Direction',
        on_delete=models.CASCADE,
        related_name='direction_disciplines',
        verbose_name='Direction',
    )
    discipline = models.ForeignKey(
        to='organization.Discipline',
        on_delete=models.CASCADE,
        related_name='direction_disciplines',
        verbose_name='Discipline',
    )
    semester = models.PositiveIntegerField(null=True, verbose_name='Semester number')
    hours_number = models.PositiveIntegerField(null=True, verbose_name='Hours number')
    # zchet_ili_examen = None    # TODO

    def __str__(self):
        return f'{self.direction}:{self.semester}:{self.discipline}'
