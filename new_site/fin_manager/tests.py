# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import models as my_models
# Create your tests here.
class Mytest(TestCase):
    def SetUp(self):
        my_models.User.objects.create_user(username='testing', password='testing')
        my_models.Categories.objects.create(name='testing_category',owner='testing')
        my_models.Wallets.objects.create(name='testing_wallet',owner='testing')
        self.category = my_models.Categories.objects.get(name='testing_category')
        self.wallet = my_models.Wallets.objects.get(name='testing_wallet')
        my_models.Transactions.objects.create(title='my transactions',amount=50,wallet_id=self.wallet.name,category=self.category.name)
    def testget(self):
        print ("dupa")