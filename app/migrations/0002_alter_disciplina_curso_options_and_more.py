# Generated by Django 5.0.3 on 2024-04-02 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disciplina_curso',
            options={'verbose_name': 'Disciplina por Curso', 'verbose_name_plural': 'Disciplinas por Cursos'},
        ),
        migrations.AlterModelOptions(
            name='tipos_avaliacao',
            options={'verbose_name': 'Tipo de Avaliação', 'verbose_name_plural': 'Tipos de Avaliações'},
        ),
    ]