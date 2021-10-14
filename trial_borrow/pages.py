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
    form_fields = ['spend1', 'check_spend1']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend1']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income1 = self.player.income1
        wealth1 = self.participant.vars['wealth1']
        return {'lang': lang,
                'income1': income1,
                'wealth1': wealth1}

    def before_next_page(self):
        self.participant.vars['spend1'] = self.player.spend1
        self.participant.vars['saving1'] = self.player.income1 - self.player.spend1
        self.participant.vars['wealth2'] = self.participant.vars['wealth1'] + self.player.income1 - self.player.spend1
        self.participant.vars['points1'] = 250 * (1 - math.exp(-0.02 * self.player.spend1)) * 1.5589


class Period2(Page):
    form_model = 'player'
    form_fields = ['spend2', 'check_spend2']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend2']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income1 = self.player.income1
        spend1 = self.participant.vars['spend1']
        saving1 = self.player.income1 - self.participant.vars['spend1']
        wealth1 = self.participant.vars['wealth1']
        points1 = int(round(self.participant.vars['points1'], 0))

        income2 = self.player.income2
        wealth2 = self.participant.vars['wealth2']

        return {'lang': lang,
                'income1': income1,
                'spend1': spend1,
                'saving1': saving1,
                'wealth1': wealth1,
                'points1': points1,
                'income2': income2,
                'wealth2': wealth2}

    def before_next_page(self):
        self.participant.vars['spend2'] = self.player.spend2
        self.participant.vars['saving2'] = self.player.income2 - self.player.spend2
        self.participant.vars['wealth3'] = self.participant.vars['wealth2'] + self.player.income2 - self.player.spend2
        self.participant.vars['points2'] = 250 * (1 - math.exp(-0.02 * self.player.spend2)) * 1.5589


class Period3(Page):
    form_model = 'player'
    form_fields = ['spend3', 'check_spend3']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend3']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income1 = self.player.income1
        spend1 = self.participant.vars['spend1']
        saving1 = self.player.income1 - self.participant.vars['spend1']
        wealth1 = self.participant.vars['wealth1']
        points1 = int(round(self.participant.vars['points1'], 0))

        income2 = self.player.income2
        spend2 = self.participant.vars['spend2']
        saving2 = self.player.income2 - self.participant.vars['spend2']
        wealth2 = self.participant.vars['wealth2']
        points2 = int(round(self.participant.vars['points2'], 0))

        income3 = self.player.income3
        wealth3 = self.participant.vars['wealth3']

        return {'lang': lang,
                'income1': income1,
                'spend1': spend1,
                'saving1': saving1,
                'wealth1': wealth1,
                'points1': points1,
                'income2': income2,
                'spend2': spend2,
                'saving2': saving2,
                'wealth2': wealth2,
                'points2': points2,
                'income3': income3,
                'wealth3': wealth3}

    def before_next_page(self):
        self.participant.vars['spend3'] = self.player.spend3
        self.participant.vars['saving3'] = self.player.income3 - self.player.spend3
        self.participant.vars['wealth4'] = self.participant.vars['wealth3'] + self.player.income3 - self.player.spend3
        self.participant.vars['points3'] = 250 * (1 - math.exp(-0.02 * self.player.spend3)) * 1.5589


class Period4(Page):
    form_model = 'player'
    form_fields = ['spend4', 'check_spend4']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend4']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income1 = self.player.income1
        spend1 = self.participant.vars['spend1']
        saving1 = self.player.income1 - self.participant.vars['spend1']
        wealth1 = self.participant.vars['wealth1']
        points1 = int(round(self.participant.vars['points1'], 0))

        income2 = self.player.income2
        spend2 = self.participant.vars['spend2']
        saving2 = self.player.income2 - self.participant.vars['spend2']
        wealth2 = self.participant.vars['wealth2']
        points2 = int(round(self.participant.vars['points2'], 0))

        income3 = self.player.income3
        spend3 = self.participant.vars['spend3']
        saving3 = self.player.income3 - self.participant.vars['spend3']
        wealth3 = self.participant.vars['wealth3']
        points3 = int(round(self.participant.vars['points3'], 0))

        income4 = self.player.income4
        wealth4 = self.participant.vars['wealth4']

        return {'lang': lang,
                'income1': income1,
                'spend1': spend1,
                'saving1': saving1,
                'wealth1': wealth1,
                'points1': points1,
                'income2': income2,
                'spend2': spend2,
                'saving2': saving2,
                'wealth2': wealth2,
                'points2': points2,
                'income3': income3,
                'spend3': spend3,
                'saving3': saving3,
                'wealth3': wealth3,
                'points3': points3,
                'income4': income4,
                'wealth4': wealth4}

    def before_next_page(self):
        self.participant.vars['spend4'] = self.player.spend4
        self.participant.vars['saving4'] = self.player.income4 - self.player.spend4
        self.participant.vars['wealth5'] = self.participant.vars['wealth4'] + self.player.income4 - self.player.spend4
        self.participant.vars['points4'] = 250 * (1 - math.exp(-0.02 * self.player.spend4)) * 1.5589


