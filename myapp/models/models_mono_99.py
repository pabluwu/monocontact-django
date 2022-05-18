# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from .models_mono_base import Account, Capability, AccountUser

class Action(models.Model):
    area_id = models.IntegerField(blank=True, null=True)
    request_type_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    created_on = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField()
    listing = models.ForeignKey('Listing', models.DO_NOTHING, blank=True, null=True)
    tag = models.ForeignKey('Tag', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=255)
    email = models.CharField(max_length=255, db_collation='utf8_general_ci')
    send_mail_on_create = models.IntegerField()
    source_email = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    source_name = models.CharField(max_length=255, db_collation='utf8_general_ci')
    referral_subject = models.CharField(max_length=255, blank=True, null=True)
    referral_text = models.TextField(blank=True, null=True)
    success_message = models.TextField()
    design = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    text_button = models.CharField(max_length=255)
    double_opt_in = models.CharField(max_length=255, db_collation='utf8_general_ci')
    double_opt_in_url = models.CharField(max_length=255, blank=True, null=True)
    generate_lead = models.IntegerField()
    limit = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    enable_captcha = models.IntegerField()
    enable_trigger = models.IntegerField()
    enable_lead_alerts = models.IntegerField()
    image_header = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    custom_inactive_msg = models.TextField(blank=True, null=True)
    custom_limit_msg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'action'


class ActionMeta(models.Model):
    action = models.ForeignKey(Action, models.DO_NOTHING)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'action_meta'


class Area(models.Model):
    area = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='+')
    name = models.CharField(max_length=255)
    working_time = models.IntegerField(blank=True, null=True)
    request_time = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'


