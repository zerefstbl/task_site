from django.db import models


class Tarefas(models.Model):
    tarefa = models.CharField(max_length=60, blank=True, null=False)
    resenha = models.TextField(max_length=300, blank=True, null=False)
    final = models.BooleanField(
        default=False, verbose_name='Finalizada', blank=True, null=False)
    categoria = models.CharField(
        max_length=6,
        default='L',
        choices=(
            ('L', 'Livre'),
            ('B', 'Livro'),
            ('F', 'Filme'),
        )
    )

    def __str__(self):
        return self.tarefa