class Period5(Page):
    form_model = 'player'
    form_fields = ['spend5', 'check_spend5']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend5']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income1 = self.player.income1
        spend1 = self.participant.vars['spend1']
        saving1 = self.player.income1 - self.participant.vars['spend1']
        wealth1 = self.participant.vars['wealth1']
        points1 = int(round(self.participant.vars['points1'], 0))

        income2 = self.player.income2
        spend2 = self.participant.vars['spend2']
        saving2 = self.player.income2 - self.participant.vars['spend2']
        wealth2 = self.participant.vars['wealth2']
        points2 = int(round(self.participant.vars['points2'], 0))

        income3 = self.player.income3
        spend3 = self.participant.vars['spend3']
        saving3 = self.player.income3 - self.participant.vars['spend3']
        wealth3 = self.participant.vars['wealth3']
        points3 = int(round(self.participant.vars['points3'], 0))

        income4 = self.player.income4
        spend4 = self.participant.vars['spend4']
        saving4 = self.player.income4 - self.participant.vars['spend4']
        wealth4 = self.participant.vars['wealth4']
        points4 = int(round(self.participant.vars['points4'], 0))

        income5 = self.player.income5
        wealth5 = self.participant.vars['wealth5']

        return {'lang': lang,
                'income1': income1,
                'spend1': spend1,
                'saving1': saving1,
                'wealth1': wealth1,
                'points1': points1,
                'income2': income2,
                'spend2': spend2,
                'saving2': saving2,
                'wealth2': wealth2,
                'points2': points2,
                'income3': income3,
                'spend3': spend3,
                'saving3': saving3,
                'wealth3': wealth3,
                'points3': points3,
                'income4': income4,
                'spend4': spend4,
                'saving4': saving4,
                'wealth4': wealth4,
                'points4': points4,
                'income5': income5,
                'wealth5': wealth5}

    def before_next_page(self):
        self.participant.vars['spend5'] = self.player.spend5
        self.participant.vars['saving5'] = self.player.income5 - self.player.spend5
        self.participant.vars['wealth6'] = self.participant.vars['wealth5'] + self.player.income5 - self.player.spend5
        self.participant.vars['points5'] = 250 * (1 - math.exp(-0.02 * self.player.spend5)) * 1.5589


