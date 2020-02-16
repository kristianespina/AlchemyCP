# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccRegNum(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'acc_reg_num'
        unique_together = (('account_id', 'key', 'index'),)


class AccRegStr(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'acc_reg_str'
        unique_together = (('account_id', 'key', 'index'),)


class Achievement(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    id = models.BigIntegerField()
    count1 = models.PositiveIntegerField()
    count2 = models.PositiveIntegerField()
    count3 = models.PositiveIntegerField()
    count4 = models.PositiveIntegerField()
    count5 = models.PositiveIntegerField()
    count6 = models.PositiveIntegerField()
    count7 = models.PositiveIntegerField()
    count8 = models.PositiveIntegerField()
    count9 = models.PositiveIntegerField()
    count10 = models.PositiveIntegerField()
    completed = models.DateTimeField(blank=True, null=True)
    rewarded = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'achievement'
        unique_together = (('char_id', 'id'),)


class Auction(models.Model):
    auction_id = models.BigAutoField(primary_key=True)
    seller_id = models.PositiveIntegerField()
    seller_name = models.CharField(max_length=30)
    buyer_id = models.PositiveIntegerField()
    buyer_name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    buynow = models.PositiveIntegerField()
    hours = models.SmallIntegerField()
    timestamp = models.PositiveIntegerField()
    nameid = models.PositiveSmallIntegerField()
    item_name = models.CharField(max_length=50)
    type = models.SmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'auction'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BonusScript(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    script = models.TextField()
    tick = models.BigIntegerField()
    flag = models.PositiveSmallIntegerField()
    type = models.PositiveIntegerField()
    icon = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'bonus_script'
        unique_together = (('char_id', 'type'),)


class BuyingstoreItems(models.Model):
    buyingstore_id = models.PositiveIntegerField(primary_key=True)
    index = models.PositiveSmallIntegerField()
    item_id = models.PositiveIntegerField()
    amount = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'buyingstore_items'
        unique_together = (('buyingstore_id', 'index'),)


class Buyingstores(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField()
    sex = models.CharField(max_length=1)
    map = models.CharField(max_length=20)
    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=80)
    limit = models.PositiveIntegerField()
    body_direction = models.CharField(max_length=1)
    head_direction = models.CharField(max_length=1)
    sit = models.CharField(max_length=1)
    autotrade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'buyingstores'


class CartInventory(models.Model):
    char_id = models.IntegerField()
    nameid = models.PositiveSmallIntegerField()
    amount = models.IntegerField()
    equip = models.PositiveIntegerField()
    identify = models.SmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.IntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    bound = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cart_inventory'


class Char(models.Model):
    char_id = models.AutoField(primary_key=True)
    account_id = models.PositiveIntegerField()
    char_num = models.IntegerField()
    name = models.CharField(unique=True, max_length=30)
    class_field = models.PositiveSmallIntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    base_level = models.PositiveSmallIntegerField()
    job_level = models.PositiveSmallIntegerField()
    base_exp = models.BigIntegerField()
    job_exp = models.BigIntegerField()
    zeny = models.PositiveIntegerField()
    str = models.PositiveSmallIntegerField()
    agi = models.PositiveSmallIntegerField()
    vit = models.PositiveSmallIntegerField()
    int = models.PositiveSmallIntegerField()
    dex = models.PositiveSmallIntegerField()
    luk = models.PositiveSmallIntegerField()
    max_hp = models.PositiveIntegerField()
    hp = models.PositiveIntegerField()
    max_sp = models.PositiveIntegerField()
    sp = models.PositiveIntegerField()
    status_point = models.PositiveIntegerField()
    skill_point = models.PositiveIntegerField()
    option = models.IntegerField()
    karma = models.IntegerField()
    manner = models.SmallIntegerField()
    party_id = models.PositiveIntegerField()
    guild_id = models.PositiveIntegerField()
    pet_id = models.PositiveIntegerField()
    homun_id = models.PositiveIntegerField()
    elemental_id = models.PositiveIntegerField()
    hair = models.PositiveIntegerField()
    hair_color = models.PositiveSmallIntegerField()
    clothes_color = models.PositiveSmallIntegerField()
    body = models.PositiveSmallIntegerField()
    weapon = models.PositiveSmallIntegerField()
    shield = models.PositiveSmallIntegerField()
    head_top = models.PositiveSmallIntegerField()
    head_mid = models.PositiveSmallIntegerField()
    head_bottom = models.PositiveSmallIntegerField()
    robe = models.PositiveSmallIntegerField()
    last_map = models.CharField(max_length=11)
    last_x = models.PositiveSmallIntegerField()
    last_y = models.PositiveSmallIntegerField()
    save_map = models.CharField(max_length=11)
    save_x = models.PositiveSmallIntegerField()
    save_y = models.PositiveSmallIntegerField()
    partner_id = models.PositiveIntegerField()
    online = models.IntegerField()
    father = models.PositiveIntegerField()
    mother = models.PositiveIntegerField()
    child = models.PositiveIntegerField()
    fame = models.PositiveIntegerField()
    rename = models.PositiveSmallIntegerField()
    delete_date = models.PositiveIntegerField()
    moves = models.PositiveIntegerField()
    unban_time = models.PositiveIntegerField()
    font = models.PositiveIntegerField()
    uniqueitem_counter = models.PositiveIntegerField()
    sex = models.CharField(max_length=1)
    hotkey_rowshift = models.PositiveIntegerField()
    clan_id = models.PositiveIntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    title_id = models.PositiveIntegerField()
    show_equip = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'char'


class CharRegNum(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'char_reg_num'
        unique_together = (('char_id', 'key', 'index'),)


class CharRegStr(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'char_reg_str'
        unique_together = (('char_id', 'key', 'index'),)


class Charlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.DateTimeField()
    char_msg = models.CharField(max_length=255)
    account_id = models.IntegerField()
    char_num = models.IntegerField()
    name = models.CharField(max_length=23)
    str = models.PositiveIntegerField()
    agi = models.PositiveIntegerField()
    vit = models.PositiveIntegerField()
    int = models.PositiveIntegerField()
    dex = models.PositiveIntegerField()
    luk = models.PositiveIntegerField()
    hair = models.IntegerField()
    hair_color = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'charlog'


class Clan(models.Model):
    clan_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    master = models.CharField(max_length=24)
    mapname = models.CharField(max_length=24)
    max_member = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'clan'


class ClanAlliance(models.Model):
    clan_id = models.PositiveIntegerField(primary_key=True)
    opposition = models.PositiveIntegerField()
    alliance_id = models.PositiveIntegerField()
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'clan_alliance'
        unique_together = (('clan_id', 'alliance_id'),)


class DbRoulette(models.Model):
    index = models.IntegerField(primary_key=True)
    level = models.PositiveSmallIntegerField()
    item_id = models.PositiveSmallIntegerField()
    amount = models.PositiveSmallIntegerField()
    flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'db_roulette'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Elemental(models.Model):
    ele_id = models.AutoField(primary_key=True)
    char_id = models.IntegerField()
    class_field = models.PositiveIntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    mode = models.PositiveIntegerField()
    hp = models.PositiveIntegerField()
    sp = models.PositiveIntegerField()
    max_hp = models.PositiveIntegerField()
    max_sp = models.PositiveIntegerField()
    atk1 = models.PositiveIntegerField()
    atk2 = models.PositiveIntegerField()
    matk = models.PositiveIntegerField()
    aspd = models.PositiveSmallIntegerField()
    def_field = models.PositiveSmallIntegerField(db_column='def')  # Field renamed because it was a Python reserved word.
    mdef = models.PositiveSmallIntegerField()
    flee = models.PositiveSmallIntegerField()
    hit = models.PositiveSmallIntegerField()
    life_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'elemental'


class Friends(models.Model):
    char_id = models.IntegerField(primary_key=True)
    friend_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'friends'
        unique_together = (('char_id', 'friend_id'),)


class GlobalAccRegNum(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'global_acc_reg_num'
        unique_together = (('account_id', 'key', 'index'),)


class GlobalAccRegStr(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'global_acc_reg_str'
        unique_together = (('account_id', 'key', 'index'),)


class Guild(models.Model):
    guild_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    char_id = models.PositiveIntegerField()
    master = models.CharField(max_length=24)
    guild_lv = models.PositiveIntegerField()
    connect_member = models.PositiveIntegerField()
    max_member = models.PositiveIntegerField()
    average_lv = models.PositiveSmallIntegerField()
    exp = models.BigIntegerField()
    next_exp = models.PositiveIntegerField()
    skill_point = models.PositiveIntegerField()
    mes1 = models.CharField(max_length=60)
    mes2 = models.CharField(max_length=120)
    emblem_len = models.PositiveIntegerField()
    emblem_id = models.PositiveIntegerField()
    emblem_data = models.TextField(blank=True, null=True)
    last_master_change = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guild'
        unique_together = (('guild_id', 'char_id'),)


class GuildAlliance(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    opposition = models.PositiveIntegerField()
    alliance_id = models.PositiveIntegerField()
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'guild_alliance'
        unique_together = (('guild_id', 'alliance_id'),)


class GuildCastle(models.Model):
    castle_id = models.PositiveIntegerField(primary_key=True)
    guild_id = models.PositiveIntegerField()
    economy = models.PositiveIntegerField()
    defense = models.PositiveIntegerField()
    triggere = models.PositiveIntegerField(db_column='triggerE')  # Field name made lowercase.
    triggerd = models.PositiveIntegerField(db_column='triggerD')  # Field name made lowercase.
    nexttime = models.PositiveIntegerField(db_column='nextTime')  # Field name made lowercase.
    paytime = models.PositiveIntegerField(db_column='payTime')  # Field name made lowercase.
    createtime = models.PositiveIntegerField(db_column='createTime')  # Field name made lowercase.
    visiblec = models.PositiveIntegerField(db_column='visibleC')  # Field name made lowercase.
    visibleg0 = models.PositiveIntegerField(db_column='visibleG0')  # Field name made lowercase.
    visibleg1 = models.PositiveIntegerField(db_column='visibleG1')  # Field name made lowercase.
    visibleg2 = models.PositiveIntegerField(db_column='visibleG2')  # Field name made lowercase.
    visibleg3 = models.PositiveIntegerField(db_column='visibleG3')  # Field name made lowercase.
    visibleg4 = models.PositiveIntegerField(db_column='visibleG4')  # Field name made lowercase.
    visibleg5 = models.PositiveIntegerField(db_column='visibleG5')  # Field name made lowercase.
    visibleg6 = models.PositiveIntegerField(db_column='visibleG6')  # Field name made lowercase.
    visibleg7 = models.PositiveIntegerField(db_column='visibleG7')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'guild_castle'


class GuildExpulsion(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    account_id = models.PositiveIntegerField()
    name = models.CharField(max_length=24)
    mes = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'guild_expulsion'
        unique_together = (('guild_id', 'name'),)


class GuildMember(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    char_id = models.PositiveIntegerField()
    exp = models.BigIntegerField()
    position = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_member'
        unique_together = (('guild_id', 'char_id'),)


class GuildPosition(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    position = models.PositiveIntegerField()
    name = models.CharField(max_length=24)
    mode = models.PositiveSmallIntegerField()
    exp_mode = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_position'
        unique_together = (('guild_id', 'position'),)


class GuildSkill(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    id = models.PositiveSmallIntegerField()
    lv = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_skill'
        unique_together = (('guild_id', 'id'),)


class GuildStorage(models.Model):
    guild_id = models.PositiveIntegerField()
    nameid = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField()
    equip = models.PositiveIntegerField()
    identify = models.PositiveSmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    bound = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_storage'


class GuildStorageLog(models.Model):
    guild_id = models.PositiveIntegerField()
    time = models.DateTimeField()
    char_id = models.IntegerField()
    name = models.CharField(max_length=24)
    nameid = models.PositiveSmallIntegerField()
    amount = models.IntegerField()
    identify = models.SmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()
    bound = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_storage_log'


class Homunculus(models.Model):
    homun_id = models.AutoField(primary_key=True)
    char_id = models.IntegerField()
    class_field = models.PositiveIntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    prev_class = models.IntegerField()
    name = models.CharField(max_length=24)
    level = models.SmallIntegerField()
    exp = models.BigIntegerField()
    intimacy = models.IntegerField()
    hunger = models.SmallIntegerField()
    str = models.PositiveSmallIntegerField()
    agi = models.PositiveSmallIntegerField()
    vit = models.PositiveSmallIntegerField()
    int = models.PositiveSmallIntegerField()
    dex = models.PositiveSmallIntegerField()
    luk = models.PositiveSmallIntegerField()
    hp = models.PositiveIntegerField()
    max_hp = models.PositiveIntegerField()
    sp = models.IntegerField()
    max_sp = models.IntegerField()
    skill_point = models.PositiveSmallIntegerField()
    alive = models.IntegerField()
    rename_flag = models.IntegerField()
    vaporize = models.IntegerField()
    autofeed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'homunculus'


class Hotkey(models.Model):
    char_id = models.IntegerField(primary_key=True)
    hotkey = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    itemskill_id = models.PositiveIntegerField()
    skill_lvl = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'hotkey'
        unique_together = (('char_id', 'hotkey'),)


class Interlog(models.Model):
    time = models.DateTimeField()
    log = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'interlog'


class Interreg(models.Model):
    varname = models.CharField(primary_key=True, max_length=11)
    value = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'interreg'


class Inventory(models.Model):
    char_id = models.PositiveIntegerField()
    nameid = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField()
    equip = models.PositiveIntegerField()
    identify = models.SmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    favorite = models.PositiveIntegerField()
    bound = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()
    equip_switch = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'inventory'


class Ipbanlist(models.Model):
    list = models.CharField(primary_key=True, max_length=15)
    btime = models.DateTimeField()
    rtime = models.DateTimeField()
    reason = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ipbanlist'
        unique_together = (('list', 'btime'),)


class Login(models.Model):
    REQUIRED_FIELDS = ('sex','birthdate','email')
    USERNAME_FIELD = 'userid'

    account_id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=23)
    user_pass = models.CharField(max_length=32)
    sex = models.CharField(max_length=1)
    email = models.CharField(max_length=39)
    group_id = models.IntegerField()
    state = models.PositiveIntegerField()
    unban_time = models.PositiveIntegerField()
    expiration_time = models.PositiveIntegerField()
    logincount = models.PositiveIntegerField()
    lastlogin = models.DateTimeField(blank=True, null=True)
    last_ip = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    character_slots = models.PositiveIntegerField()
    pincode = models.CharField(max_length=4)
    pincode_change = models.PositiveIntegerField()
    vip_time = models.PositiveIntegerField()
    old_group = models.IntegerField()

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    class Meta:
        managed = False
        db_table = 'login'


class Mail(models.Model):
    id = models.BigAutoField(primary_key=True)
    send_name = models.CharField(max_length=30)
    send_id = models.PositiveIntegerField()
    dest_name = models.CharField(max_length=30)
    dest_id = models.PositiveIntegerField()
    title = models.CharField(max_length=45)
    message = models.CharField(max_length=500)
    time = models.PositiveIntegerField()
    status = models.IntegerField()
    zeny = models.PositiveIntegerField()
    type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mail'


class MailAttachments(models.Model):
    id = models.BigAutoField(primary_key=True)
    index = models.PositiveSmallIntegerField()
    nameid = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    identify = models.SmallIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    unique_id = models.BigIntegerField()
    bound = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'mail_attachments'
        unique_together = (('id', 'index'),)


class Mapreg(models.Model):
    varname = models.CharField(primary_key=True, max_length=32)
    index = models.PositiveIntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mapreg'
        unique_together = (('varname', 'index'),)


class Market(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    nameid = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    amount = models.PositiveSmallIntegerField()
    flag = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'market'
        unique_together = (('name', 'nameid'),)


class Memo(models.Model):
    memo_id = models.AutoField(primary_key=True)
    char_id = models.PositiveIntegerField()
    map = models.CharField(max_length=11)
    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'memo'


class Mercenary(models.Model):
    mer_id = models.AutoField(primary_key=True)
    char_id = models.IntegerField()
    class_field = models.PositiveIntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    hp = models.PositiveIntegerField()
    sp = models.PositiveIntegerField()
    kill_counter = models.IntegerField()
    life_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mercenary'


class MercenaryOwner(models.Model):
    char_id = models.IntegerField(primary_key=True)
    merc_id = models.IntegerField()
    arch_calls = models.IntegerField()
    arch_faith = models.IntegerField()
    spear_calls = models.IntegerField()
    spear_faith = models.IntegerField()
    sword_calls = models.IntegerField()
    sword_faith = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mercenary_owner'


class Party(models.Model):
    party_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    exp = models.PositiveIntegerField()
    item = models.PositiveIntegerField()
    leader_id = models.PositiveIntegerField()
    leader_char = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'party'


class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    class_field = models.PositiveIntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=24)
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField()
    level = models.PositiveSmallIntegerField()
    egg_id = models.PositiveSmallIntegerField()
    equip = models.PositiveIntegerField()
    intimate = models.PositiveSmallIntegerField()
    hungry = models.PositiveSmallIntegerField()
    rename_flag = models.PositiveIntegerField()
    incubate = models.PositiveIntegerField()
    autofeed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet'


class Quest(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    quest_id = models.PositiveIntegerField()
    state = models.CharField(max_length=1)
    time = models.PositiveIntegerField()
    count1 = models.PositiveIntegerField()
    count2 = models.PositiveIntegerField()
    count3 = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'quest'
        unique_together = (('char_id', 'quest_id'),)


class Sales(models.Model):
    nameid = models.PositiveSmallIntegerField(primary_key=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales'


class ScData(models.Model):
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField(primary_key=True)
    type = models.PositiveSmallIntegerField()
    tick = models.BigIntegerField()
    val1 = models.IntegerField()
    val2 = models.IntegerField()
    val3 = models.IntegerField()
    val4 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sc_data'
        unique_together = (('char_id', 'type'),)


class Skill(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    id = models.PositiveSmallIntegerField()
    lv = models.PositiveIntegerField()
    flag = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'skill'
        unique_together = (('char_id', 'id'),)


class SkillHomunculus(models.Model):
    homun_id = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    lv = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'skill_homunculus'
        unique_together = (('homun_id', 'id'),)


class Skillcooldown(models.Model):
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField(primary_key=True)
    skill = models.PositiveSmallIntegerField()
    tick = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'skillcooldown'
        unique_together = (('char_id', 'skill'),)


class Storage(models.Model):
    account_id = models.PositiveIntegerField()
    nameid = models.PositiveSmallIntegerField()
    amount = models.PositiveSmallIntegerField()
    equip = models.PositiveIntegerField()
    identify = models.PositiveSmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    bound = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'storage'


class VendingItems(models.Model):
    vending_id = models.PositiveIntegerField(primary_key=True)
    index = models.PositiveSmallIntegerField()
    cartinventory_id = models.PositiveIntegerField()
    amount = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'vending_items'
        unique_together = (('vending_id', 'index'),)


class Vendings(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField()
    sex = models.CharField(max_length=1)
    map = models.CharField(max_length=20)
    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=80)
    body_direction = models.CharField(max_length=1)
    head_direction = models.CharField(max_length=1)
    sit = models.CharField(max_length=1)
    autotrade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vendings'
