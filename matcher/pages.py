from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants
from django.utils.timezone import now


class Page(oTreePage):
    def get_context_data(self, **context):
        r = super().get_context_data(**context)
        r['maxpages'] = self.participant._max_page_index
        r['page_index'] = self._index_in_pages
        r['progress'] = f'{int(self._index_in_pages / self.participant._max_page_index * 100):d}'
        return r

    def title(self):
        return self.__class__.__name__


class FirstWP(WaitPage):
    template_name = 'matcher/FirstWP.html'
    group_by_arrival_time = True

    def _get_wait_page(self):
        self.participant.vars.setdefault('first_wp_arrival', now())
        return super()._get_wait_page()

    def is_displayed(self):
        return self.round_number == 1


class SecondWP(WaitPage):
    def is_displayed(self):
        return not self.participant.vars.get('group_blocked')


class ResultsWaitPage(WaitPage):
    pass


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
    template_name = 'matcher/InterMingleWP.html'

    def is_displayed(self):
        return not self.participant.vars.get('group_blocked')

    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    timeout_seconds = 30

    def is_displayed(self):
        return not self.participant.vars.get('group_blocked')


class Blocked(Page):
    def is_displayed(self):
        return self.participant.vars.get('own_block')


class BlockedByOther(Page):
    def is_displayed(self):
        return self.participant.vars.get('alter_block')


class Last(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    FirstWP,
    Decision,
    InterMingleWP,
    Results,
    Blocked,
    BlockedByOther,
    Last,
]
