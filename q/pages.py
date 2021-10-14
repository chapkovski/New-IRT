from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants
import json
from pprint import pprint


class Page(oTreePage):
    def title(self):
        return self.__class__.__name__

    template_name = 'q/Q1.html'
    form_model = 'player'


class SES(Page):
    form_fields = ["gender",
                   "smoke",
                   "best_intentions",
                   "fast_drive", ]


class Income(Page):
    form_fields = [
        "income",
        "fin_situation_change",
        "income_diff",
        "reduce_income_diff",
        "regional_diff",
        "regional_average_income",
        "regional_income_changed",
        "relative_income", ]


class Big5(Page):
    template_name = 'q/Big5.html'

    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('big5')

        for k, v in data.items():
            setattr(self.player, k, v.get('col1'))
        return super().post()


class AltruismAndTrust(Page):
    template_name = 'q/AltruismAndTrust.html'

    def post(self):
        data = json.loads(self.request.POST.get('surveyholder'))
        ready_help = data.get('ready_help')
        self.player.ready_help = ready_help
        altruism = data.get('altruism')
        if altruism:
            for k, v in altruism.items():
                setattr(self.player, k, v.get('col1'))
        return super().post()


class Risk(Page):
    template_name = 'q/Risk.html'

    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('risk')
        pprint(data)
        for k, v in data.items():
            setattr(self.player, k, v.get('col1'))
        return super().post()


class Patience(Page):
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('patience')

        for k, v in data.items():
            setattr(self.player, k, v.get('col1'))
        return super().post()

    template_name = 'q/Patience.html'


class CityInteractionsTrustDisappointed(Page):
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('trust_disappointed')
        if data:
            for k, v in data.items():
                setattr(self.player, k, v.get('col1'))
        return super().post()

    template_name = 'q/CityInteractionsTrustDisappointed.html'


class TrustPaidBack(Page):
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('trust_paid_back')
        if data:
            for k, v in data.items():
                setattr(self.player, k, v.get('col1'))
        return super().post()

    template_name = 'q/TrustPaidBack.html'


class ChildrenQualities(Page):
    template_name = 'q/ChildrenQualities.html'

    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('children_qualities')
        if data:
            for i in data:
                if hasattr(self.player, i):
                    setattr(self.player, i, 1)
        print(data, '=======')
        return super().post()


class IncomePyramid(Page):
    template_name = 'q/IncomePyramid.html'
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('pictures')

        for k, v in data.items():
            setattr(self.player, k, v.get('col1'))
        return super().post()




page_sequence = [
    # Income,
    IncomePyramid,
    # AltruismAndTrust,
    # Big5,
    # Risk,
    # Patience,
    # SES,
    ChildrenQualities,
    # TrustPaidBack,
    # CityInteractionsTrustDisappointed,

]
