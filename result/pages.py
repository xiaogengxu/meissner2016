from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .generic_pages import Page
import random, time
from django.utils.translation import ugettext_lazy as _


def get_timeout_seconds(player):
    return player.participant.vars['expiry'] - time.time()


class Result(Page):
    form_model = 'player'
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        if self.participant.vars['time_instruction'] >= 60 and self.participant.vars['end'] == 0 \
                and get_timeout_seconds(self.player) > 3:
            return self.participant.vars['time_choice'] != 'delay0'
        else:
            return False

    def vars_for_template(self):
        if self.participant.vars['part_chosen'] == 'borrow':
            if self.participant.vars['round_chosen'] == 1:
                if self.participant.vars['treatment'] == 'borrow_first':
                    round_chosen_string = '1'
                else:
                    round_chosen_string = '3'
            else:
                if self.participant.vars['treatment'] == 'borrow_first':
                    round_chosen_string = '2'
                else:
                    round_chosen_string = '4'
        else:
            if self.participant.vars['round_chosen'] == 1:
                if self.participant.vars['treatment'] == 'borrow_first':
                    round_chosen_string = '3'
                else:
                    round_chosen_string = '1'
            else:
                if self.participant.vars['treatment'] == 'borrow_first':
                    round_chosen_string = '4'
                else:
                    round_chosen_string = '2'

        points_total_num = self.participant.vars['reward']
        points_total = round(points_total_num/100, 2)
        risk_choice = self.participant.vars['risk_choice']
        invest_num = self.participant.vars['reward'] * self.participant.vars['risk_choice'] / 100

        if self.participant.vars['risk_outcome'] == 'win':
            earn_invest_num = 3.5 * risk_choice / 100 * self.participant.vars['reward']
            if self.participant.vars['lang_chosen'] == 'en':
                risk_outcome = 'win'
            else:
                risk_outcome = 'Gewinn'
        else:
            earn_invest_num = 0
            if self.participant.vars['lang_chosen'] == 'en':
                risk_outcome = 'loss'
            else:
                risk_outcome = 'Verlust'

        earn_safe_num = (100 - risk_choice) / 100 * self.participant.vars['reward']
        invest = round(invest_num/100, 2)
        earn_invest = round(earn_invest_num/100, 2)
        earn_safe = round(earn_safe_num/100, 2)
        total_num = earn_invest + earn_safe
        total = round(total_num, 2)

        if self.participant.vars['time_choice'] == 'delay1':
            pay_time = _('in 1 month')
            bonus_time_num = total * 0.05
            total1_num = total + bonus_time_num
        elif self.participant.vars['time_choice'] == 'delay2':
            pay_time = _('in 2 months')
            bonus_time_num = total * 0.103
            total1_num = total + bonus_time_num
        else:
            pay_time = _('in 3 months')
            bonus_time_num = total * 0.158
            total1_num = total + bonus_time_num

        total1 = round(total1_num, 2)

        return {
            'points_total': points_total,
            'round_chosen_string': round_chosen_string,
            'risk_outcome': risk_outcome,
            'risk_choice': risk_choice,
            'invest': invest,
            'earn_invest': earn_invest,
            'total': total,
            'pay_time': pay_time,
            'total1': total1
        }

    def before_next_page(self):
        self.participant.vars['finished'] = '1'

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/complete?p=73952_f6efdde9&m='+username_value)


class Result_nodelay(Page):
    form_model = 'player'
    get_timeout_seconds = get_timeout_seconds

    def is_displayed(self):
        if self.participant.vars['time_instruction'] >= 60 and self.participant.vars['end'] == 0 \
                and get_timeout_seconds(self.player) > 3:
            return self.participant.vars['time_choice'] == 'delay0'
        else:
            return False

    def vars_for_template(self):
        if self.participant.vars['part_chosen'] == 'borrow':
            if self.participant.vars['round_chosen'] == 1:
                if self.participant.vars['treatment'] == 'borrow_first':
                    round_chosen_string = '1'
                else:
                    round_chosen_string = '3'
            else:
                if self.participant.vars['treatment'] == 'borrow_first':
                    round_chosen_string = '2'
                else:
                    round_chosen_string = '4'
        else:
            if self.participant.vars['round_chosen'] == 1:
                if self.participant.vars['treatment'] == 'borrow_first':
                    round_chosen_string = '3'
                else:
                    round_chosen_string = '1'
            else:
                if self.participant.vars['treatment'] == 'borrow_first':
                    round_chosen_string = '4'
                else:
                    round_chosen_string = '2'

        points_total_num = self.participant.vars['reward']
        points_total = round(points_total_num/100, 2)
        risk_choice = self.participant.vars['risk_choice']
        invest_num = self.participant.vars['reward'] * self.participant.vars['risk_choice'] / 100

        if self.participant.vars['risk_outcome'] in ['win', 'Gewinn']:
            earn_invest_num = 3.5 * risk_choice / 100 * self.participant.vars['reward']
            if self.participant.vars['lang_chosen'] == 'en':
                risk_outcome = 'win'
            else:
                risk_outcome = 'Gewinn'
        else:
            earn_invest_num = 0
            if self.participant.vars['lang_chosen'] == 'en':
                risk_outcome = 'loss'
            else:
                risk_outcome = 'Verlust'

        earn_safe_num = (100 - risk_choice) / 100 * self.participant.vars['reward']
        invest = round(invest_num/100, 2)
        earn_invest = round(earn_invest_num/100, 2)
        earn_safe = round(earn_safe_num/100, 2)
        total_num = earn_invest + earn_safe
        total = round(total_num, 2)

        return {
            'points_total': points_total,
            'round_chosen_string': round_chosen_string,
            'risk_outcome': risk_outcome,
            'risk_choice': risk_choice,
            'invest': invest,
            'earn_invest': earn_invest,
            'total': total
        }

    def before_next_page(self):
        self.participant.vars['finished'] = '1'

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/complete?p=73952_f6efdde9&m='+username_value)


class Timeout(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.participant.vars['time_instruction'] >= 60 and self.participant.vars['end'] == 0 and \
               self.participant.vars['finished'] == ''

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/speeder?p=73952&m='+username_value)


page_sequence = [Result, Result_nodelay, Timeout]