class Period6(Page):
    form_model = 'player'
    form_fields = ['spend6', 'check_spend6']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend6']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income1 = self.player.income1
        spend1 = self.participant.vars['spend1']
        saving1 = self.player.income1 - self.participant.vars['spend1']
        wealth1 = self.participant.vars['wealth1']
        points1 = int(round(self.participant.vars['points1'], 0))

        income2 = self.player.income2
        spend2 = self.participant.vars['spend2']
        saving2 = self.player.income2 - self.participant.vars['spend2']
        wealth2 = self.participant.vars['wealth2']
        points2 = int(round(self.participant.vars['points2'], 0))

        income3 = self.player.income3
        spend3 = self.participant.vars['spend3']
        saving3 = self.player.income3 - self.participant.vars['spend3']
        wealth3 = self.participant.vars['wealth3']
        points3 = int(round(self.participant.vars['points3'], 0))

        income4 = self.player.income4
        spend4 = self.participant.vars['spend4']
        saving4 = self.player.income4 - self.participant.vars['spend4']
        wealth4 = self.participant.vars['wealth4']
        points4 = int(round(self.participant.vars['points4'], 0))

        income5 = self.player.income5
        spend5 = self.participant.vars['spend5']
        saving5 = self.player.income5 - self.participant.vars['spend5']
        wealth5 = self.participant.vars['wealth5']
        points5 = int(round(self.participant.vars['points5'], 0))

        income6 = self.player.income6
        wealth6 = self.participant.vars['wealth6']

        return {'lang': lang,
                'income1': income1,
                'spend1': spend1,
                'saving1': saving1,
                'wealth1': wealth1,
                'points1': points1,
                'income2': income2,
                'spend2': spend2,
                'saving2': saving2,
                'wealth2': wealth2,
                'points2': points2,
                'income3': income3,
                'spend3': spend3,
                'saving3': saving3,
                'wealth3': wealth3,
                'points3': points3,
                'income4': income4,
                'spend4': spend4,
                'saving4': saving4,
                'wealth4': wealth4,
                'points4': points4,
                'income5': income5,
                'spend5': spend5,
                'saving5': saving5,
                'wealth5': wealth5,
                'points5': points5,
                'income6': income6,
                'wealth6': wealth6}

    def before_next_page(self):
        self.participant.vars['spend6'] = self.player.spend6
        self.participant.vars['saving6'] = self.player.income6 - self.player.spend6
        self.participant.vars['wealth7'] = self.participant.vars['wealth6'] + self.player.income6 - self.player.spend6
        self.participant.vars['points6'] = 250 * (1 - math.exp(-0.02 * self.player.spend6)) * 1.5589


class Period7(Page):
    form_model = 'player'
    form_fields = ['spend7', 'check_spend7']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend7']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income1 = self.player.income1
        spend1 = self.participant.vars['spend1']
        saving1 = self.player.income1 - self.participant.vars['spend1']
        wealth1 = self.participant.vars['wealth1']
        points1 = int(round(self.participant.vars['points1'], 0))

        income2 = self.player.income2
        spend2 = self.participant.vars['spend2']
        saving2 = self.player.income2 - self.participant.vars['spend2']
        wealth2 = self.participant.vars['wealth2']
        points2 = int(round(self.participant.vars['points2'], 0))

        income3 = self.player.income3
        spend3 = self.participant.vars['spend3']
        saving3 = self.player.income3 - self.participant.vars['spend3']
        wealth3 = self.participant.vars['wealth3']
        points3 = int(round(self.participant.vars['points3'], 0))

        income4 = self.player.income4
        spend4 = self.participant.vars['spend4']
        saving4 = self.player.income4 - self.participant.vars['spend4']
        wealth4 = self.participant.vars['wealth4']
        points4 = int(round(self.participant.vars['points4'], 0))

        income5 = self.player.income5
        spend5 = self.participant.vars['spend5']
        saving5 = self.player.income5 - self.participant.vars['spend5']
        wealth5 = self.participant.vars['wealth5']
        points5 = int(round(self.participant.vars['points5'], 0))

        income6 = self.player.income6
        spend6 = self.participant.vars['spend6']
        saving6 = self.player.income6 - self.participant.vars['spend6']
        wealth6 = self.participant.vars['wealth6']
        points6 = int(round(self.participant.vars['points6'], 0))

        income7 = self.player.income7
        wealth7 = self.participant.vars['wealth7']

        return {'lang': lang,
                'income1': income1,
                'spend1': spend1,
                'saving1': saving1,
                'wealth1': wealth1,
                'points1': points1,
                'income2': income2,
                'spend2': spend2,
                'saving2': saving2,
                'wealth2': wealth2,
                'points2': points2,
                'income3': income3,
                'spend3': spend3,
                'saving3': saving3,
                'wealth3': wealth3,
                'points3': points3,
                'income4': income4,
                'spend4': spend4,
                'saving4': saving4,
                'wealth4': wealth4,
                'points4': points4,
                'income5': income5,
                'spend5': spend5,
                'saving5': saving5,
                'wealth5': wealth5,
                'points5': points5,
                'income6': income6,
                'spend6': spend6,
                'saving6': saving6,
                'wealth6': wealth6,
                'points6': points6,
                'income7': income7,
                'wealth7': wealth7}

    def before_next_page(self):
        self.participant.vars['spend7'] = self.player.spend7
        self.participant.vars['saving7'] = self.player.income7 - self.player.spend7
        self.participant.vars['wealth8'] = self.participant.vars['wealth7'] + self.player.income7 - self.player.spend7
        self.participant.vars['points7'] = 250 * (1 - math.exp(-0.02 * self.player.spend7)) * 1.5589


