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
import random
from django.utils.translation import ugettext_lazy as _


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'decision-making1'
    players_per_group = None
    num_rounds = 2
    income_rdm = [-10, 10]


class Subsession(BaseSubsession):
    def creating_session(self):
        def myfun(a):
            income_rdm_seq = Constants.income_rdm.copy()
            income_num = 110 - 10 * a + random.choice(income_rdm_seq)
            return income_num

        for r in range(1, 3):
            for player in self.in_round(r).get_players():
                player.participant.vars['wealth_save1'] = 0
                for j in range(1, 11):
                    income = myfun(j)
                    str_income = 'income_save%s' % j
                    setattr(player.in_round(r), str_income, income)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    income_save1 = models.IntegerField(blank=True)
    income_save2 = models.IntegerField(blank=True)
    income_save3 = models.IntegerField(blank=True)
    income_save4 = models.IntegerField(blank=True)
    income_save5 = models.IntegerField(blank=True)
    income_save6 = models.IntegerField(blank=True)
    income_save7 = models.IntegerField(blank=True)
    income_save8 = models.IntegerField(blank=True)
    income_save9 = models.IntegerField(blank=True)
    income_save10 = models.IntegerField(blank=True)

    spend_save1 = models.IntegerField()
    check_spend_save1 = models.IntegerField(blank=True)

    spend_save2 = models.IntegerField()
    check_spend_save2 = models.IntegerField(blank=True)

    spend_save3 = models.IntegerField()
    check_spend_save3 = models.IntegerField(blank=True)

    spend_save4 = models.IntegerField()
    check_spend_save4 = models.IntegerField(blank=True)

    spend_save5 = models.IntegerField()
    check_spend_save5 = models.IntegerField(blank=True)

    spend_save6 = models.IntegerField()
    check_spend_save6 = models.IntegerField(blank=True)

    spend_save7 = models.IntegerField()
    check_spend_save7 = models.IntegerField(blank=True)

    spend_save8 = models.IntegerField()
    check_spend_save8 = models.IntegerField(blank=True)

    spend_save9 = models.IntegerField()
    check_spend_save9 = models.IntegerField(blank=True)

    spend_save10 = models.IntegerField(blank=True)

    points_total_save = models.FloatField(blank=True)
    total_time_save = models.IntegerField()
