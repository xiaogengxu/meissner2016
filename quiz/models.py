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
    name_in_url = 'quiz'
    players_per_group = None
    num_rounds = 1

    rdm_seq = ['borrow', 'save']
    rdm_round = [1, 2]


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():

            player.participant.vars['mis_q1'] = 0
            player.participant.vars['mis_q2'] = 0
            player.participant.vars['mis_q3'] = 0
            player.participant.vars['mis_q4'] = 0
            player.participant.vars['mis_q5'] = 0
            player.participant.vars['mis_q6'] = 0
            player.participant.vars['end'] = 0

            rdm_seq_list = Constants.rdm_seq.copy()
            rdm_round_list = Constants.rdm_round.copy()
            chosen = random.choice(rdm_seq_list)
            round_chosen = random.choice(rdm_round_list)
            player.part_chosen = chosen
            player.round_chosen = round_chosen
            player.participant.vars['part_chosen'] = chosen
            player.participant.vars['round_chosen'] = round_chosen
            if chosen == 'borrow':
                player.participant.vars['round_chosen_borrow'] = round_chosen
            else:
                player.participant.vars['round_chosen_save'] = round_chosen


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    part_chosen = models.StringField(blank=True)
    round_chosen = models.IntegerField(blank=True)

    trial = models.IntegerField(blank=True)
    quiz1 = models.StringField(
        label=_('1. How many periods are there in one simulated life?'),
        widget=widgets.RadioSelect
    )
    quiz2 = models.StringField(
        label=_('2. How is your Income measured?'),
        widget=widgets.RadioSelect
    )
    quiz3 = models.StringField(
        label=_('3. If you spend 50 points in a period, how many Eurocent rewards will you gather in the same period, '
                'approximately?'),
        widget=widgets.RadioSelect
    )
    quiz4 = models.StringField(
        label=_('4. How will your additional compensation be determined?'),
        widget=widgets.RadioSelect
    )
    quiz5 = models.StringField(
        label=_('5. Which of the following rules exist in the Investment Game?'),
        widget=widgets.RadioSelect
    )
    quiz6 = models.StringField(
        label=_('6. In a period, assume your Start Balance is 60, your Income is 40, and Your Spending decision is 70. '
                'What is your End Balance?'),
        widget=widgets.RadioSelect
    )
