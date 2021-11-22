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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'intro_matcher'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    understand_rules=models.BooleanField(label='Я подтверждаю что понимаю правила игры.',
                                         widget=widgets.CheckboxInput)
    understand_drop =models.BooleanField(label='Я понимаю, что если второй участник покинет исследование, то мое участие также завершится.',
                                         widget=widgets.CheckboxInput)
