# Generated by Django 2.2.6 on 2020-03-20 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('founded', models.CharField(blank=True, max_length=255, null=True)),
                ('legal_person', models.CharField(blank=True, max_length=255, null=True)),
                ('car_model', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'car_logo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EnglishWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=32, null=True)),
                ('word_chinese', models.CharField(blank=True, max_length=255, null=True)),
                ('cixing', models.CharField(max_length=10)),
                ('study_time', models.DateField()),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'english_word',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EngStu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=255, null=True)),
                ('fayin', models.CharField(blank=True, max_length=255, null=True)),
                ('cigen', models.CharField(blank=True, max_length=255, null=True)),
                ('yisi', models.CharField(blank=True, max_length=255, null=True)),
                ('pl', models.CharField(blank=True, db_column='pL', max_length=255, null=True)),
            ],
            options={
                'db_table': 'eng_stu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Idiom',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('spenak', models.CharField(blank=True, max_length=255, null=True)),
                ('meaning', models.CharField(blank=True, max_length=255, null=True)),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('example', models.CharField(blank=True, max_length=255, null=True)),
                ('hot', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'idiom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('round_num', models.IntegerField()),
            ],
            options={
                'db_table': 'rank',
                'managed': False,
            },
        ),
    ]
