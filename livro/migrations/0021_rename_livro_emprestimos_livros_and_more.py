# Generated by Django 4.1 on 2022-09-24 02:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0020_rename_livros_emprestimos_livro_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimos',
            old_name='livro',
            new_name='livros',
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 23, 23, 48, 23, 75098)),
        ),
    ]