class AreaListing(models.Model):
    area = models.ForeignKey(Area, models.DO_NOTHING)
    listing = models.ForeignKey('Listing', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'area_listing'


class Blacklist(models.Model):
    account = models.ForeignKey(Account, models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=255, db_collation='utf8_general_ci')
    bounced = models.IntegerField()
    unsubscribed = models.IntegerField()
    unsubscribed_on = models.DateTimeField()
    unsubscribe_reason = models.IntegerField(blank=True, null=True)
    unsubscribe_reason_text = models.CharField(max_length=255, blank=True, null=True)
    spam = models.IntegerField()
    manually = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blacklist'


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    subject = models.CharField(max_length=255)
    html = models.TextField()
    text = models.TextField()
    from_name = models.CharField(max_length=255)
    from_email = models.CharField(max_length=255, db_collation='utf8_general_ci')
    reply_to = models.CharField(max_length=255)
    template = models.ForeignKey('Template', models.DO_NOTHING, blank=True, null=True)
    listing_names = models.CharField(max_length=1024, blank=True, null=True)
    status = models.IntegerField()
    sent = models.IntegerField()
    opened = models.IntegerField()
    bounced = models.IntegerField()
    clicked = models.IntegerField()
    unsubscribed = models.IntegerField()
    spam = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    sent_date = models.DateTimeField(blank=True, null=True)
    send_date = models.DateTimeField(blank=True, null=True)
    step = models.IntegerField(blank=True, null=True)
    editor = models.IntegerField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign'


class CampaignFilter(models.Model):
    campaign = models.ForeignKey(Campaign, models.DO_NOTHING)
    filter = models.ForeignKey('Filter', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_filter'
        unique_together = (('campaign', 'filter'),)


class CampaignListing(models.Model):
    campaign = models.ForeignKey(Campaign, models.DO_NOTHING)
    listing = models.ForeignKey('Listing', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_listing'
        unique_together = (('campaign', 'listing'),)


class CampaignSubscriber(models.Model):
    contact = models.ForeignKey('Contact', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=255, db_collation='utf8_general_ci')
    account = models.ForeignKey(Account, models.DO_NOTHING)
    campaign = models.ForeignKey(Campaign, models.DO_NOTHING)
    sent = models.IntegerField()
    bounced = models.IntegerField()
    opened = models.IntegerField()
    opened_date = models.DateTimeField(blank=True, null=True)
    clicked = models.IntegerField()
    unsubscribed = models.IntegerField()
    spam = models.IntegerField()
    country = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    client_os = models.CharField(max_length=100, blank=True, null=True)
    client_device_type = models.CharField(max_length=100, blank=True, null=True)
    client_name = models.CharField(max_length=100, blank=True, null=True)
    client_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_subscriber'
        unique_together = (('email', 'campaign'),)


class CampaignSubscriberUrl(models.Model):
    campaign_subscriber = models.ForeignKey(CampaignSubscriber, models.DO_NOTHING)
    campaign_url = models.ForeignKey('CampaignUrl', models.DO_NOTHING)
    campaign = models.ForeignKey(Campaign, models.DO_NOTHING)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    clicked_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'campaign_subscriber_url'


class CampaignUrl(models.Model):
    url = models.CharField(max_length=1000)
    campaign = models.ForeignKey(Campaign, models.DO_NOTHING)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    clicked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'campaign_url'


class Comment(models.Model):
    text = models.TextField()
    lead = models.ForeignKey('Lead', models.DO_NOTHING)
    user_role = models.ForeignKey('UserRole', models.DO_NOTHING, blank=True, null=True)
    created_on = models.DateTimeField()
    active = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Contact(models.Model):
    code = models.CharField(unique=True, max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    account_id = models.IntegerField()
    email = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_source = models.IntegerField()
    created_by = models.IntegerField()
    updated_on = models.DateTimeField(blank=True, null=True)
    updated_source = models.IntegerField()
    updated_by = models.IntegerField()
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    is_blacklisted = models.IntegerField()
    bounced = models.IntegerField()
    unsubscribed = models.IntegerField()
    unsubscribed_on = models.DateTimeField(blank=True, null=True)
    unsubscribe_reason = models.IntegerField(blank=True, null=True)
    unsubscribe_reason_text = models.CharField(max_length=255, blank=True, null=True)
    manually = models.IntegerField()
    spam = models.IntegerField()
    token = models.CharField(max_length=255, blank=True, null=True)
    score = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    flag = models.IntegerField()
    fields = models.JSONField(blank=True, null=True)

    @property
    def account(self):
        return Account.objects.get(pk=self.account_id)

    class Meta:
        managed = False
        db_table = 'contact'


class ContactData(models.Model):
    contact_field = models.ForeignKey('ContactField', models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    value = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'contact_data'
        unique_together = (('contact_field', 'contact'),)


class ContactField(models.Model):
    name = models.CharField(max_length=255)
    placeholder = models.CharField(max_length=255)
    options = models.JSONField(blank=True, null=True)
    type = models.IntegerField()
    default_value = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField()
    enable_crm = models.IntegerField()
    enable_view = models.IntegerField()
    fixed = models.IntegerField()
    group = models.ForeignKey('Group', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_field'


class ContactTag(models.Model):
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    tag = models.ForeignKey('Tag', models.DO_NOTHING)
    created_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contact_tag'
        unique_together = (('contact', 'tag'),)


class Event(models.Model):
    name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255, blank=True, null=True)
    is_api = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event'


class EventField(models.Model):
    name = models.CharField(max_length=255)
    type = models.IntegerField()
    event = models.ForeignKey(Event, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_field'


class FieldData(models.Model):
    account = models.ForeignKey(Account, models.DO_NOTHING)
    action = models.ForeignKey(Action, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    created_on = models.DateTimeField()
    verified = models.IntegerField()
    trigger_email = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    traffic_type = models.CharField(max_length=255, blank=True, null=True)
    traffic_source = models.CharField(max_length=255, blank=True, null=True)
    traffic_medium = models.CharField(max_length=255, blank=True, null=True)
    session_pages = models.IntegerField(blank=True, null=True)
    current_page = models.CharField(max_length=2000, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    client_device_type = models.CharField(max_length=255, blank=True, null=True)
    client_os = models.CharField(max_length=255, blank=True, null=True)
    client_name = models.CharField(max_length=255, blank=True, null=True)
    client_ip = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_data'


class FieldDataValues(models.Model):
    field_data = models.ForeignKey(FieldData, models.DO_NOTHING)
    field = models.ForeignKey('FormField', models.DO_NOTHING)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'field_data_values'


class FieldOption(models.Model):
    account = models.ForeignKey(Account, models.DO_NOTHING)
    action = models.ForeignKey(Action, models.DO_NOTHING)
    field = models.ForeignKey('FormField', models.DO_NOTHING)
    field_name = models.CharField(max_length=255)
    field_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'field_option'


class Filter(models.Model):
    name = models.CharField(max_length=255)
    filter = models.CharField(max_length=1024)
    operator_type = models.IntegerField()
    filter_json = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filter'


class FormData(models.Model):
    created_on = models.DateTimeField()
    account = models.ForeignKey(Account, models.DO_NOTHING)
    action = models.ForeignKey(Action, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, db_collation='utf8_general_ci')
    referred_by = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'form_data'


class FormField(models.Model):
    account = models.ForeignKey(Account, models.DO_NOTHING)
    action = models.ForeignKey(Action, models.DO_NOTHING)
    field_type = models.IntegerField()
    short_name = models.CharField(max_length=255, db_collation='utf8_general_ci')
    field_name = models.CharField(max_length=1024)
    field_order = models.IntegerField()
    unique = models.IntegerField()
    is_required = models.IntegerField()
    is_conditional = models.IntegerField()
    image_name = models.CharField(max_length=1024, blank=True, null=True)
    json_condition = models.JSONField(blank=True, null=True)
    validations = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_field'


class Group(models.Model):
    name = models.CharField(max_length=255)
    fields = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group'


class Lead(models.Model):
    cc_user = models.IntegerField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    first_email_sent = models.IntegerField()
    lead_time = models.FloatField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    type_time = models.IntegerField(blank=True, null=True)
    source = models.ForeignKey('Source', models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    user_role = models.ForeignKey('UserRole', models.DO_NOTHING, blank=True, null=True, related_name='lead_user_role')
    request_type = models.ForeignKey('RequestType', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('Status', models.DO_NOTHING, blank=True, null=True)
    contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    overseer = models.ForeignKey('UserRole', models.DO_NOTHING, blank=True, null=True, related_name='lead_overseer')
    created_by = models.ForeignKey('UserRole', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='lead_created_by')
    closed_by = models.ForeignKey('UserRole', models.DO_NOTHING, db_column='closed_by', blank=True, null=True, related_name='lead_closed_by')
    closed_on = models.DateField(blank=True, null=True)
    status_0 = models.IntegerField(db_column='status')  # Field renamed because of name conflict.
    trace = models.JSONField(blank=True, null=True)
    followers = models.JSONField(blank=True, null=True)
    is_contacted = models.IntegerField(blank=True, null=True)
    contacted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lead'


class LeadSkill(models.Model):
    skill = models.ForeignKey('Skill', models.DO_NOTHING)
    lead = models.ForeignKey(Lead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lead_skill'


class Listing(models.Model):
    name = models.CharField(max_length=255)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    created_on = models.DateTimeField(blank=True, null=True)
    unsubscribe_external_url = models.CharField(max_length=2048, blank=True, null=True)
    invite_from = models.CharField(max_length=255, blank=True, null=True)
    invite_from_email = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    invite_subject = models.CharField(max_length=255, blank=True, null=True)
    invite_message = models.TextField(blank=True, null=True)
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'listing'


class Log(models.Model):
    event_date = models.DateTimeField()
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    request_type = models.ForeignKey('RequestType', models.DO_NOTHING, blank=True, null=True)
    element_id = models.IntegerField(blank=True, null=True)
    json_fields = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class Option(models.Model):
    name = models.CharField(unique=True, max_length=50)
    value = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'option'


class RequestType(models.Model):
    name = models.CharField(max_length=255)
    working_time = models.IntegerField(blank=True, null=True)
    request_time = models.FloatField(blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_type'


class Role(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'role'


class RoleCapability(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING)
    capability = models.ForeignKey(Capability, models.DO_NOTHING)
    custom = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_capability'
        unique_together = (('role', 'capability'),)


class Rule(models.Model):
    name = models.CharField(max_length=255)
    rule_trigger = models.IntegerField()
    field_id = models.IntegerField(blank=True, null=True)
    field_value = models.CharField(max_length=255, blank=True, null=True)
    rule_trigger_value = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rule'


class RuleContact(models.Model):
    rule = models.ForeignKey(Rule, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    rule_stage = models.ForeignKey('RuleStage', models.DO_NOTHING, blank=True, null=True)
    position = models.IntegerField()
    email = models.CharField(max_length=255, db_collation='utf8_general_ci')
    start_time = models.DateTimeField()
    added_time = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rule_contact'


class RuleMail(models.Model):
    name = models.CharField(max_length=255)
    account_id = models.IntegerField()
    subject = models.CharField(max_length=255)
    html = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    from_name = models.CharField(max_length=255)
    from_email = models.CharField(max_length=255)
    reply_to = models.CharField(max_length=255)
    template_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    editor = models.IntegerField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rule_mail'


class RuleStage(models.Model):
    rule = models.ForeignKey(Rule, models.DO_NOTHING)
    action = models.IntegerField()
    value = models.IntegerField(blank=True, null=True)
    wait_time_unit = models.IntegerField()
    wait_time_value = models.IntegerField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rule_stage'


class Score(models.Model):
    action = models.IntegerField()
    value = models.IntegerField()
    recurring = models.IntegerField()
    max = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'score'


class ScoreLog(models.Model):
    created_on = models.DateTimeField()
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    score = models.ForeignKey(Score, models.DO_NOTHING)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'score_log'


class Skill(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'skill'


class Source(models.Model):
    name = models.CharField(max_length=255)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'source'


class Status(models.Model):
    name = models.CharField(max_length=255)
    start = models.IntegerField(blank=True, null=True)
    end = models.IntegerField(blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'


class Subscriber(models.Model):
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    unsubscribed_on = models.DateTimeField(blank=True, null=True)
    listing = models.ForeignKey(Listing, models.DO_NOTHING)
    account = models.ForeignKey(Account, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)
    bounced = models.IntegerField()
    unsubscribed = models.IntegerField()
    unsubscribe_reason = models.IntegerField(blank=True, null=True)
    unsubscribe_reason_text = models.CharField(max_length=255, blank=True, null=True)
    spam = models.IntegerField()
    manually = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subscriber'


class Tag(models.Model):
    name = models.CharField(max_length=255)
    listing = models.ForeignKey(Listing, models.DO_NOTHING, blank=True, null=True)
    created_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tag'


class TblMigration(models.Model):
    version = models.CharField(primary_key=True, max_length=180)
    apply_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_migration'


class Template(models.Model):
    name = models.CharField(max_length=255)
    account = models.ForeignKey(Account, models.DO_NOTHING, blank=True, null=True)
    html = models.TextField(db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    editor = models.IntegerField()
    body = models.TextField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)
    preview = models.TextField(db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template'


class TicketField(models.Model):
    data_type = models.IntegerField()
    options = models.JSONField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    close_required = models.IntegerField()
    create_required = models.IntegerField()
    user_required = models.IntegerField()
    extern_name = models.CharField(max_length=255, blank=True, null=True)
    intern_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    order = models.IntegerField()
    field_text = models.CharField(max_length=2000, blank=True, null=True)
    ticket_field_option_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_field'


class TicketFieldRestriction(models.Model):
    type = models.IntegerField()
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    request_type_id = models.IntegerField(blank=True, null=True)
    ticket_field = models.ForeignKey(TicketField, models.DO_NOTHING)
    option = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_field_restriction'


class TicketFieldValue(models.Model):
    value = models.CharField(max_length=1024)
    ticket_field = models.ForeignKey(TicketField, models.DO_NOTHING)
    lead = models.ForeignKey(Lead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ticket_field_value'


class TicketTrigger(models.Model):
    type = models.IntegerField()
    data_type = models.IntegerField(blank=True, null=True)
    value = models.IntegerField()
    subvalue = models.IntegerField(blank=True, null=True)
    subvalue_data = models.CharField(max_length=255, blank=True, null=True)
    action = models.IntegerField()
    action_value = models.IntegerField()
    request_time = models.FloatField(blank=True, null=True)
    working_time = models.IntegerField(blank=True, null=True)
    text_field = models.TextField(blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    request_type = models.ForeignKey(RequestType, models.DO_NOTHING, blank=True, null=True)
    enable_asign_trigger = models.IntegerField(blank=True, null=True)
    field_read_id = models.IntegerField(blank=True, null=True)
    ticket_field_write_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_trigger'


class UserRole(models.Model):
    set_overseer = models.IntegerField()
    crm_user = models.IntegerField()
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    account_user = models.OneToOneField(AccountUser, models.DO_NOTHING)
    role = models.ForeignKey(Role, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'
        


class UserRoleArea(models.Model):
    area = models.ForeignKey(Area, models.DO_NOTHING)
    user_role = models.ForeignKey(UserRole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role_area'


class UserRoleSkill(models.Model):
    skill = models.ForeignKey(Skill, models.DO_NOTHING)
    user_role = models.ForeignKey(UserRole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role_skill'
