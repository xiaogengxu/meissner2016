from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import math, datetime
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _


class Start(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60


class Period1(Page):
    form_model = 'player'
    form_fields = ['spend_save1', 'check_spend_save1']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend_save1']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income_save1 = self.player.income_save1
        wealth_save1 = self.participant.vars['wealth_save1']
        return {'lang': lang,
                'income_save1': income_save1,
                'wealth_save1': wealth_save1}

    def before_next_page(self):
        self.participant.vars['spend_save1'] = self.player.spend_save1
        self.participant.vars['saving_save1'] = self.player.income_save1 - self.player.spend_save1
        self.participant.vars['wealth_save2'] = self.participant.vars['wealth_save1'] + self.player.income_save1 - self.player.spend_save1
        self.participant.vars['points_save1'] = 250 * (1 - math.exp(-0.02 * self.player.spend_save1)) * 1.5589


class Period2(Page):
    form_model = 'player'
    form_fields = ['spend_save2', 'check_spend_save2']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend_save2']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income_save1 = self.player.income_save1
        spend_save1 = self.participant.vars['spend_save1']
        saving_save1 = self.player.income_save1 - self.participant.vars['spend_save1']
        wealth_save1 = self.participant.vars['wealth_save1']
        points_save1 = int(round(self.participant.vars['points_save1'], 0))

        income_save2 = self.player.income_save2
        wealth_save2 = self.participant.vars['wealth_save2']

        return {'lang': lang,
                'income_save1': income_save1,
                'spend_save1': spend_save1,
                'saving_save1': saving_save1,
                'wealth_save1': wealth_save1,
                'points_save1': points_save1,
                'income_save2': income_save2,
                'wealth_save2': wealth_save2}

    def before_next_page(self):
        self.participant.vars['spend_save2'] = self.player.spend_save2
        self.participant.vars['saving_save2'] = self.player.income_save2 - self.player.spend_save2
        self.participant.vars['wealth_save3'] = self.participant.vars['wealth_save2'] + self.player.income_save2 - self.player.spend_save2
        self.participant.vars['points_save2'] = 250 * (1 - math.exp(-0.02 * self.player.spend_save2)) * 1.5589


class Period3(Page):
    form_model = 'player'
    form_fields = ['spend_save3', 'check_spend_save3']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend_save3']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income_save1 = self.player.income_save1
        spend_save1 = self.participant.vars['spend_save1']
        saving_save1 = self.player.income_save1 - self.participant.vars['spend_save1']
        wealth_save1 = self.participant.vars['wealth_save1']
        points_save1 = int(round(self.participant.vars['points_save1'], 0))

        income_save2 = self.player.income_save2
        spend_save2 = self.participant.vars['spend_save2']
        saving_save2 = self.player.income_save2 - self.participant.vars['spend_save2']
        wealth_save2 = self.participant.vars['wealth_save2']
        points_save2 = int(round(self.participant.vars['points_save2'], 0))

        income_save3 = self.player.income_save3
        wealth_save3 = self.participant.vars['wealth_save3']

        return {'lang': lang,
                'income_save1': income_save1,
                'spend_save1': spend_save1,
                'saving_save1': saving_save1,
                'wealth_save1': wealth_save1,
                'points_save1': points_save1,
                'income_save2': income_save2,
                'spend_save2': spend_save2,
                'saving_save2': saving_save2,
                'wealth_save2': wealth_save2,
                'points_save2': points_save2,
                'income_save3': income_save3,
                'wealth_save3': wealth_save3}

    def before_next_page(self):
        self.participant.vars['spend_save3'] = self.player.spend_save3
        self.participant.vars['saving_save3'] = self.player.income_save3 - self.player.spend_save3
        self.participant.vars['wealth_save4'] = self.participant.vars['wealth_save3'] + self.player.income_save3 - self.player.spend_save3
        self.participant.vars['points_save3'] = 250 * (1 - math.exp(-0.02 * self.player.spend_save3)) * 1.5589


class Period4(Page):
    form_model = 'player'
    form_fields = ['spend_save4', 'check_spend_save4']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend_save4']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income_save1 = self.player.income_save1
        spend_save1 = self.participant.vars['spend_save1']
        saving_save1 = self.player.income_save1 - self.participant.vars['spend_save1']
        wealth_save1 = self.participant.vars['wealth_save1']
        points_save1 = int(round(self.participant.vars['points_save1'], 0))

        income_save2 = self.player.income_save2
        spend_save2 = self.participant.vars['spend_save2']
        saving_save2 = self.player.income_save2 - self.participant.vars['spend_save2']
        wealth_save2 = self.participant.vars['wealth_save2']
        points_save2 = int(round(self.participant.vars['points_save2'], 0))

        income_save3 = self.player.income_save3
        spend_save3 = self.participant.vars['spend_save3']
        saving_save3 = self.player.income_save3 - self.participant.vars['spend_save3']
        wealth_save3 = self.participant.vars['wealth_save3']
        points_save3 = int(round(self.participant.vars['points_save3'], 0))

        income_save4 = self.player.income_save4
        wealth_save4 = self.participant.vars['wealth_save4']

        return {'lang': lang,
                'income_save1': income_save1,
                'spend_save1': spend_save1,
                'saving_save1': saving_save1,
                'wealth_save1': wealth_save1,
                'points_save1': points_save1,
                'income_save2': income_save2,
                'spend_save2': spend_save2,
                'saving_save2': saving_save2,
                'wealth_save2': wealth_save2,
                'points_save2': points_save2,
                'income_save3': income_save3,
                'spend_save3': spend_save3,
                'saving_save3': saving_save3,
                'wealth_save3': wealth_save3,
                'points_save3': points_save3,
                'income_save4': income_save4,
                'wealth_save4': wealth_save4}

    def before_next_page(self):
        self.participant.vars['spend_save4'] = self.player.spend_save4
        self.participant.vars['saving_save4'] = self.player.income_save4 - self.player.spend_save4
        self.participant.vars['wealth_save5'] = self.participant.vars['wealth_save4'] + self.player.income_save4 - self.player.spend_save4
        self.participant.vars['points_save4'] = 250 * (1 - math.exp(-0.02 * self.player.spend_save4)) * 1.5589


class Period5(Page):
    form_model = 'player'
    form_fields = ['spend_save5', 'check_spend_save5']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend_save5']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income_save1 = self.player.income_save1
        spend_save1 = self.participant.vars['spend_save1']
        saving_save1 = self.player.income_save1 - self.participant.vars['spend_save1']
        wealth_save1 = self.participant.vars['wealth_save1']
        points_save1 = int(round(self.participant.vars['points_save1'], 0))

        income_save2 = self.player.income_save2
        spend_save2 = self.participant.vars['spend_save2']
        saving_save2 = self.player.income_save2 - self.participant.vars['spend_save2']
        wealth_save2 = self.participant.vars['wealth_save2']
        points_save2 = int(round(self.participant.vars['points_save2'], 0))

        income_save3 = self.player.income_save3
        spend_save3 = self.participant.vars['spend_save3']
        saving_save3 = self.player.income_save3 - self.participant.vars['spend_save3']
        wealth_save3 = self.participant.vars['wealth_save3']
        points_save3 = int(round(self.participant.vars['points_save3'], 0))

        income_save4 = self.player.income_save4
        spend_save4 = self.participant.vars['spend_save4']
        saving_save4 = self.player.income_save4 - self.participant.vars['spend_save4']
        wealth_save4 = self.participant.vars['wealth_save4']
        points_save4 = int(round(self.participant.vars['points_save4'], 0))

        income_save5 = self.player.income_save5
        wealth_save5 = self.participant.vars['wealth_save5']

        return {'lang': lang,
                'income_save1': income_save1,
                'spend_save1': spend_save1,
                'saving_save1': saving_save1,
                'wealth_save1': wealth_save1,
                'points_save1': points_save1,
                'income_save2': income_save2,
                'spend_save2': spend_save2,
                'saving_save2': saving_save2,
                'wealth_save2': wealth_save2,
                'points_save2': points_save2,
                'income_save3': income_save3,
                'spend_save3': spend_save3,
                'saving_save3': saving_save3,
                'wealth_save3': wealth_save3,
                'points_save3': points_save3,
                'income_save4': income_save4,
                'spend_save4': spend_save4,
                'saving_save4': saving_save4,
                'wealth_save4': wealth_save4,
                'points_save4': points_save4,
                'income_save5': income_save5,
                'wealth_save5': wealth_save5}

    def before_next_page(self):
        self.participant.vars['spend_save5'] = self.player.spend_save5
        self.participant.vars['saving_save5'] = self.player.income_save5 - self.player.spend_save5
        self.participant.vars['wealth_save6'] = self.participant.vars['wealth_save5'] + self.player.income_save5 - self.player.spend_save5
        self.participant.vars['points_save5'] = 250 * (1 - math.exp(-0.02 * self.player.spend_save5)) * 1.5589


class Period6(Page):
    form_model = 'player'
    form_fields = ['spend_save6', 'check_spend_save6']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend_save6']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income_save1 = self.player.income_save1
        spend_save1 = self.participant.vars['spend_save1']
        saving_save1 = self.player.income_save1 - self.participant.vars['spend_save1']
        wealth_save1 = self.participant.vars['wealth_save1']
        points_save1 = int(round(self.participant.vars['points_save1'], 0))

        income_save2 = self.player.income_save2
        spend_save2 = self.participant.vars['spend_save2']
        saving_save2 = self.player.income_save2 - self.participant.vars['spend_save2']
        wealth_save2 = self.participant.vars['wealth_save2']
        points_save2 = int(round(self.participant.vars['points_save2'], 0))

        income_save3 = self.player.income_save3
        spend_save3 = self.participant.vars['spend_save3']
        saving_save3 = self.player.income_save3 - self.participant.vars['spend_save3']
        wealth_save3 = self.participant.vars['wealth_save3']
        points_save3 = int(round(self.participant.vars['points_save3'], 0))

        income_save4 = self.player.income_save4
        spend_save4 = self.participant.vars['spend_save4']
        saving_save4 = self.player.income_save4 - self.participant.vars['spend_save4']
        wealth_save4 = self.participant.vars['wealth_save4']
        points_save4 = int(round(self.participant.vars['points_save4'], 0))

        income_save5 = self.player.income_save5
        spend_save5 = self.participant.vars['spend_save5']
        saving_save5 = self.player.income_save5 - self.participant.vars['spend_save5']
        wealth_save5 = self.participant.vars['wealth_save5']
        points_save5 = int(round(self.participant.vars['points_save5'], 0))

        income_save6 = self.player.income_save6
        wealth_save6 = self.participant.vars['wealth_save6']

        return {'lang': lang,
                'income_save1': income_save1,
                'spend_save1': spend_save1,
                'saving_save1': saving_save1,
                'wealth_save1': wealth_save1,
                'points_save1': points_save1,
                'income_save2': income_save2,
                'spend_save2': spend_save2,
                'saving_save2': saving_save2,
                'wealth_save2': wealth_save2,
                'points_save2': points_save2,
                'income_save3': income_save3,
                'spend_save3': spend_save3,
                'saving_save3': saving_save3,
                'wealth_save3': wealth_save3,
                'points_save3': points_save3,
                'income_save4': income_save4,
                'spend_save4': spend_save4,
                'saving_save4': saving_save4,
                'wealth_save4': wealth_save4,
                'points_save4': points_save4,
                'income_save5': income_save5,
                'spend_save5': spend_save5,
                'saving_save5': saving_save5,
                'wealth_save5': wealth_save5,
                'points_save5': points_save5,
                'income_save6': income_save6,
                'wealth_save6': wealth_save6}

    def before_next_page(self):
        self.participant.vars['spend_save6'] = self.player.spend_save6
        self.participant.vars['saving_save6'] = self.player.income_save6 - self.player.spend_save6
        self.participant.vars['wealth_save7'] = self.participant.vars['wealth_save6'] + self.player.income_save6 - self.player.spend_save6
        self.participant.vars['points_save6'] = 250 * (1 - math.exp(-0.02 * self.player.spend_save6)) * 1.5589


class Period7(Page):
    form_model = 'player'
    form_fields = ['spend_save7', 'check_spend_save7']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend_save7']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income_save1 = self.player.income_save1
        spend_save1 = self.participant.vars['spend_save1']
        saving_save1 = self.player.income_save1 - self.participant.vars['spend_save1']
        wealth_save1 = self.participant.vars['wealth_save1']
        points_save1 = int(round(self.participant.vars['points_save1'], 0))

        income_save2 = self.player.income_save2
        spend_save2 = self.participant.vars['spend_save2']
        saving_save2 = self.player.income_save2 - self.participant.vars['spend_save2']
        wealth_save2 = self.participant.vars['wealth_save2']
        points_save2 = int(round(self.participant.vars['points_save2'], 0))

        income_save3 = self.player.income_save3
        spend_save3 = self.participant.vars['spend_save3']
        saving_save3 = self.player.income_save3 - self.participant.vars['spend_save3']
        wealth_save3 = self.participant.vars['wealth_save3']
        points_save3 = int(round(self.participant.vars['points_save3'], 0))

        income_save4 = self.player.income_save4
        spend_save4 = self.participant.vars['spend_save4']
        saving_save4 = self.player.income_save4 - self.participant.vars['spend_save4']
        wealth_save4 = self.participant.vars['wealth_save4']
        points_save4 = int(round(self.participant.vars['points_save4'], 0))

        income_save5 = self.player.income_save5
        spend_save5 = self.participant.vars['spend_save5']
        saving_save5 = self.player.income_save5 - self.participant.vars['spend_save5']
        wealth_save5 = self.participant.vars['wealth_save5']
        points_save5 = int(round(self.participant.vars['points_save5'], 0))

        income_save6 = self.player.income_save6
        spend_save6 = self.participant.vars['spend_save6']
        saving_save6 = self.player.income_save6 - self.participant.vars['spend_save6']
        wealth_save6 = self.participant.vars['wealth_save6']
        points_save6 = int(round(self.participant.vars['points_save6'], 0))

        income_save7 = self.player.income_save7
        wealth_save7 = self.participant.vars['wealth_save7']

        return {'lang': lang,
                'income_save1': income_save1,
                'spend_save1': spend_save1,
                'saving_save1': saving_save1,
                'wealth_save1': wealth_save1,
                'points_save1': points_save1,
                'income_save2': income_save2,
                'spend_save2': spend_save2,
                'saving_save2': saving_save2,
                'wealth_save2': wealth_save2,
                'points_save2': points_save2,
                'income_save3': income_save3,
                'spend_save3': spend_save3,
                'saving_save3': saving_save3,
                'wealth_save3': wealth_save3,
                'points_save3': points_save3,
                'income_save4': income_save4,
                'spend_save4': spend_save4,
                'saving_save4': saving_save4,
                'wealth_save4': wealth_save4,
                'points_save4': points_save4,
                'income_save5': income_save5,
                'spend_save5': spend_save5,
                'saving_save5': saving_save5,
                'wealth_save5': wealth_save5,
                'points_save5': points_save5,
                'income_save6': income_save6,
                'spend_save6': spend_save6,
                'saving_save6': saving_save6,
                'wealth_save6': wealth_save6,
                'points_save6': points_save6,
                'income_save7': income_save7,
                'wealth_save7': wealth_save7}

    def before_next_page(self):
        self.participant.vars['spend_save7'] = self.player.spend_save7
        self.participant.vars['saving_save7'] = self.player.income_save7 - self.player.spend_save7
        self.participant.vars['wealth_save8'] = self.participant.vars['wealth_save7'] + self.player.income_save7 - self.player.spend_save7
        self.participant.vars['points_save7'] = 250 * (1 - math.exp(-0.02 * self.player.spend_save7)) * 1.5589


class Period8(Page):
    form_model = 'player'
    form_fields = ['spend_save8', 'check_spend_save8']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend_save8']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income_save1 = self.player.income_save1
        spend_save1 = self.participant.vars['spend_save1']
        saving_save1 = self.player.income_save1 - self.participant.vars['spend_save1']
        wealth_save1 = self.participant.vars['wealth_save1']
        points_save1 = int(round(self.participant.vars['points_save1'], 0))

        income_save2 = self.player.income_save2
        spend_save2 = self.participant.vars['spend_save2']
        saving_save2 = self.player.income_save2 - self.participant.vars['spend_save2']
        wealth_save2 = self.participant.vars['wealth_save2']
        points_save2 = int(round(self.participant.vars['points_save2'], 0))

        income_save3 = self.player.income_save3
        spend_save3 = self.participant.vars['spend_save3']
        saving_save3 = self.player.income_save3 - self.participant.vars['spend_save3']
        wealth_save3 = self.participant.vars['wealth_save3']
        points_save3 = int(round(self.participant.vars['points_save3'], 0))

        income_save4 = self.player.income_save4
        spend_save4 = self.participant.vars['spend_save4']
        saving_save4 = self.player.income_save4 - self.participant.vars['spend_save4']
        wealth_save4 = self.participant.vars['wealth_save4']
        points_save4 = int(round(self.participant.vars['points_save4'], 0))

        income_save5 = self.player.income_save5
        spend_save5 = self.participant.vars['spend_save5']
        saving_save5 = self.player.income_save5 - self.participant.vars['spend_save5']
        wealth_save5 = self.participant.vars['wealth_save5']
        points_save5 = int(round(self.participant.vars['points_save5'], 0))

        income_save6 = self.player.income_save6
        spend_save6 = self.participant.vars['spend_save6']
        saving_save6 = self.player.income_save6 - self.participant.vars['spend_save6']
        wealth_save6 = self.participant.vars['wealth_save6']
        points_save6 = int(round(self.participant.vars['points_save6'], 0))

        income_save7 = self.player.income_save7
        spend_save7 = self.participant.vars['spend_save7']
        saving_save7 = self.player.income_save7 - self.participant.vars['spend_save7']
        wealth_save7 = self.participant.vars['wealth_save7']
        points_save7 = int(round(self.participant.vars['points_save7'], 0))

        income_save8 = self.player.income_save8
        wealth_save8 = self.participant.vars['wealth_save8']

        return {'lang': lang,
                'income_save1': income_save1,
                'spend_save1': spend_save1,
                'saving_save1': saving_save1,
                'wealth_save1': wealth_save1,
                'points_save1': points_save1,
                'income_save2': income_save2,
                'spend_save2': spend_save2,
                'saving_save2': saving_save2,
                'wealth_save2': wealth_save2,
                'points_save2': points_save2,
                'income_save3': income_save3,
                'spend_save3': spend_save3,
                'saving_save3': saving_save3,
                'wealth_save3': wealth_save3,
                'points_save3': points_save3,
                'income_save4': income_save4,
                'spend_save4': spend_save4,
                'saving_save4': saving_save4,
                'wealth_save4': wealth_save4,
                'points_save4': points_save4,
                'income_save5': income_save5,
                'spend_save5': spend_save5,
                'saving_save5': saving_save5,
                'wealth_save5': wealth_save5,
                'points_save5': points_save5,
                'income_save6': income_save6,
                'spend_save6': spend_save6,
                'saving_save6': saving_save6,
                'wealth_save6': wealth_save6,
                'points_save6': points_save6,
                'income_save7': income_save7,
                'spend_save7': spend_save7,
                'saving_save7': saving_save7,
                'wealth_save7': wealth_save7,
                'points_save7': points_save7,
                'income_save8': income_save8,
                'wealth_save8': wealth_save8}

    def before_next_page(self):
        self.participant.vars['spend_save8'] = self.player.spend_save8
        self.participant.vars['saving_save8'] = self.player.income_save8 - self.player.spend_save8
        self.participant.vars['wealth_save9'] = self.participant.vars['wealth_save8'] + self.player.income_save8 - self.player.spend_save8
        self.participant.vars['points_save8'] = 250 * (1 - math.exp(-0.02 * self.player.spend_save8)) * 1.5589


class Period9(Page):
    form_model = 'player'
    form_fields = ['spend_save9', 'check_spend_save9']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend_save9']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income_save1 = self.player.income_save1
        spend_save1 = self.participant.vars['spend_save1']
        saving_save1 = self.player.income_save1 - self.participant.vars['spend_save1']
        wealth_save1 = self.participant.vars['wealth_save1']
        points_save1 = int(round(self.participant.vars['points_save1'], 0))

        income_save2 = self.player.income_save2
        spend_save2 = self.participant.vars['spend_save2']
        saving_save2 = self.player.income_save2 - self.participant.vars['spend_save2']
        wealth_save2 = self.participant.vars['wealth_save2']
        points_save2 = int(round(self.participant.vars['points_save2'], 0))

        income_save3 = self.player.income_save3
        spend_save3 = self.participant.vars['spend_save3']
        saving_save3 = self.player.income_save3 - self.participant.vars['spend_save3']
        wealth_save3 = self.participant.vars['wealth_save3']
        points_save3 = int(round(self.participant.vars['points_save3'], 0))

        income_save4 = self.player.income_save4
        spend_save4 = self.participant.vars['spend_save4']
        saving_save4 = self.player.income_save4 - self.participant.vars['spend_save4']
        wealth_save4 = self.participant.vars['wealth_save4']
        points_save4 = int(round(self.participant.vars['points_save4'], 0))

        income_save5 = self.player.income_save5
        spend_save5 = self.participant.vars['spend_save5']
        saving_save5 = self.player.income_save5 - self.participant.vars['spend_save5']
        wealth_save5 = self.participant.vars['wealth_save5']
        points_save5 = int(round(self.participant.vars['points_save5'], 0))

        income_save6 = self.player.income_save6
        spend_save6 = self.participant.vars['spend_save6']
        saving_save6 = self.player.income_save6 - self.participant.vars['spend_save6']
        wealth_save6 = self.participant.vars['wealth_save6']
        points_save6 = int(round(self.participant.vars['points_save6'], 0))

        income_save7 = self.player.income_save7
        spend_save7 = self.participant.vars['spend_save7']
        saving_save7 = self.player.income_save7 - self.participant.vars['spend_save7']
        wealth_save7 = self.participant.vars['wealth_save7']
        points_save7 = int(round(self.participant.vars['points_save7'], 0))

        income_save8 = self.player.income_save8
        spend_save8 = self.participant.vars['spend_save8']
        saving_save8 = self.player.income_save8 - self.participant.vars['spend_save8']
        wealth_save8 = self.participant.vars['wealth_save8']
        points_save8 = int(round(self.participant.vars['points_save8'], 0))

        income_save9 = self.player.income_save9
        wealth_save9 = self.participant.vars['wealth_save9']

        return {'lang': lang,
                'income_save1': income_save1,
                'spend_save1': spend_save1,
                'saving_save1': saving_save1,
                'wealth_save1': wealth_save1,
                'points_save1': points_save1,
                'income_save2': income_save2,
                'spend_save2': spend_save2,
                'saving_save2': saving_save2,
                'wealth_save2': wealth_save2,
                'points_save2': points_save2,
                'income_save3': income_save3,
                'spend_save3': spend_save3,
                'saving_save3': saving_save3,
                'wealth_save3': wealth_save3,
                'points_save3': points_save3,
                'income_save4': income_save4,
                'spend_save4': spend_save4,
                'saving_save4': saving_save4,
                'wealth_save4': wealth_save4,
                'points_save4': points_save4,
                'income_save5': income_save5,
                'spend_save5': spend_save5,
                'saving_save5': saving_save5,
                'wealth_save5': wealth_save5,
                'points_save5': points_save5,
                'income_save6': income_save6,
                'spend_save6': spend_save6,
                'saving_save6': saving_save6,
                'wealth_save6': wealth_save6,
                'points_save6': points_save6,
                'income_save7': income_save7,
                'spend_save7': spend_save7,
                'saving_save7': saving_save7,
                'wealth_save7': wealth_save7,
                'points_save7': points_save7,
                'income_save8': income_save8,
                'spend_save8': spend_save8,
                'saving_save8': saving_save8,
                'wealth_save8': wealth_save8,
                'points_save8': points_save8,
                'income_save9': income_save9,
                'wealth_save9': wealth_save9}

    def before_next_page(self):
        self.participant.vars['spend_save9'] = self.player.spend_save9
        self.participant.vars['saving_save9'] = self.player.income_save9 - self.player.spend_save9
        self.participant.vars['wealth_save10'] = self.participant.vars['wealth_save9'] + self.player.income_save9 - self.player.spend_save9
        self.participant.vars['points_save9'] = 250 * (1 - math.exp(-0.02 * self.player.spend_save9)) * 1.5589
        self.participant.vars['spend_save10'] = self.participant.vars['wealth_save9'] + self.player.income_save9 - self.player.spend_save9 + \
                                           self.player.income_save10
        self.player.spend_save10 = self.participant.vars['wealth_save9'] + self.player.income_save9 - self.player.spend_save9 + \
                              self.player.income_save10


class Period10(Page):
    form_model = 'player'
    form_fields = ['points_total_save']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income_save1 = self.player.income_save1
        spend_save1 = self.participant.vars['spend_save1']
        saving_save1 = self.player.income_save1 - self.participant.vars['spend_save1']
        wealth_save1 = self.participant.vars['wealth_save1']
        points_save1 = int(round(self.participant.vars['points_save1'], 0))

        income_save2 = self.player.income_save2
        spend_save2 = self.participant.vars['spend_save2']
        saving_save2 = self.player.income_save2 - self.participant.vars['spend_save2']
        wealth_save2 = self.participant.vars['wealth_save2']
        points_save2 = int(round(self.participant.vars['points_save2'], 0))

        income_save3 = self.player.income_save3
        spend_save3 = self.participant.vars['spend_save3']
        saving_save3 = self.player.income_save3 - self.participant.vars['spend_save3']
        wealth_save3 = self.participant.vars['wealth_save3']
        points_save3 = int(round(self.participant.vars['points_save3'], 0))

        income_save4 = self.player.income_save4
        spend_save4 = self.participant.vars['spend_save4']
        saving_save4 = self.player.income_save4 - self.participant.vars['spend_save4']
        wealth_save4 = self.participant.vars['wealth_save4']
        points_save4 = int(round(self.participant.vars['points_save4'], 0))

        income_save5 = self.player.income_save5
        spend_save5 = self.participant.vars['spend_save5']
        saving_save5 = self.player.income_save5 - self.participant.vars['spend_save5']
        wealth_save5 = self.participant.vars['wealth_save5']
        points_save5 = int(round(self.participant.vars['points_save5'], 0))

        income_save6 = self.player.income_save6
        spend_save6 = self.participant.vars['spend_save6']
        saving_save6 = self.player.income_save6 - self.participant.vars['spend_save6']
        wealth_save6 = self.participant.vars['wealth_save6']
        points_save6 = int(round(self.participant.vars['points_save6'], 0))

        income_save7 = self.player.income_save7
        spend_save7 = self.participant.vars['spend_save7']
        saving_save7 = self.player.income_save7 - self.participant.vars['spend_save7']
        wealth_save7 = self.participant.vars['wealth_save7']
        points_save7 = int(round(self.participant.vars['points_save7'], 0))

        income_save8 = self.player.income_save8
        spend_save8 = self.participant.vars['spend_save8']
        saving_save8 = self.player.income_save8 - self.participant.vars['spend_save8']
        wealth_save8 = self.participant.vars['wealth_save8']
        points_save8 = int(round(self.participant.vars['points_save8'], 0))

        income_save9 = self.player.income_save9
        spend_save9 = self.participant.vars['spend_save9']
        saving_save9 = self.player.income_save9 - self.participant.vars['spend_save9']
        wealth_save9 = self.participant.vars['wealth_save9']
        points_save9 = int(round(self.participant.vars['points_save9'], 0))

        income_save10 = self.player.income_save10
        spend_save10 = self.participant.vars['spend_save10']
        saving_save10 = self.player.income_save10 - self.participant.vars['spend_save10']
        wealth_save10 = self.participant.vars['wealth_save10']
        points_save10_num = 250 * (1 - math.exp(-0.02 * self.participant.vars['spend_save10'])) * 1.5589
        points_save10 = int(round(points_save10_num, 0))

        return {'lang': lang,
                'income_save1': income_save1,
                'spend_save1': spend_save1,
                'saving_save1': saving_save1,
                'wealth_save1': wealth_save1,
                'points_save1': points_save1,
                'income_save2': income_save2,
                'spend_save2': spend_save2,
                'saving_save2': saving_save2,
                'wealth_save2': wealth_save2,
                'points_save2': points_save2,
                'income_save3': income_save3,
                'spend_save3': spend_save3,
                'saving_save3': saving_save3,
                'wealth_save3': wealth_save3,
                'points_save3': points_save3,
                'income_save4': income_save4,
                'spend_save4': spend_save4,
                'saving_save4': saving_save4,
                'wealth_save4': wealth_save4,
                'points_save4': points_save4,
                'income_save5': income_save5,
                'spend_save5': spend_save5,
                'saving_save5': saving_save5,
                'wealth_save5': wealth_save5,
                'points_save5': points_save5,
                'income_save6': income_save6,
                'spend_save6': spend_save6,
                'saving_save6': saving_save6,
                'wealth_save6': wealth_save6,
                'points_save6': points_save6,
                'income_save7': income_save7,
                'spend_save7': spend_save7,
                'saving_save7': saving_save7,
                'wealth_save7': wealth_save7,
                'points_save7': points_save7,
                'income_save8': income_save8,
                'spend_save8': spend_save8,
                'saving_save8': saving_save8,
                'wealth_save8': wealth_save8,
                'points_save8': points_save8,
                'income_save9': income_save9,
                'spend_save9': spend_save9,
                'saving_save9': saving_save9,
                'wealth_save9': wealth_save9,
                'points_save9': points_save9,
                'income_save10': income_save10,
                'spend_save10': spend_save10,
                'saving_save10': saving_save10,
                'wealth_save10': wealth_save10,
                'points_save10': points_save10}

    def before_next_page(self):
        points_save10_num = 250 * (1 - math.exp(-0.02 * self.player.spend_save10)) * 1.5589
        self.participant.vars['points_save10'] = int(round(points_save10_num, 0))
        points_save_total_num = 0
        for k in range(1, 11):
            str_points_save = 'points_save%s' % k
            points_save_total_num += self.participant.vars[str_points_save]
        if points_save_total_num < 0:
            self.player.points_total_save = 0
        else:
            self.player.points_total_save = int(round(points_save_total_num, 0))


class Summary(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        points_total1_num = self.player.in_round(1).points_total_save
        points_total1 = int(round(points_total1_num, 0))
        return {
            'points_total1': points_total1
        }

    def before_next_page(self):
        self.participant.vars['points_total1_save'] = self.player.in_round(1).points_total_save


class End(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60


page_sequence = [Start, Period1, Period2, Period3, Period4, Period5, Period6, Period7, Period8, Period9, Period10,
                 Summary, End]
