from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from django.utils.translation import ugettext_lazy as _
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'decision-making'
    players_per_group = None
    num_rounds = 2
    income_rdm = [-10, 10]


class Subsession(BaseSubsession):
    def creating_session(self):
        def myfun(a):
            income_rdm_seq = Constants.income_rdm.copy()
            income_num = 10 * a + random.choice(income_rdm_seq)
            return income_num

        for r in range(1, 3):
            for player in self.in_round(r).get_players():
                player.participant.vars['wealth1'] = 0
                for j in range(1, 11):
                    income = myfun(j)
                    str_income = 'income%s' % j
                    setattr(player.in_round(r), str_income, income)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    income1 = models.IntegerField(blank=True)
    income2 = models.IntegerField(blank=True)
    income3 = models.IntegerField(blank=True)
    income4 = models.IntegerField(blank=True)
    income5 = models.IntegerField(blank=True)
    income6 = models.IntegerField(blank=True)
    income7 = models.IntegerField(blank=True)
    income8 = models.IntegerField(blank=True)
    income9 = models.IntegerField(blank=True)
    income10 = models.IntegerField(blank=True)

    spend1 = models.IntegerField()
    check_spend1 = models.IntegerField(blank=True)

    spend2 = models.IntegerField()
    check_spend2 = models.IntegerField(blank=True)

    spend3 = models.IntegerField()
    check_spend3 = models.IntegerField(blank=True)

    spend4 = models.IntegerField()
    check_spend4 = models.IntegerField(blank=True)

    spend5 = models.IntegerField()
    check_spend5 = models.IntegerField(blank=True)

    spend6 = models.IntegerField()
    check_spend6 = models.IntegerField(blank=True)

    spend7 = models.IntegerField()
    check_spend7 = models.IntegerField(blank=True)

    spend8 = models.IntegerField()
    check_spend8 = models.IntegerField(blank=True)

    spend9 = models.IntegerField()
    check_spend9 = models.IntegerField(blank=True)

    spend10 = models.IntegerField(blank=True)

    points_total = models.FloatField(blank=True)
    total_time = models.IntegerField(blank=True)
