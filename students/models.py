from django.db import models


class Student(models.Model):
    """Модель студента"""

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    first_name = models.CharField(max_length=50, verbose_name='Firstname')
    last_name = models.CharField(max_length=50, verbose_name='Lastname')
    patronymic = models.CharField(max_length=50, null=True, verbose_name='Patronymic')
    email = models.EmailField(unique=True, verbose_name='Email')
    study_group = models.ForeignKey(
        to='students.StudyGroup',
        on_delete=models.SET_NULL,
        related_name='students',
        null=True,
        verbose_name='Study group',
    )

    def __str__(self):
        pass


class StudyGroup(models.Model):
    """Модель учебной группы"""

    class Meta:
        verbose_name = 'Study group'
        verbose_name_plural = 'Study groups'

    code = models.CharField(max_length=30, unique=True, verbose_name='Group code')
    direction = models.ForeignKey(
        to='organization.Direction',
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name='Direction',
    )
    monitor = models.OneToOneField(
        to='students.Student',
        on_delete=models.SET_NULL,
        related_name='monitored_group',
        null=True,
        verbose_name='Group monitor',
    )

    def __str__(self):
        pass
