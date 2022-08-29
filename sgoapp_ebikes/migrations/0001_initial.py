# Generated by Django 3.2.3 on 2021-05-29 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=40)),
                ('shop_address', models.CharField(max_length=40)),
                ('dealer_type', models.CharField(choices=[('ONLINE', 'ONLINE'), ('OFFLINE', 'OFFLINE')], max_length=40)),
                ('profile_pic1', models.ImageField(blank=True, null=True, upload_to='profile_pic/dealerProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Speedometer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.IntegerField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='shopnames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopnames', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgoapp_ebikes.dealer')),
            ],
        ),
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BPercentage', models.CharField(max_length=3)),
                ('RTime', models.TextField(max_length=20)),
                ('KmsRide', models.IntegerField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LockUnlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=4)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='kilometers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('Ridekm', models.CharField(max_length=20)),
                ('useCharge', models.CharField(max_length=25)),
                ('BalCharge', models.CharField(max_length=20)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='estimatekms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BPercentage', models.CharField(max_length=3)),
                ('KmsRide', models.IntegerField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/CustomerProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('pincode', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='bookbike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('bikename', models.CharField(choices=[('TVS Jupiter', 'TVS Jupiter'), ('Hero HF Deluxe', 'Hero HF Deluxe'), ('Yamaha YZF R15 V3', 'Yamaha YZF R15 V3'), ('Bajaj Pulsar NS 125', 'Bajaj Pulsar NS 125'), ('Hero Splendor Plus', 'Hero Splendor Plus'), ('Yamaha MT-15', 'Yamaha MT-15'), ('Royal Enfield Classic 350', 'Royal Enfield Classic 350'), ('TVS Apache RTR 160', 'TVS Apache RTR 160'), ('Royal Enfield Bullet 350', 'Royal Enfield Bullet 350'), ('Bajaj Pulsar 150', 'Bajaj Pulsar 150'), ('Bajaj Pulsar NS200', 'Bajaj Pulsar NS200'), ('TVS Apache RTR 160 4V', 'TVS Apache RTR 160 4V'), ('Hero HF Deluxe', 'Hero HF Deluxe'), ('2021 Suzuki Hayabusa', '2021 Suzuki Hayabusa'), ('TVS Apache RR 310', 'TVS Apache RR 310'), ('TVS Apache RTR 200 4V', 'TVS Apache RTR 200 4V')], default=None, max_length=100)),
                ('amount', models.CharField(choices=[('TVS Jupiter', (('64437', '64437'), (12, '64437'), (13, 'Taxes'))), ('Hero HF Deluxe', (('38900', '38900'), ('63175', '63175'))), ('Yamaha YZF R15 V3', (('141000', '141000'), ('158000', '158000'))), ('Hero Splendor Plus', (('49990 ', '49990 '), ('68560', '68560'), ('59870', '59870'))), ('Yamaha MT-15', (('140000', '140000'), ('141000', '141000'))), ('Royal Enfield Classic 350', (('152000', '152000'), ('200000', '200000'), ('217000', '217000'))), ('TVS Apache RTR 160', (('103000', '103000'), ('106000', '106000')))], default=None, max_length=100)),
                ('order_id', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('dealer_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sgoapp_ebikes.shopnames')),
            ],
        ),
        migrations.CreateModel(
            name='Bikesales',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=50, null=True)),
                ('sales_per_day', models.IntegerField()),
                ('total_sales', models.IntegerField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sgoapp_ebikes.cust')),
            ],
        ),
        migrations.CreateModel(
            name='bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headlight', models.CharField(choices=[('Working', '1'), ('Not Working', '0')], default=1, max_length=11)),
                ('signal_light', models.CharField(choices=[('Working', '1'), ('Not Working', '0')], default=1, max_length=11)),
                ('breaks', models.CharField(choices=[('Working', '1'), ('Not Working', '0')], default=1, max_length=11)),
                ('motor_working', models.CharField(choices=[('Working', '1'), ('Not Working', '0')], default=1, max_length=11)),
                ('key', models.CharField(choices=[('Working', '1'), ('Not Working', '0')], default=1, max_length=11)),
                ('body_status', models.CharField(choices=[('Working', '1'), ('Not Working', '0')], default=1, max_length=11)),
                ('usb_status', models.CharField(choices=[('Working', '1'), ('Not Working', '0')], default=1, max_length=11)),
                ('battery', models.CharField(choices=[('Working', '1'), ('Not Working', '0')], default=1, max_length=11)),
                ('controller', models.CharField(choices=[('Working', '1'), ('Not Working', '0')], default=1, max_length=11)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Battery_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charging_state', models.BooleanField()),
                ('battery_level', models.PositiveIntegerField()),
                ('dischrging_time', models.TimeField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
