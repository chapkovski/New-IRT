from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants


class Page(oTreePage):
    def get_context_data(self, **context):
        r = super().get_context_data(**context)
        r['maxpages'] = self.participant._max_page_index
        r['page_index'] = self._index_in_pages
        r['progress'] = f'{int(self._index_in_pages / self.participant._max_page_index * 100):d}'
        return r

    def title(self):
        return self.__class__.__name__


class Intro(Page):
    form_model = 'player'
    form_fields = ['understand_rules', 'understand_drop']




page_sequence = [Intro]
