# Generated by Django 4.1 on 2022-08-30 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0008_livros_usuario_categoria_livros_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='data_devolucao',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='data_emprestimo',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='nome_emprestado',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='tempo_durcao',
        ),
        migrations.CreateModel(
            name='Empresrimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_emprestado', models.CharField(blank=True, max_length=30)),
                ('data_emprestimo', models.DateTimeField(blank=True, null=True)),
                ('data_devolucao', models.DateTimeField(blank=True, null=True)),
                ('tempo_durcao', models.DateField(blank=True, null=True)),
                ('livros', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livros')),
            ],
        ),
    ]