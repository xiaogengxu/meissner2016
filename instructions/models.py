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

def seq_to_dict(s):
    r = {}
    l = len(s) - 1
    for i, j in enumerate(s):
        if i < l:
            r[j] = s[i + 1]
        else:
            r[j] = None
    return r


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1

    seq_treat = ['borrow_first', 'save_first']


class Subsession(BaseSubsession):
    def creating_session(self):
        app_seq = self.session.config.get('app_sequence')
        for p in self.get_players():
            seq_treatment = Constants.seq_treat.copy()
            p.treatment = random.choice(seq_treatment)
            p.participant.vars['treatment'] = p.treatment
            p.participant.vars['finished'] = ''
            app_instruction, app_trial1, app_trial2, app_quiz, app_decision1, app_decision2, app_post, app_result \
                = app_seq
            if p.treatment == 'borrow_first':
                new_app_seq = [app_instruction] + [app_trial1] + [app_quiz] + [app_decision1] + [app_decision2] \
                              + [app_post] + [app_result]
            else:
                new_app_seq = [app_instruction] + [app_trial2] + [app_quiz] + [app_decision2] + [app_decision1] \
                              + [app_post] + [app_result]
            p.participant.vars['_updated_seq_apps'] = seq_to_dict(new_app_seq)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()
    time_instruction = models.IntegerField()
    consent = models.StringField(
        label=_('Do you want to start the simulation?'),
        choices=[('yes', _('Yes')), ('no', _('No'))]
    )
    lang = models.StringField(
        label='Bitte wählen Sie Ihre Sprache. / Please, select your language.',
        choices=[('de', 'Deutsch'), ('en', 'English')],
        widget=widgets.RadioSelect,
        initial='de',
        blank=True
    )
    username = models.StringField(blank=True)
