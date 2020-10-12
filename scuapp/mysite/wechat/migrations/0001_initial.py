# Generated by Django 3.1.1 on 2020-10-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tbapplication',
            fields=[
                ('ap_number', models.CharField(db_column='AP_Number', max_length=10, primary_key=True, serialize=False)),
                ('ap_reson', models.TextField(blank=True, db_column='AP_Reson', null=True)),
                ('ap_time', models.DateTimeField(db_column='AP_Time')),
                ('ap_abletime', models.CharField(blank=True, db_column='AP_AbleTime', max_length=60, null=True)),
            ],
            options={
                'db_table': 'tbapplication',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbcompany',
            fields=[
                ('com_number', models.CharField(db_column='Com_Number', max_length=10, primary_key=True, serialize=False)),
                ('phone_num', models.CharField(blank=True, db_column='Phone_Num', max_length=11, null=True)),
                ('password', models.CharField(db_column='Password', max_length=20)),
                ('com_name', models.CharField(db_column='Com_Name', max_length=60)),
                ('com_leader', models.CharField(db_column='Com_Leader', max_length=20)),
                ('e_mail', models.CharField(blank=True, db_column='E_mail', max_length=60, null=True)),
                ('com_address', models.CharField(db_column='Com_Address', max_length=60)),
            ],
            options={
                'db_table': 'tbcompany',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbfeedbackEr',
            fields=[
                ('fbe_number', models.CharField(db_column='Fbe_Number', max_length=10, primary_key=True, serialize=False)),
                ('fb_content', models.CharField(blank=True, db_column='Fb_Content', max_length=200, null=True)),
                ('fb_time', models.DateTimeField(db_column='Fb_Time')),
            ],
            options={
                'db_table': 'tbfeedback_er',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbfeedbackStu',
            fields=[
                ('fbs_number', models.CharField(db_column='Fbs_Number', max_length=10, primary_key=True, serialize=False)),
                ('fb_content', models.CharField(blank=True, db_column='Fb_Content', max_length=200, null=True)),
                ('fb_time', models.DateTimeField(db_column='Fb_Time')),
            ],
            options={
                'db_table': 'tbfeedback_stu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbinResult',
            fields=[
                ('inr_number', models.CharField(db_column='Inr_Number', max_length=10, primary_key=True, serialize=False)),
                ('inr_phonenum', models.CharField(db_column='Inr_Phonenum', max_length=11)),
                ('r_time', models.CharField(db_column='R_Time', max_length=60)),
                ('result', models.CharField(db_column='Result', max_length=60)),
                ('r_ps', models.CharField(blank=True, db_column='R_Ps', max_length=200, null=True)),
                ('in_r_time', models.DateTimeField(db_column='In_R_Time')),
            ],
            options={
                'db_table': 'tbin_result',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbinterviewApply',
            fields=[
                ('ia_number', models.CharField(db_column='IA_Number', max_length=10, primary_key=True, serialize=False)),
                ('ia_time', models.CharField(blank=True, db_column='IA_Time', max_length=60, null=True)),
                ('ia_name', models.CharField(blank=True, db_column='IA_Name', max_length=20, null=True)),
                ('phonenumber', models.CharField(db_column='PhoneNumber', max_length=12)),
                ('a_time', models.DateTimeField(db_column='A_Time')),
            ],
            options={
                'db_table': 'tbinterview_apply',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbinterviewNotice',
            fields=[
                ('i_number', models.CharField(db_column='I_Number', max_length=10, primary_key=True, serialize=False)),
                ('i_address', models.CharField(blank=True, db_column='I_Address', max_length=60, null=True)),
                ('i_time', models.DateTimeField(db_column='I_Time')),
            ],
            options={
                'db_table': 'tbinterview_notice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbinterviewResult',
            fields=[
                ('ir_number', models.CharField(db_column='IR_Number', max_length=10, primary_key=True, serialize=False)),
                ('ir_rtime', models.CharField(db_column='IR_Rtime', max_length=60)),
                ('ir_result', models.CharField(db_column='IR_Result', max_length=60)),
                ('ir_ps', models.CharField(blank=True, db_column='IR_Ps', max_length=200, null=True)),
                ('ir_time', models.DateTimeField(db_column='IR_Time')),
            ],
            options={
                'db_table': 'tbinterview_result',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbinWork',
            fields=[
                ('iw_number', models.CharField(db_column='IW_Number', max_length=10, primary_key=True, serialize=False)),
                ('iw_post', models.CharField(db_column='IW_Post', max_length=60)),
                ('iw_depart', models.CharField(db_column='IW_depart', max_length=60)),
                ('w_time', models.CharField(blank=True, db_column='W_Time', max_length=60, null=True)),
                ('w_place', models.CharField(blank=True, db_column='W_Place', max_length=60, null=True)),
                ('work', models.CharField(db_column='Work', max_length=200)),
                ('w_salary', models.CharField(blank=True, db_column='W_Salary', max_length=20, null=True)),
                ('w_reuire', models.CharField(blank=True, db_column='W_Reuire', max_length=200, null=True)),
                ('w_amount', models.CharField(blank=True, db_column='W_Amount', max_length=50, null=True)),
                ('ddl_time', models.DateTimeField(db_column='Ddl_Time')),
                ('inpub_time', models.DateTimeField(db_column='Inpub_time')),
                ('w_ps', models.CharField(blank=True, db_column='W_Ps', max_length=200, null=True)),
            ],
            options={
                'db_table': 'tbin_work',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbmanager',
            fields=[
                ('manager_id', models.CharField(db_column='Manager_ID', max_length=9, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=20)),
                ('phonenumber', models.CharField(db_column='PhoneNumber', max_length=12)),
                ('password', models.CharField(db_column='Password', max_length=20)),
                ('school', models.CharField(blank=True, db_column='School', max_length=60, null=True)),
                ('sex', models.CharField(db_column='Sex', max_length=2)),
                ('e_mail', models.CharField(blank=True, db_column='E-mail', max_length=60, null=True)),
            ],
            options={
                'db_table': 'tbmanager',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TboutWork',
            fields=[
                ('ow_number', models.CharField(db_column='Ow_Number', max_length=10, primary_key=True, serialize=False)),
                ('ow_post', models.CharField(db_column='Ow_Post', max_length=60)),
                ('w_time', models.CharField(blank=True, db_column='W_Time', max_length=60, null=True)),
                ('w_place', models.CharField(blank=True, db_column='W_Place', max_length=60, null=True)),
                ('work', models.CharField(db_column='Work', max_length=200)),
                ('w_salary', models.CharField(blank=True, db_column='W_Salary', max_length=20, null=True)),
                ('w_reuire', models.CharField(blank=True, db_column='W_Reuire', max_length=200, null=True)),
                ('w_amount', models.CharField(blank=True, db_column='W_Amount', max_length=50, null=True)),
                ('ddl_time', models.DateTimeField(db_column='Ddl_Time')),
                ('ipub_time', models.DateTimeField(db_column='Ipub_Time')),
                ('w_ps', models.CharField(blank=True, db_column='W_Ps', max_length=200, null=True)),
            ],
            options={
                'db_table': 'tbout_work',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbqualify',
            fields=[
                ('com_license', models.CharField(db_column='Com_License', max_length=20, primary_key=True, serialize=False)),
                ('com_condition', models.CharField(blank=True, db_column='Com_Condition', max_length=200, null=True)),
                ('com_business', models.CharField(blank=True, db_column='Com_Business', max_length=200, null=True)),
            ],
            options={
                'db_table': 'tbqualify',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbquery',
            fields=[
                ('q_number', models.CharField(db_column='Q_Number', max_length=10, primary_key=True, serialize=False)),
                ('q_content', models.CharField(db_column='Q_Content', max_length=200)),
                ('q_time', models.DateTimeField(db_column='Q_Time')),
                ('q_direc', models.CharField(db_column='Q_direc', max_length=10)),
            ],
            options={
                'db_table': 'tbquery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbresume',
            fields=[
                ('res_id', models.CharField(db_column='Res_ID', max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=20)),
                ('age', models.IntegerField(db_column='Age')),
                ('sex', models.CharField(db_column='Sex', max_length=2)),
                ('res_asses', models.TextField(blank=True, db_column='Res_Asses', null=True)),
                ('res_edu', models.TextField(blank=True, db_column='Res_Edu', null=True)),
                ('res_work', models.TextField(blank=True, db_column='Res_Work', null=True)),
                ('res_proj', models.TextField(blank=True, db_column='Res_Proj', null=True)),
                ('res_extra', models.TextField(blank=True, db_column='Res_extra', null=True)),
                ('res_per', models.TextField(blank=True, db_column='Res_Per', null=True)),
            ],
            options={
                'db_table': 'tbresume',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbstudent',
            fields=[
                ('stu_id', models.CharField(db_column='Stu_ID', max_length=13, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=20)),
                ('pov_identity', models.CharField(db_column='Pov_Identity', max_length=2)),
                ('phonenumber_phonenumberphonenumber_phonenumber', models.CharField(db_column='PhoneNumber\r\nPhoneNumberPhoneNumber\r\nPhoneNumber', max_length=12)),
                ('password', models.CharField(db_column='Password', max_length=20)),
                ('nickname', models.CharField(db_column='Nickname', max_length=20)),
                ('sex', models.CharField(db_column='Sex', max_length=2)),
                ('age', models.IntegerField(db_column='Age')),
                ('e_mail', models.CharField(blank=True, db_column='E_mail', max_length=60, null=True)),
                ('school', models.CharField(db_column='School', max_length=60)),
                ('major', models.CharField(blank=True, db_column='Major', max_length=60, null=True)),
                ('grade', models.CharField(blank=True, db_column='Grade', max_length=6, null=True)),
            ],
            options={
                'db_table': 'tbstudent',
                'managed': False,
            },
        ),
    ]