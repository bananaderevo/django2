from django.db import models


class Logs(models.Model):
    path = models.CharField(max_length=255, verbose_name='path')
    method = models.CharField(max_length=255, verbose_name='method')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='timestamp')

    def __str__(self):
        return self.path

    class Meta:
        verbose_name = 'Логи'
        verbose_name_plural = 'Логи'
        ordering = ['path', 'method']
