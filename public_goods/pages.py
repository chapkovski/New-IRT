from ._builtin import WaitPage
from matcher.generic_pages import Page
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    body_text = "Ждите решения других участников"


class Results(Page):

    def vars_for_template(self):
        return dict(total_earnings=self.group.total_contribution * Constants.multiplier)


page_sequence = [
    Introduction,
    Contribute,
    ResultsWaitPage,
    Results
]
