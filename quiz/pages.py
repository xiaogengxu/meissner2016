from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random, time
from .generic_pages import Page
from django.utils.translation import ugettext_lazy as _


class Quiz_borrow(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6']

    def is_displayed(self):
        return self.participant.vars['treatment'] == 'borrow_first' and self.participant.vars['time_instruction'] >= 60

    def quiz1_choices(player):
        choices = ['5', '10', '20']
        random.shuffle(choices)
        return choices

    def quiz2_choices(player):
        choices = [['points', _('In Points')], ['coins', _('In Coins')], ['USD', _('In US Dollars')]]
        random.shuffle(choices)
        return choices

    def quiz3_choices(player):
        choices = ['11', '50', '246']
        random.shuffle(choices)
        return choices

    def quiz4_choices(player):
        choices = [['sum_cent', _('Sum of Eurocent Rewards in one of the 4 lives')],
                   ['one_cent', _('One Eurocent for each Income point')],
                   ['avg_start', _('Average of account Start Balance in one of the 4 lives')]]
        random.shuffle(choices)
        return choices

    def quiz5_choices(player):
        choices = [['all_same', _('Income is always the same for all periods')],
                   ['end_negative', _('If your End Balance at the end of a life is negative, '
                                      'you will gather a negative Eurocent Rewards for that period')],
                   ['start_20', _('The Start Balance at the first period is 20')]]
        random.shuffle(choices)
        return choices

    def quiz6_choices(player):
        choices = ['30', '-10', '100']
        random.shuffle(choices)
        return choices

    def error_message(self, values):
        if not values['quiz1'] or not values['quiz2'] or not values['quiz3'] or not values['quiz4'] \
                or not values['quiz5'] or not values['quiz6']:
            return _('Please answer all questions.')

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60*60
        if self.player.quiz1 and self.player.quiz2 and self.player.quiz3 and self.player.quiz4 and self.player.quiz5 \
                and self.player.quiz6:
            if self.player.quiz1 != '10':
                self.participant.vars['mis_q1'] = 1
                self.player.quiz1 = ''
            if self.player.quiz2 != 'points':
                self.participant.vars['mis_q2'] = 1
                self.player.quiz2 = ''
            if self.player.quiz3 != '246':
                self.participant.vars['mis_q3'] = 1
                self.player.quiz3 = ''
            if self.player.quiz4 != 'sum_cent':
                self.participant.vars['mis_q4'] = 1
                self.player.quiz4 = ''
            if self.player.quiz5 != 'end_negative':
                self.participant.vars['mis_q5'] = 1
                self.player.quiz5 = ''
            if self.player.quiz6 != '30':
                self.participant.vars['mis_q6'] = 1
                self.player.quiz6 = ''

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        return {'lang': lang}


class Quiz_save(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'quiz6']

    def is_displayed(self):
        return self.participant.vars['treatment'] == 'save_first' and self.participant.vars['time_instruction'] >= 60

    def quiz1_choices(player):
        choices = ['5', '10', '20']
        random.shuffle(choices)
        return choices

    def quiz2_choices(player):
        choices = [['points', _('In Points')], ['coins', _('In Coins')], ['USD', _('In US Dollars')]]
        random.shuffle(choices)
        return choices

    def quiz3_choices(player):
        choices = ['11', '50', '246']
        random.shuffle(choices)
        return choices

    def quiz4_choices(player):
        choices = [['sum_cent', _('Sum of Eurocent Rewards in one of the 4 lives')],
                   ['one_cent', _('One Eurocent for each Income point')],
                   ['avg_start', _('Average of account Start Balance in one of the 4 lives')]]
        random.shuffle(choices)
        return choices

    def quiz5_choices(player):
        choices = [['all_same', _('Income is always the same for all periods')],
                   ['end_negative', _('If your End Balance at the end of a life is negative, '
                                      'you will gather a negative Eurocent Rewards for that period')],
                   ['start_20', _('The Start Balance at the first period is 20')]]
        random.shuffle(choices)
        return choices

    def quiz6_choices(player):
        choices = ['30', '-10', '100']
        random.shuffle(choices)
        return choices

    def error_message(self, values):
        if not values['quiz1'] or not values['quiz2'] or not values['quiz3'] or not values['quiz4'] \
                or not values['quiz5'] or not values['quiz6']:
            return _('Please answer all questions.')

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60*60
        if self.player.quiz1 and self.player.quiz2 and self.player.quiz3 and self.player.quiz4 and self.player.quiz5 \
                and self.player.quiz6:
            if self.player.quiz1 != '10':
                self.participant.vars['mis_q1'] = 1
                self.player.quiz1 = ''
            if self.player.quiz2 != 'points':
                self.participant.vars['mis_q2'] = 1
                self.player.quiz2 = ''
            if self.player.quiz3 != '246':
                self.participant.vars['mis_q3'] = 1
                self.player.quiz3 = ''
            if self.player.quiz4 != 'sum_cent':
                self.participant.vars['mis_q4'] = 1
                self.player.quiz4 = ''
            if self.player.quiz5 != 'end_negative':
                self.participant.vars['mis_q5'] = 1
                self.player.quiz5 = ''
            if self.player.quiz6 != '30':
                self.participant.vars['mis_q6'] = 1
                self.player.quiz6 = ''

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        return {'lang': lang}


class End_attempt1(Page):
    form_model = 'player'

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake > 2 and self.participant.vars['time_instruction'] >= 60

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/quality?p=73952&m='+username_value)

    def before_next_page(self):
        self.participant.vars['end'] = 1


class Quiz_retry(Page):
    form_model = 'player'

    def get_form_fields(self):
        formfield_list = []
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
            + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        if sum_mistake < 3:
            if self.participant.vars['mis_q1'] == 1:
                formfield_list.append('quiz1')
            if self.participant.vars['mis_q2'] == 1:
                formfield_list.append('quiz2')
            if self.participant.vars['mis_q3'] == 1:
                formfield_list.append('quiz3')
            if self.participant.vars['mis_q4'] == 1:
                formfield_list.append('quiz4')
            if self.participant.vars['mis_q5'] == 1:
                formfield_list.append('quiz5')
            if self.participant.vars['mis_q6'] == 1:
                formfield_list.append('quiz6')
        return formfield_list

    def quiz1_choices(player):
        choices = ['5', '10', '20']
        random.shuffle(choices)
        return choices

    def quiz2_choices(player):
        choices = [['points', _('In Points')], ['coins', _('In Coins')], ['USD', _('In US Dollars')]]
        random.shuffle(choices)
        return choices

    def quiz3_choices(player):
        choices = ['11', '50', '246']
        random.shuffle(choices)
        return choices

    def quiz4_choices(player):
        choices = [['sum_cent', 'Sum of Eurocent Rewards in one of the 4 lives'],
                   ['one_cent', 'One Eurocent for each Income point'],
                   ['avg_start', 'Average of account Start Balance in one of the 4 lives']]
        random.shuffle(choices)
        return choices

    def quiz5_choices(player):
        choices = [['all_same', 'Income is always the same for all periods'],
                   ['end_negative', 'If your End Balance at the end of a life is negative, '
                                    'you will gather a negative Eurocent Rewards for that period'],
                   ['start_20', 'The Start Balance at the first period is 20']]
        random.shuffle(choices)
        return choices

    def quiz6_choices(player):
        choices = ['30', '-10', '100']
        random.shuffle(choices)
        return choices

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
            + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake < 3 and self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if (self.participant.vars['mis_q1'] == 1 and not values['quiz1']) or \
                (self.participant.vars['mis_q2'] == 1 and not values['quiz2']) or \
                (self.participant.vars['mis_q3'] == 1 and not values['quiz3']) or \
                (self.participant.vars['mis_q4'] == 1 and not values['quiz4']) or \
                (self.participant.vars['mis_q5'] == 1 and not values['quiz5']) or \
                (self.participant.vars['mis_q6'] == 1 and not values['quiz6']):
            return _('Please answer the question.')

    def vars_for_template(self):
        treatment = self.participant.vars['treatment']
        lang = self.participant.vars['lang_chosen']
        if self.participant.vars['mis_q1'] == 1:
            show1 = 1
        else:
            show1 = 0

        if self.participant.vars['mis_q2'] == 1:
            show2 = 1
        else:
            show2 = 0

        if self.participant.vars['mis_q3'] == 1:
            show3 = 1
        else:
            show3 = 0

        if self.participant.vars['mis_q4'] == 1:
            show4 = 1
        else:
            show4 = 0

        if self.participant.vars['mis_q5'] == 1:
            show5 = 1
        else:
            show5 = 0

        if self.participant.vars['mis_q6'] == 1:
            show6 = 1
        else:
            show6 = 0

        return {
            'treatment': treatment,
            'lang': lang,
            'show1': show1,
            'show2': show2,
            'show3': show3,
            'show4': show4,
            'show5': show5,
            'show6': show6
        }

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60*60

        if self.participant.vars['mis_q1'] == 1:
            if self.player.quiz1 == '10':
                self.participant.vars['mis_q1'] = 0

        if self.participant.vars['mis_q2'] == 1:
            if self.player.quiz2 == 'points':
                self.participant.vars['mis_q2'] = 0

        if self.participant.vars['mis_q3'] == 1:
            if self.player.quiz3 == '246':
                self.participant.vars['mis_q3'] = 0

        if self.participant.vars['mis_q4'] == 1:
            if self.player.quiz4 == 'sum_cent':
                self.participant.vars['mis_q4'] = 0

        if self.participant.vars['mis_q5'] == 1:
            if self.player.quiz5 == 'end_negative':
                self.participant.vars['mis_q5'] = 0

        if self.participant.vars['mis_q6'] == 1:
            if self.player.quiz6 == '30':
                self.participant.vars['mis_q6'] = 0


class End_attempt2(Page):
    form_model = 'player'

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake != 0 and self.participant.vars['time_instruction'] >= 60

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/quality?p=73952&m='+username_value)

    def before_next_page(self):
        self.participant.vars['end'] = 1


class Quiz_q1(Page):
    form_model = 'player'
    form_fields = ['quiz1']

    def quiz1_choices(player):
        choices = ['5', '10', '20']
        random.shuffle(choices)
        return choices

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake == 1 and self.participant.vars['mis_q1'] == 1 and self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['quiz1']:
            return _('Please answer the question.')

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60*60


class End_q1(Page):
    form_model = 'player'

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake == 1 and self.participant.vars['mis_q1'] == 1 and self.player.quiz1 != '10' \
               and self.participant.vars['time_instruction'] >= 60

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/quality?p=73952&m='+username_value)

    def before_next_page(self):
        self.participant.vars['end'] = 1


class Quiz_q2_borrow(Page):
    form_model = 'player'
    form_fields = ['quiz2']

    def quiz2_choices(player):
        choices = [['points', _('In Points')], ['coins', _('In Coins')], ['USD', _('In US Dollars')]]
        random.shuffle(choices)
        return choices

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return self.participant.vars['treatment'] == 'borrow_first' and sum_mistake == 1 \
               and self.participant.vars['mis_q2'] == 1 and self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['quiz2']:
            return _('Please answer the question.')

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60*60


class Quiz_q2_save(Page):
    form_model = 'player'
    form_fields = ['quiz2']

    def quiz2_choices(player):
        choices = [['points', _('Points')], ['coins', 'Coins'], ['USD', 'US Dollars']]
        random.shuffle(choices)
        return choices

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return self.participant.vars['treatment'] == 'save_first' and sum_mistake == 1 \
               and self.participant.vars['mis_q2'] == 1 and self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['quiz2']:
            return _('Please answer the question.')

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60*60


class End_q2(Page):
    form_model = 'player'

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake == 1 and self.participant.vars['mis_q2'] == 1 and self.player.quiz2 != 'points' \
               and self.participant.vars['time_instruction'] >= 60

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/quality?p=73952&m='+username_value)

    def before_next_page(self):
        self.participant.vars['end'] = 1


class Quiz_q3(Page):
    form_model = 'player'
    form_fields = ['quiz3']

    def quiz3_choices(player):
        choices = ['11', '50', '246']
        random.shuffle(choices)
        return choices

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake == 1 and self.participant.vars['mis_q3'] == 1 \
               and self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['quiz3']:
            return _('Please answer the question.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        return {'lang': lang}

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60 * 60


class End_q3(Page):
    form_model = 'player'

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake == 1 and self.participant.vars['mis_q3'] == 1 and self.player.quiz3 != '246' \
               and self.participant.vars['time_instruction'] >= 60

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/quality?p=73952&m='+username_value)

    def before_next_page(self):
        self.participant.vars['end'] = 1


class Quiz_q4(Page):
    form_model = 'player'
    form_fields = ['quiz4']

    def quiz4_choices(player):
        choices = [['sum_cent', 'Sum of Eurocent Rewards in one of the 4 lives'],
                   ['one_cent', 'One Eurocent for each Income point'],
                   ['avg_start', 'Average of account Start Balance in one of the 4 lives']]
        random.shuffle(choices)
        return choices

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake == 1 and self.participant.vars['mis_q4'] == 1 \
               and self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['quiz4']:
            return _('Please answer the question.')

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60 * 60


class End_q4(Page):
    form_model = 'player'

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake == 1 and self.participant.vars['mis_q4'] == 1 and self.player.quiz4 != 'sum_cent' \
               and self.participant.vars['time_instruction'] >= 60

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/quality?p=73952&m='+username_value)

    def before_next_page(self):
        self.participant.vars['end'] = 1


class Quiz_q5(Page):
    form_model = 'player'
    form_fields = ['quiz5']

    def quiz5_choices(player):
        choices = [['all_same', 'Income is always the same for all periods'],
                   ['end_negative', 'If your End Balance at the end of a life is negative, '
                                    'you will gather a negative Eurocent Rewards for that period'],
                   ['start_20', 'The Start Balance at the first period is 20']]
        random.shuffle(choices)
        return choices

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake == 1 and self.participant.vars['mis_q5'] == 1 \
               and self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['quiz5']:
            return _('Please answer the question.')

    def vars_for_template(self):
        lang = self.participant.vars['lang_chosen']
        return {'lang': lang}

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60 * 60


class End_q5(Page):
    form_model = 'player'

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake == 1 and self.participant.vars['mis_q5'] == 1 and self.player.quiz5 != 'end_negative' \
               and self.participant.vars['time_instruction'] >= 60

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/quality?p=73952&m='+username_value)

    def before_next_page(self):
        self.participant.vars['end'] = 1


class Quiz_q6(Page):
    form_model = 'player'
    form_fields = ['quiz6']

    def quiz6_choices(player):
        choices = ['30', '-10', '100']
        random.shuffle(choices)
        return choices

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake == 1 and self.participant.vars['mis_q6'] == 1 \
               and self.participant.vars['time_instruction'] >= 60

    def error_message(self, values):
        if not values['quiz6']:
            return _('Please answer the question.')

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 60 * 60


class End_q6(Page):
    form_model = 'player'

    def is_displayed(self):
        sum_mistake = self.participant.vars['mis_q1']+self.participant.vars['mis_q2']+self.participant.vars['mis_q3']\
                      + self.participant.vars['mis_q4']+self.participant.vars['mis_q5']+self.participant.vars['mis_q6']
        return sum_mistake == 1 and self.participant.vars['mis_q6'] == 1 and self.player.quiz6 != '30' \
               and self.participant.vars['time_instruction'] >= 60

    def js_vars(self):
        username_value = self.participant.label
        return dict(url='https://survey.maximiles.com/quality?p=73952&m='+username_value)

    def before_next_page(self):
        self.participant.vars['end'] = 1


page_sequence = [Quiz_borrow, Quiz_save, End_attempt1, Quiz_retry, End_attempt2]
