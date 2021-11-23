
from  otree.api import Page as oTreePage, WaitPage


class Page(oTreePage):
    def get_context_data(self, **context):
        r = super().get_context_data(**context)
        r['maxpages'] = self.participant._max_page_index
        r['page_index'] = self._index_in_pages
        r['progress'] = f'{int(self._index_in_pages / self.participant._max_page_index * 100):d}'
        return r

    def title(self):
        return self.__class__.__name__

    def app_after_this_page(self, upcoming_apps):
        if self.participant.vars.get('group_blocked'):
            return "blocker"