from models import Wallets
import logging
from django.db.models import Sum, Case, When, F, IntegerField
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
# add the handlers to the logger

logger.addHandler(ch)
def wallets_list(context):
    sum_pay = Case(When(transactions__transaction_type='+', then=F('transactions__amount')), default=0,
         output_field=IntegerField())
    sum_payoff = Case(When(transactions__transaction_type='-', then=F('transactions__amount')), default=0,
                   output_field=IntegerField())
    wallets = Wallets.objects.filter(owner=context.user.username).annotate(sum_pay=Sum(sum_pay),sum_payoff=Sum(sum_payoff))
    return {'wallets_list' :wallets}