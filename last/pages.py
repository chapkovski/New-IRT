from otree.api import Currency as c, currency_range
from matcher.generic_pages import Page
from .models import Constants


class BlockedByOther(Page):
    def is_displayed(self):
        self.player.payable = self.participant.vars.get('payable')
        return self.participant.vars.get('alter_block')


class Last(Page):
    def is_displayed(self):
        self.player.payable = self.participant.vars.get('payable')
        return self.round_number == Constants.num_rounds


page_sequence = [BlockedByOther, Last]
