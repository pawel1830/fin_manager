# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    New User extend default django User model,
    set username as primary key and set first name, last name and email to required
    """
    username = models.CharField(primary_key=True, max_length=50, unique=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    class Meta:
        db_table = 'Users'


class Categories(models.Model):
    """
    This model is used to collect transaction categories,
    it's necessary to group of transactions for better management and visualization it

    """
    name = models.CharField(max_length=50, unique=True, primary_key=True)
    public = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Categories'


class Wallets(models.Model):
    """
    In the assumption One user can create more than one wallets.
    Why? Because User can have more than one bank account
    """
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Wallets'


class Transactions(models.Model):
    """
    This model save every operation in user wallet, deposit and withdrawal and another?
    """
    transaction_choices = (
        ('+','in'),
        ('-','out')
    )
    title = models.CharField(max_length=80, default="Transaction without title")
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    wallet_id = models.ForeignKey(Wallets, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    const = models.BooleanField(default=False)
    transaction_type = models.CharField(choices=transaction_choices,max_length=1,default='+')
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Transactions'
