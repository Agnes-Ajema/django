# Generated by Django 5.0.7 on 2024-07-29 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_rename_code_student_student_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='bio',
            new_name='student_bio',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='student_email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='grade_level',
            new_name='student_locker',
        ),
        migrations.RemoveField(
            model_name='student',
            name='country',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gurdian_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_national_id_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_next_of_kin',
        ),
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.CharField(default=0, max_length=40),
        ),
        migrations.AddField(
            model_name='student',
            name='student_guardian',
            field=models.CharField(default=0, max_length=40),
        ),
        migrations.AddField(
            model_name='student',
            name='student_mentor',
            field=models.CharField(default=0, max_length=40),
        ),
        migrations.AddField(
            model_name='student',
            name='student_name',
            field=models.CharField(default='Ajema', max_length=40),
        ),
        migrations.AddField(
            model_name='student',
            name='student_nationality',
            field=models.CharField(default='Kenya', max_length=25),
        ),
    ]
