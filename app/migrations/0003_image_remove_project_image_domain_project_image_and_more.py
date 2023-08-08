# Generated by Django 4.2.3 on 2023-07-19 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_project_lead_alter_userprofile_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('filepath', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Images',
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AddField(
            model_name='domain',
            name='project_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.image'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.image'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='project_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.image'),
        ),
    ]