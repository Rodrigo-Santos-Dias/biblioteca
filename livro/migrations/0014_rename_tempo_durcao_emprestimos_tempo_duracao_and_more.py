# Generated by Django 4.1 on 2022-08-30 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0013_alter_emprestimos_nome_emprestado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimos',
            old_name='tempo_durcao',
            new_name='tempo_duracao',
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
    ]