class Period8(Page):
    form_model = 'player'
    form_fields = ['spend8', 'check_spend8']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend8']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income1 = self.player.income1
        spend1 = self.participant.vars['spend1']
        saving1 = self.player.income1 - self.participant.vars['spend1']
        wealth1 = self.participant.vars['wealth1']
        points1 = int(round(self.participant.vars['points1'], 0))

        income2 = self.player.income2
        spend2 = self.participant.vars['spend2']
        saving2 = self.player.income2 - self.participant.vars['spend2']
        wealth2 = self.participant.vars['wealth2']
        points2 = int(round(self.participant.vars['points2'], 0))

        income3 = self.player.income3
        spend3 = self.participant.vars['spend3']
        saving3 = self.player.income3 - self.participant.vars['spend3']
        wealth3 = self.participant.vars['wealth3']
        points3 = int(round(self.participant.vars['points3'], 0))

        income4 = self.player.income4
        spend4 = self.participant.vars['spend4']
        saving4 = self.player.income4 - self.participant.vars['spend4']
        wealth4 = self.participant.vars['wealth4']
        points4 = int(round(self.participant.vars['points4'], 0))

        income5 = self.player.income5
        spend5 = self.participant.vars['spend5']
        saving5 = self.player.income5 - self.participant.vars['spend5']
        wealth5 = self.participant.vars['wealth5']
        points5 = int(round(self.participant.vars['points5'], 0))

        income6 = self.player.income6
        spend6 = self.participant.vars['spend6']
        saving6 = self.player.income6 - self.participant.vars['spend6']
        wealth6 = self.participant.vars['wealth6']
        points6 = int(round(self.participant.vars['points6'], 0))

        income7 = self.player.income7
        spend7 = self.participant.vars['spend7']
        saving7 = self.player.income7 - self.participant.vars['spend7']
        wealth7 = self.participant.vars['wealth7']
        points7 = int(round(self.participant.vars['points7'], 0))

        income8 = self.player.income8
        wealth8 = self.participant.vars['wealth8']

        return {'lang': lang,
                'income1': income1,
                'spend1': spend1,
                'saving1': saving1,
                'wealth1': wealth1,
                'points1': points1,
                'income2': income2,
                'spend2': spend2,
                'saving2': saving2,
                'wealth2': wealth2,
                'points2': points2,
                'income3': income3,
                'spend3': spend3,
                'saving3': saving3,
                'wealth3': wealth3,
                'points3': points3,
                'income4': income4,
                'spend4': spend4,
                'saving4': saving4,
                'wealth4': wealth4,
                'points4': points4,
                'income5': income5,
                'spend5': spend5,
                'saving5': saving5,
                'wealth5': wealth5,
                'points5': points5,
                'income6': income6,
                'spend6': spend6,
                'saving6': saving6,
                'wealth6': wealth6,
                'points6': points6,
                'income7': income7,
                'spend7': spend7,
                'saving7': saving7,
                'wealth7': wealth7,
                'points7': points7,
                'income8': income8,
                'wealth8': wealth8}

    def before_next_page(self):
        self.participant.vars['spend8'] = self.player.spend8
        self.participant.vars['saving8'] = self.player.income8 - self.player.spend8
        self.participant.vars['wealth9'] = self.participant.vars['wealth8'] + self.player.income8 - self.player.spend8
        self.participant.vars['points8'] = 250 * (1 - math.exp(-0.02 * self.player.spend8)) * 1.5589


