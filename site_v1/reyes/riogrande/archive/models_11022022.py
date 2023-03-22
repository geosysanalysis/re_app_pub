# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcaciaLen(models.Model):
    dat = models.DateField(blank=True, null=True)
    sum_len = models.DecimalField(max_digits=28, decimal_places=2, blank=True, null=True)
    frac_len = models.DecimalField(max_digits=31, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'acacia_len'


class AllLen(models.Model):
    thedate = models.DateField(blank=True, null=True)
    isleta_sum_len = models.DecimalField(max_digits=28, decimal_places=2, blank=True, null=True)
    isleta_frac_len = models.DecimalField(max_digits=31, decimal_places=2, blank=True, null=True)
    acacia_sum_len = models.DecimalField(max_digits=28, decimal_places=2, blank=True, null=True)
    acacia_frac_len = models.DecimalField(max_digits=31, decimal_places=2, blank=True, null=True)
    combined_sum_len = models.DecimalField(max_digits=29, decimal_places=2, blank=True, null=True)
    combined_frac_len = models.DecimalField(max_digits=32, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'all_len'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Databasechangelog(models.Model):
    id = models.CharField(db_column='ID', max_length=255)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=255)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=255)  # Field name made lowercase.
    dateexecuted = models.DateTimeField(db_column='DATEEXECUTED')  # Field name made lowercase.
    orderexecuted = models.IntegerField(db_column='ORDEREXECUTED')  # Field name made lowercase.
    exectype = models.CharField(db_column='EXECTYPE', max_length=10)  # Field name made lowercase.
    md5sum = models.CharField(db_column='MD5SUM', max_length=35, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    liquibase = models.CharField(db_column='LIQUIBASE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contexts = models.CharField(db_column='CONTEXTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    labels = models.CharField(db_column='LABELS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deployment_id = models.CharField(db_column='DEPLOYMENT_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'databasechangelog'


class Databasechangeloglock(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    locked = models.TextField(db_column='LOCKED')  # Field name made lowercase. This field type is a guess.
    lockgranted = models.DateTimeField(db_column='LOCKGRANTED', blank=True, null=True)  # Field name made lowercase.
    lockedby = models.CharField(db_column='LOCKEDBY', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'databasechangeloglock'


class DischargeBallTape(models.Model):
    dbid = models.AutoField(primary_key=True)
    qid = models.ForeignKey('DischargeGsa', models.DO_NOTHING, db_column='qid')
    channel_width_ft = models.IntegerField(blank=True, null=True)
    depth_measurement_1_ft = models.IntegerField(blank=True, null=True)
    depth_measurement_2_ft = models.IntegerField(blank=True, null=True)
    depth_measurement_3_ft = models.IntegerField(blank=True, null=True)
    depth_measurement_4_ft = models.IntegerField(blank=True, null=True)
    average_depth_ft = models.IntegerField(blank=True, null=True)
    cross_section_area_sq_ft = models.IntegerField(blank=True, null=True)
    seconds_to_travel_length_recorded_below_typically_20_ft = models.IntegerField(blank=True, null=True)
    timed_length_ft_leave_at_20_unless_a_different_distance_was_used = models.IntegerField(blank=True, null=True)
    correction_factor_coefficient_typically_leave_at_09 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discharge_ball_tape'


class DischargeGsa(models.Model):
    qid = models.AutoField(primary_key=True)
    id = models.ForeignKey('Observation', models.DO_NOTHING, db_column='id')
    discharge_cfs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discharge_gsa'


class DischargeVisual(models.Model):
    dvid = models.AutoField(primary_key=True)
    qid = models.ForeignKey(DischargeGsa, models.DO_NOTHING, db_column='qid')
    minimum_estimated_discharge_cfs = models.IntegerField(blank=True, null=True)
    maximum_estimated_discharge_cfs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discharge_visual'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DryLength(models.Model):
    rm_up = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rm_down = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dry_length = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    dat = models.DateField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'dry_length'


class DryLengthAgg(models.Model):
    rm_up = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rm_down = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dry_length = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    dat = models.DateField(blank=True, null=True)
    rm_down_rd = models.DecimalField(max_digits=22, decimal_places=1, blank=True, null=True)
    rm_up_rd = models.DecimalField(max_digits=22, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'dry_length_agg'


class Dryness(models.Model):
    dryid = models.IntegerField(primary_key=True)
    id = models.ForeignKey('Observation', models.DO_NOTHING, db_column='id')
    extent = models.CharField(max_length=10, blank=True, null=True)
    down_dryid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dryness'


class Feature(models.Model):
    fid = models.AutoField(primary_key=True)
    feature = models.TextField(blank=True, null=True)
    rm = models.ForeignKey('Rivermile', models.DO_NOTHING, db_column='rm', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feature'


class FeatureRm(models.Model):
    rm_rounded = models.DecimalField(db_column='rm-rounded', max_digits=22, decimal_places=1, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    feature = models.TextField(db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'feature_rm'


class FlatTable(models.Model):
    rm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    id = models.IntegerField()
    qid = models.IntegerField(blank=True, null=True)
    fulcrum_id = models.CharField(max_length=38, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    obstype = models.CharField(max_length=38, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    datet = models.DateTimeField(blank=True, null=True)
    note = models.TextField(db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    observer_name_joined = models.CharField(max_length=303, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    oid_joined = models.CharField(max_length=25, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    remid = models.IntegerField(blank=True, null=True)
    approximate_width_ft = models.IntegerField(blank=True, null=True)
    approximate_length_ft = models.IntegerField(blank=True, null=True)
    approximate_area_sq_feet = models.IntegerField(blank=True, null=True)
    discharge_cfs = models.IntegerField(blank=True, null=True)
    dvid = models.IntegerField(blank=True, null=True)
    minimum_estimated_discharge_cfs = models.IntegerField(blank=True, null=True)
    maximum_estimated_discharge_cfs = models.IntegerField(blank=True, null=True)
    dbid = models.IntegerField(blank=True, null=True)
    channel_width_ft = models.IntegerField(blank=True, null=True)
    depth_measurement_1_ft = models.IntegerField(blank=True, null=True)
    depth_measurement_2_ft = models.IntegerField(blank=True, null=True)
    depth_measurement_3_ft = models.IntegerField(blank=True, null=True)
    depth_measurement_4_ft = models.IntegerField(blank=True, null=True)
    average_depth_ft = models.IntegerField(blank=True, null=True)
    cross_section_area_sq_ft = models.IntegerField(blank=True, null=True)
    seconds_to_travel_length_recorded_below_typically_20_ft = models.IntegerField(blank=True, null=True)
    timed_length_ft_leave_at_20_unless_a_different_distance_was_used = models.IntegerField(blank=True, null=True)
    correction_factor_coefficient_typically_leave_at_09 = models.IntegerField(blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    photos_gen_url = models.CharField(max_length=2083, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    dryid = models.IntegerField(blank=True, null=True)
    extent = models.CharField(max_length=10, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    down_dryid = models.IntegerField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)  # This field type is a guess.
    latlong = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'flat_table'


class IsletaLen(models.Model):
    dat = models.DateField(blank=True, null=True)
    sum_len = models.DecimalField(max_digits=28, decimal_places=2, blank=True, null=True)
    frac_len = models.DecimalField(max_digits=31, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'isleta_len'


class Observation(models.Model):
    fulcrum_id = models.CharField(max_length=38, blank=True, null=True)
    rm = models.ForeignKey('Rivermile', models.DO_NOTHING, db_column='rm', blank=True, null=True)
    obstype = models.CharField(max_length=38, blank=True, null=True)
    datet = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'observation'


class ObservationObserver(models.Model):
    ooid = models.AutoField(primary_key=True)
    id = models.ForeignKey(Observation, models.DO_NOTHING, db_column='id')
    oid = models.ForeignKey('Observer', models.DO_NOTHING, db_column='oid')

    class Meta:
        managed = False
        db_table = 'observation_observer'


class Observer(models.Model):
    oid = models.AutoField(primary_key=True)
    observer_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'observer'


class Photos(models.Model):
    pid = models.AutoField(primary_key=True)
    id = models.ForeignKey(Observation, models.DO_NOTHING, db_column='id')
    photos_gen_url = models.CharField(max_length=2083, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photos'


class Reach(models.Model):
    reaid = models.AutoField(primary_key=True)
    reach = models.CharField(max_length=10, blank=True, null=True)
    upstream_rm = models.ForeignKey('Rivermile', models.DO_NOTHING, db_column='upstream_rm', blank=True, null=True)
    downstream_rm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reach'


class Remnant(models.Model):
    remid = models.AutoField(primary_key=True)
    id = models.ForeignKey(Observation, models.DO_NOTHING, db_column='id')
    approximate_width_ft = models.IntegerField(blank=True, null=True)
    approximate_length_ft = models.IntegerField(blank=True, null=True)
    approximate_area_sq_feet = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'remnant'


class Rivermile(models.Model):
    rm = models.DecimalField(primary_key=True, max_digits=5, decimal_places=2)
    position = models.TextField()  # This field type is a guess.
    latlong = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rivermile'


class Subreach(models.Model):
    sid = models.AutoField(primary_key=True)
    subreach = models.CharField(blank=True, null=True)
    upstream_rm = models.ForeignKey(Rivermile, models.DO_NOTHING, db_column='upstream_rm', blank=True, null=True)
    downstream_rm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subreach'


class UsgsData(models.Model):
    uoid = models.AutoField(primary_key=True)
    usgs = models.ForeignKey('UsgsGages', models.DO_NOTHING)
    date = models.DateTimeField()
    flow_cfs = models.FloatField(blank=True, null=True)
    prov_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usgs_data'


class UsgsGages(models.Model):
    usgs_id = models.AutoField(primary_key=True)
    fid = models.ForeignKey(Feature, models.DO_NOTHING, db_column='fid')
    usgs_station_name = models.CharField(max_length=8)
    usgs_feature_short_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usgs_gages'
