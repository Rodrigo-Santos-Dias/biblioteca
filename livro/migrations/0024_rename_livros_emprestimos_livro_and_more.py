# Generated by Django 4.1 on 2022-10-20 00:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0023_rename_livro_emprestimos_livros_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimos',
            old_name='livros',
            new_name='livro',
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 21, 28, 46, 649349)),
        ),
    ]