class Period9(Page):
    form_model = 'player'
    form_fields = ['spend9', 'check_spend9']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['check_spend9']:
            return _('Please decide the amount you would like to spend.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income1 = self.player.income1
        spend1 = self.participant.vars['spend1']
        saving1 = self.player.income1 - self.participant.vars['spend1']
        wealth1 = self.participant.vars['wealth1']
        points1 = int(round(self.participant.vars['points1'], 0))

        income2 = self.player.income2
        spend2 = self.participant.vars['spend2']
        saving2 = self.player.income2 - self.participant.vars['spend2']
        wealth2 = self.participant.vars['wealth2']
        points2 = int(round(self.participant.vars['points2'], 0))

        income3 = self.player.income3
        spend3 = self.participant.vars['spend3']
        saving3 = self.player.income3 - self.participant.vars['spend3']
        wealth3 = self.participant.vars['wealth3']
        points3 = int(round(self.participant.vars['points3'], 0))

        income4 = self.player.income4
        spend4 = self.participant.vars['spend4']
        saving4 = self.player.income4 - self.participant.vars['spend4']
        wealth4 = self.participant.vars['wealth4']
        points4 = int(round(self.participant.vars['points4'], 0))

        income5 = self.player.income5
        spend5 = self.participant.vars['spend5']
        saving5 = self.player.income5 - self.participant.vars['spend5']
        wealth5 = self.participant.vars['wealth5']
        points5 = int(round(self.participant.vars['points5'], 0))

        income6 = self.player.income6
        spend6 = self.participant.vars['spend6']
        saving6 = self.player.income6 - self.participant.vars['spend6']
        wealth6 = self.participant.vars['wealth6']
        points6 = int(round(self.participant.vars['points6'], 0))

        income7 = self.player.income7
        spend7 = self.participant.vars['spend7']
        saving7 = self.player.income7 - self.participant.vars['spend7']
        wealth7 = self.participant.vars['wealth7']
        points7 = int(round(self.participant.vars['points7'], 0))

        income8 = self.player.income8
        spend8 = self.participant.vars['spend8']
        saving8 = self.player.income8 - self.participant.vars['spend8']
        wealth8 = self.participant.vars['wealth8']
        points8 = int(round(self.participant.vars['points8'], 0))

        income9 = self.player.income9
        wealth9 = self.participant.vars['wealth9']

        return {'lang': lang,
                'income1': income1,
                'spend1': spend1,
                'saving1': saving1,
                'wealth1': wealth1,
                'points1': points1,
                'income2': income2,
                'spend2': spend2,
                'saving2': saving2,
                'wealth2': wealth2,
                'points2': points2,
                'income3': income3,
                'spend3': spend3,
                'saving3': saving3,
                'wealth3': wealth3,
                'points3': points3,
                'income4': income4,
                'spend4': spend4,
                'saving4': saving4,
                'wealth4': wealth4,
                'points4': points4,
                'income5': income5,
                'spend5': spend5,
                'saving5': saving5,
                'wealth5': wealth5,
                'points5': points5,
                'income6': income6,
                'spend6': spend6,
                'saving6': saving6,
                'wealth6': wealth6,
                'points6': points6,
                'income7': income7,
                'spend7': spend7,
                'saving7': saving7,
                'wealth7': wealth7,
                'points7': points7,
                'income8': income8,
                'spend8': spend8,
                'saving8': saving8,
                'wealth8': wealth8,
                'points8': points8,
                'income9': income9,
                'wealth9': wealth9}

    def before_next_page(self):
        self.participant.vars['spend9'] = self.player.spend9
        self.participant.vars['saving9'] = self.player.income9 - self.player.spend9
        self.participant.vars['wealth10'] = self.participant.vars['wealth9'] + self.player.income9 - self.player.spend9
        self.participant.vars['points9'] = 250 * (1 - math.exp(-0.02 * self.player.spend9)) * 1.5589
        self.participant.vars['spend10'] = self.participant.vars['wealth9'] + self.player.income9 - self.player.spend9 + \
                                           self.player.income10
        self.player.spend10 = self.participant.vars['wealth9'] + self.player.income9 - self.player.spend9 + \
                              self.player.income10


class Period10(Page):
    form_model = 'player'
    form_fields = ['points_total']

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']

        income1 = self.player.income1
        spend1 = self.participant.vars['spend1']
        saving1 = self.player.income1 - self.participant.vars['spend1']
        wealth1 = self.participant.vars['wealth1']
        points1 = int(round(self.participant.vars['points1'], 0))

        income2 = self.player.income2
        spend2 = self.participant.vars['spend2']
        saving2 = self.player.income2 - self.participant.vars['spend2']
        wealth2 = self.participant.vars['wealth2']
        points2 = int(round(self.participant.vars['points2'], 0))

        income3 = self.player.income3
        spend3 = self.participant.vars['spend3']
        saving3 = self.player.income3 - self.participant.vars['spend3']
        wealth3 = self.participant.vars['wealth3']
        points3 = int(round(self.participant.vars['points3'], 0))

        income4 = self.player.income4
        spend4 = self.participant.vars['spend4']
        saving4 = self.player.income4 - self.participant.vars['spend4']
        wealth4 = self.participant.vars['wealth4']
        points4 = int(round(self.participant.vars['points4'], 0))

        income5 = self.player.income5
        spend5 = self.participant.vars['spend5']
        saving5 = self.player.income5 - self.participant.vars['spend5']
        wealth5 = self.participant.vars['wealth5']
        points5 = int(round(self.participant.vars['points5'], 0))

        income6 = self.player.income6
        spend6 = self.participant.vars['spend6']
        saving6 = self.player.income6 - self.participant.vars['spend6']
        wealth6 = self.participant.vars['wealth6']
        points6 = int(round(self.participant.vars['points6'], 0))

        income7 = self.player.income7
        spend7 = self.participant.vars['spend7']
        saving7 = self.player.income7 - self.participant.vars['spend7']
        wealth7 = self.participant.vars['wealth7']
        points7 = int(round(self.participant.vars['points7'], 0))

        income8 = self.player.income8
        spend8 = self.participant.vars['spend8']
        saving8 = self.player.income8 - self.participant.vars['spend8']
        wealth8 = self.participant.vars['wealth8']
        points8 = int(round(self.participant.vars['points8'], 0))

        income9 = self.player.income9
        spend9 = self.participant.vars['spend9']
        saving9 = self.player.income9 - self.participant.vars['spend9']
        wealth9 = self.participant.vars['wealth9']
        points9 = int(round(self.participant.vars['points9'], 0))

        income10 = self.player.income10
        spend10 = self.participant.vars['spend10']
        saving10 = self.player.income10 - self.participant.vars['spend10']
        wealth10 = self.participant.vars['wealth10']
        points10_num = 250 * (1 - math.exp(-0.02 * self.participant.vars['spend10'])) * 1.5589
        points10 = int(round(points10_num, 0))

        return {'lang': lang,
                'income1': income1,
                'spend1': spend1,
                'saving1': saving1,
                'wealth1': wealth1,
                'points1': points1,
                'income2': income2,
                'spend2': spend2,
                'saving2': saving2,
                'wealth2': wealth2,
                'points2': points2,
                'income3': income3,
                'spend3': spend3,
                'saving3': saving3,
                'wealth3': wealth3,
                'points3': points3,
                'income4': income4,
                'spend4': spend4,
                'saving4': saving4,
                'wealth4': wealth4,
                'points4': points4,
                'income5': income5,
                'spend5': spend5,
                'saving5': saving5,
                'wealth5': wealth5,
                'points5': points5,
                'income6': income6,
                'spend6': spend6,
                'saving6': saving6,
                'wealth6': wealth6,
                'points6': points6,
                'income7': income7,
                'spend7': spend7,
                'saving7': saving7,
                'wealth7': wealth7,
                'points7': points7,
                'income8': income8,
                'spend8': spend8,
                'saving8': saving8,
                'wealth8': wealth8,
                'points8': points8,
                'income9': income9,
                'spend9': spend9,
                'saving9': saving9,
                'wealth9': wealth9,
                'points9': points9,
                'income10': income10,
                'spend10': spend10,
                'saving10': saving10,
                'wealth10': wealth10,
                'points10': points10}

    def before_next_page(self):
        points10_num = 250 * (1 - math.exp(-0.02 * self.player.spend10)) * 1.5589
        self.participant.vars['points10'] = int(round(points10_num, 0))
        points_total_num = 0
        for k in range(1, 11):
            str_points = 'points%s' % k
            points_total_num += self.participant.vars[str_points]
        if points_total_num < 0:
            self.player.points_total = 0
        else:
            self.player.points_total = int(round(points_total_num, 0))


class Summary(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60

    def vars_for_template(self):
        points_total1_num = self.player.in_round(1).points_total
        points_total1 = int(points_total1_num)
        return {
            'points_total1': points_total1
        }

    def before_next_page(self):
        self.participant.vars['points_total1_borrow'] = self.player.in_round(1).points_total


class End(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60


page_sequence = [Start, Period1, Period2, Period3, Period4, Period5, Period6, Period7, Period8, Period9, Period10,
                 Summary, End]
