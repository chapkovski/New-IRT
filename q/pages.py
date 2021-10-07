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

        for k,v in data.items():
            setattr(self.player, k, v.get('col1'))
        return super().post()



class AltruismAndTrust(Page):
    form_fields = ["ready_help",
                   "donated_money",
                   "count_on_relatives",
                   "help_stranger",
                   "self_employed",
                   "own_business",
                   "save_money",
                   "fin_help",
                   "vote_official",
                   "volunteer",
                   "police_confidence",
                   "safety",
                   "stolen_money",
                   "used_trust",
                   "reciprocated_trust",
                   "disappointed_trust",
                   "donated_blood", ]


class Risk(Page):
    template_name = 'q/Risk.html'
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('risk')
        pprint(data)
        for k,v in data.items():
            setattr(self.player, k, v.get('col1'))
        return super().post()



class Patience(Page):
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('patience')

        for k,v in data.items():
            setattr(self.player, k, v.get('col1'))
        return super().post()
    template_name = 'q/Patience.html'


class CityInteractionsTrustPaid(Page):
    form_fields = ["trust_paid_back_ARK",
                   "trust_paid_back_EKB",
                   "trust_paid_back_KAZ",
                   "trust_paid_back_KHB",
                   "trust_paid_back_MAK",
                   "trust_paid_back_MOS",
                   "trust_paid_back_NSK",
                   "trust_paid_back_PER",
                   "trust_paid_back_POS",
                   "trust_paid_back_SPB",
                   "trust_paid_back_VLK",
                   "trust_paid_back_VOR",
                   ]

class CityInteractionsTrustDisappointed(Page):
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('trust_disappointed')

        for k,v in data.items():
            setattr(self.player, k, v.get('col1'))
        return super().post()
    template_name = 'q/CityInteractionsTrustDisappointed.html'


class ChildrenQualities(Page):
    pass
    # form_fields = ["good_manners",
    #                "independence",
    #                "hard_work",
    #                "responsibility",
    #                "imagination",
    #                "thrift",
    #                "determination",
    #                "religious",
    #                "unselfishness",
    #                "obedience",
    #                ]

page_sequence = [
    # Income,
    # AltruismAndTrust,
    # Big5,
    # Risk,
    # Patience,
    # SES,
    # ChildrenQualities,
    CityInteractionsTrustPaid, #TODO
    # CityInteractionsTrustDisappointed
]
