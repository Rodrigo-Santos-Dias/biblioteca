# Generated by Django 4.1 on 2022-08-30 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0009_remove_livros_data_devolucao_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empresrimos',
        ),
    ]
