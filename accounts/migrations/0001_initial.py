# Generated by Django 4.0.6 on 2022-08-28 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='이메일')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('username', models.CharField(max_length=20, verbose_name='이름')),
                ('mobile', models.CharField(max_length=20, verbose_name='휴대폰 번호')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일자')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일자')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
