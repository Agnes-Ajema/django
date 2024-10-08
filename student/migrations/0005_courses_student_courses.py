# Generated by Django 5.0.7 on 2024-08-08 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_rename_bio_student_student_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='student.courses'),
        ),
    ]
