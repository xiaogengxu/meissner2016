from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _
import time


def get_timeout_seconds(player):
    return player.participant.vars['expiry'] - time.time()


class Info(Page):
    form_model = 'player'
    form_fields = ['birth_year', 'gender', 'education', 'finance_ability', 'income']
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60 and self.participant.vars['end'] == 0 \
               and get_timeout_seconds(self.player) > 3

    def error_message(self, values):
        if not values['birth_year'] or not values['gender'] or not values['education'] or not values['finance_ability'] \
                or not values['income']:
            return _('Please answer all questions.')

        if values['birth_year']:
            if values['birth_year'] < 1900 or values['birth_year'] > 2021:
                return _('Please input a sensible year of birth.')


class Risk_pref(Page):
    form_model = 'player'
    form_fields = ['risk_choice', 'check_risk_choice']
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60 and self.participant.vars['end'] == 0 \
               and get_timeout_seconds(self.player) > 3

    def error_message(self, values):
        if not values['check_risk_choice']:
            return _('Please decide the amount of reward you would like to put in the risky investment.')

    def before_next_page(self):
        self.participant.vars['risk_choice'] = self.player.risk_choice
        self.participant.vars['safe_choice'] = 100 - self.player.risk_choice
        if self.participant.vars['risk_outcome'] == 'win':
            self.participant.vars['new_reward'] = (2.5 * self.player.risk_choice + 100) / 100 * \
                                                  self.participant.vars['reward']
        else:
            self.participant.vars['new_reward'] = (100 - self.player.risk_choice) / 100 * self.participant.vars['reward']

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        return {'lang': lang}


class Time_pref(Page):
    form_model = 'player'
    form_fields = ['time_choice']
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60 and self.participant.vars['end'] == 0 \
               and get_timeout_seconds(self.player) > 3

    def error_message(self, values):
        if not values['time_choice']:
            return _('Please choose one of the options.')

    def before_next_page(self):
        self.participant.vars['time_choice'] = self.player.time_choice


page_sequence = [Info, Risk_pref, Time_pref]
