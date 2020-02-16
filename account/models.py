from django.db import models
from django.contrib.auth.models import AbstractUser

class Login(AbstractUser):  
    SEX = (
        ('M','Male'),
        ('F','Female')
    )
    STATES = (
        (0, 'Active'),
        (1, 'Banned')
    )

    account_id = models.AutoField(primary_key=True, db_column='account_id', verbose_name='Account ID')
    username = models.CharField(unique=True, max_length=23, db_column='userid')
    password = models.CharField(max_length=32, db_column='user_pass')
    sex = models.CharField(max_length=1, choices=SEX, default='M')
    email = models.EmailField(unique=True, max_length=39)
    group_id = models.IntegerField(null=False, blank=True, default=0)
    state = models.PositiveIntegerField(choices=STATES, default=0, null=False)
    unban_time = models.PositiveIntegerField(null=False, blank=True, default = 0) # TODO
    expiration_time = models.PositiveIntegerField(null=False, blank=True, default=0) # TODO
    logincount = models.PositiveIntegerField(null=False, blank=True, default=0)
    last_login = models.DateTimeField(blank=True, null=True, db_column='lastlogin') # TODO 1
    last_ip = models.CharField(max_length=100, null=False, blank=True)
    birthdate = models.DateField(null=True, default='2020-01-01') # TODO
    character_slots = models.PositiveIntegerField(null=False, blank=False, default=12)
    pincode = models.CharField(max_length=4)
    pincode_change = models.PositiveIntegerField(null=False, default=0)
    vip_time = models.PositiveIntegerField(null=False, default=0)
    old_group = models.IntegerField(null=False, default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['sex','email','birthdate']

    @property
    def is_superuser(self):
        if self.group_id > 0:
            return True
        return False

    @property
    def is_staff(self):
        if self.group_id > 0:
            return True
        return False

    @property
    def is_active(self):
        return True
        
    @property
    def first_name(self):
        return self.username
        
    @property
    def last_name(self):
        return self.username
        
    @property
    def date_joined(self):
        return self.birthdate
        
    class Meta:
        managed = True
        db_table = "login"
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'