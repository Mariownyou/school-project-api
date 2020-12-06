# Generated by Django 3.1.3 on 2020-12-06 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Уникальное название связанное с заголовком. Используйте латинские буквы. Пробелы заменяйте "-"', max_length=25, unique=True, verbose_name='уникальное имя')),
                ('title', models.CharField(help_text='Назовите категорию', max_length=200, unique=True, verbose_name='Заголовок')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=25, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Заголовок')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('is_important', models.BooleanField(default=False, help_text='Поставте галочку если хотите отметить это важным', verbose_name='Новость?')),
                ('image', models.ImageField(blank=True, help_text='Картинка украсит ваш пост', null=True, upload_to='posts/img', verbose_name='Картинка')),
                ('video', models.FileField(blank=True, help_text='Добавтье видео', null=True, upload_to='posts/video', verbose_name='Видео')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, help_text='Выберите категорию, если хотите 😉', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.category', verbose_name='Категория')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Напишите ваш коммент ❤', verbose_name='Ваш комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='group',
            field=models.ForeignKey(help_text='Выберите Группу', on_delete=django.db.models.deletion.CASCADE, related_name='category', to='posts.group', verbose_name='Категории'),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'author')},
            },
        ),
    ]
