from otree.api import Currency as c, currency_range
from ._builtin import WaitPage
from matcher.generic_pages import Page
from .models import Constants


class Decision(Page):
    timeout_seconds = 30
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return not self.participant.vars.get('group_blocked')

    def before_next_page(self):
        if self.timeout_happened:
            for p in self.group.get_players():
                p.participant.vars['group_blocked'] = True
            self.participant.vars['own_block'] = True
            for p in self.player.get_others_in_group():
                if not p.participant.vars.get('own_block'):
                    p.participant.vars['alter_block'] = True
            self.group.blocked = True


class InterMingleWP(WaitPage):
    template_name = 'matcher/FirstWP.html'

    def is_displayed(self):
        return not self.participant.vars.get('group_blocked')

    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    timeout_seconds = 30

    def is_displayed(self):
        return not self.participant.vars.get('group_blocked')
class FinalResults(Page):
    timeout_seconds = 30

    def is_displayed(self):
        return not self.participant.vars.get('group_blocked') and self.round_number == Constants.num_rounds
    def before_next_page(self):
        self.participant.vars['payable'] = True

page_sequence = [Decision, InterMingleWP, Results]
