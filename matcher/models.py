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
from django.utils.timezone import now

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'matcher'
    players_per_group = 2
    num_rounds = 1
    max_waiting_time = 30
    wp_update_freq = 10


class Subsession(BaseSubsession):
    def group_by_arrival_time_method(self, waiting_players):
        if len(waiting_players) > 1:
            return waiting_players[:2]
        for i in waiting_players:
            if (now() - i.participant.vars.get('first_wp_arrival', now())).total_seconds() > Constants.max_waiting_time:
                i.participant.vars['blocked_in_wp'] = True
                i.participant.vars['group_blocked'] = True
                i.participant.vars['alter_block'] = True
                i.participant.vars['payable'] = True
                return [i]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
