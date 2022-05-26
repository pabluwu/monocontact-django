from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime
from multiprocessing.sharedctypes import Value
from django.db import models

from pytz import timezone
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class Account(models.Model):
    name = models.CharField(max_length=255, db_collation='latin1_swedish_ci')
    status = models.IntegerField()
    bulker = models.IntegerField()
    auto = models.IntegerField()
    domain = models.CharField(unique=True, max_length=100, db_collation='latin1_swedish_ci')
    api_token = models.CharField(max_length=255, db_collation='latin1_swedish_ci')
    api_secret = models.CharField(max_length=255, db_collation='latin1_swedish_ci')
    descuento = models.FloatField(blank=True, null=True)
    email_account = models.CharField(max_length=255, blank=True, null=True)
    external_id = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.IntegerField()
    disabled_reason = models.CharField(max_length=255, blank=True, null=True)

    objects= models.Manager().using('mono_base')

    class Meta:
        managed = False
        db_table = 'account'


class AccountPlan(models.Model):
    plan = models.ForeignKey('Plan', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(Account, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_plan'


class AccountUser(models.Model):
    account = models.ForeignKey(Account, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    role = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_user'
        unique_together = (('account', 'user'),)


class Capability(models.Model):
    slug = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    module = models.ForeignKey('Module', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'capability'


class Module(models.Model):
    name = models.CharField(max_length=255)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'module'


class ModulePlan(models.Model):
    module = models.ForeignKey(Module, models.DO_NOTHING)
    plan = models.ForeignKey('Plan', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'module_plan'


class Plan(models.Model):
    name = models.CharField(max_length=255, db_collation='latin1_swedish_ci')
    max_contacts = models.IntegerField(blank=True, null=True)
    max_users_crm = models.IntegerField(blank=True, null=True)
    max_forms = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    type = models.ForeignKey('Type', models.DO_NOTHING)
    api_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan'


class Type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'type'

class User(models.Model):
    email = models.CharField(unique=True, max_length=100, db_collation='latin1_swedish_ci')
    password = models.CharField(max_length=100, db_collation='latin1_swedish_ci')
    firstname = models.CharField(max_length=255, db_collation='latin1_swedish_ci')
    lastname = models.CharField(max_length=255, db_collation='latin1_swedish_ci')
    status = models.IntegerField()
    created = models.DateTimeField()
    lastvisit = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)
    token_created = models.DateTimeField(blank=True, null=True)
    manager = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'

