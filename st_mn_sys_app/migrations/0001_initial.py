# Generated by Django 5.0 on 2024-01-07 04:09

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='lop',
            fields=[
                ('malop', models.AutoField(primary_key=True, serialize=False)),
                ('tenlop', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='monHoc',
            fields=[
                ('mamonhoc', models.AutoField(primary_key=True, serialize=False)),
                ('tenmonhoc', models.CharField(max_length=255)),
                ('sotiet', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='nguoiDung',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mand', models.AutoField(primary_key=True, serialize=False)),
                ('hovaten', models.CharField(max_length=255)),
                ('ngaysinh', models.DateField(default=datetime.date(1970, 1, 1))),
                ('gioitinh', models.CharField(max_length=255)),
                ('diachi', models.CharField(max_length=255)),
                ('cccd', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('sdt', models.CharField(max_length=255)),
                ('ngaybatdau', models.DateField(default=datetime.date(1970, 1, 1))),
                ('user_type', models.CharField(choices=[(1, 'admin'), (2, 'nhanVien'), (3, 'giaoVien')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='hocSinh',
            fields=[
                ('mahs', models.AutoField(primary_key=True, serialize=False)),
                ('hovaten', models.CharField(max_length=255)),
                ('ngaysinh', models.DateField()),
                ('gioitinh', models.CharField(max_length=255)),
                ('diachi', models.CharField(max_length=255)),
                ('tenbo', models.CharField(max_length=255)),
                ('sdtbo', models.CharField(max_length=255)),
                ('emailbo', models.CharField(max_length=255)),
                ('tenme', models.CharField(max_length=255)),
                ('sdtme', models.CharField(max_length=255)),
                ('emailme', models.CharField(max_length=255)),
                ('malop', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='st_mn_sys_app.lop')),
            ],
        ),
        migrations.CreateModel(
            name='giaoVien',
            fields=[
                ('magv', models.AutoField(primary_key=True, serialize=False)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('malop', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='st_mn_sys_app.lop')),
                ('mamonhoc', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='st_mn_sys_app.monhoc')),
            ],
        ),
        migrations.CreateModel(
            name='diem',
            fields=[
                ('maxulydiem', models.AutoField(primary_key=True, serialize=False)),
                ('mucdatduoc', models.CharField(max_length=10)),
                ('diem', models.FloatField()),
                ('mahs', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='st_mn_sys_app.hocsinh')),
                ('mamonhoc', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='st_mn_sys_app.monhoc')),
            ],
        ),
        migrations.CreateModel(
            name='nhanVien',
            fields=[
                ('manv', models.AutoField(primary_key=True, serialize=False)),
                ('vitri', models.CharField(max_length=255)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
