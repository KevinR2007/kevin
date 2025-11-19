from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_zapato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapato',
            name='modelo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='zapato',
            name='marca',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='zapato',
            name='talla',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='zapato',
            name='fecha',
            field=models.DateField(),
        ),
    ]
