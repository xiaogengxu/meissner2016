from os import environ
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_lazy

SESSION_CONFIGS = [
    {
        'name': 'Meissner2016',
        'display_name': 'Meissner2016',
        'num_demo_participants': 100,
        'app_sequence': ['instructions', 'trial_borrow', 'trial_save', 'quiz', 'borrow', 'save', 'post_survey',
                         'result'],
        'language': 'de',
    },
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'
LANGUAGE_SESSION_KEY = '_language'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '06%_$3b*ef8odb!69yr(s%o9doi9-sb-j+fi4m+-_sxt&k-9&g'

INSTALLED_APPS = ['otree']
MIDDLEWARE_CLASSES = ['django.middleware.locale.LocaleMiddleware', ]
