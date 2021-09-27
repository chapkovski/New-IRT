from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants


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
    def get_form_fields(self):
        return [f'big5_{i}' for i in range(1, 11)]


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
    form_fields = ["risk_general",
                   "risk_fin",
                   "risk_sport",
                   "risk_prof",
                   "risk_health",
                   "risk_strangers",
                   "risk_drive", ]


class Patience(Page):
    def get_form_fields(self):
        return [f'patience_{i}' for i in range(1, 5)]

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
    form_fields = ["trust_disappointed_ARK",
                   "trust_disappointed_EKB",
                   "trust_disappointed_KAZ",
                   "trust_disappointed_KHB",
                   "trust_disappointed_MAK",
                   "trust_disappointed_MOS",
                   "trust_disappointed_NSK",
                   "trust_disappointed_PER",
                   "trust_disappointed_POS",
                   "trust_disappointed_SPB",
                   "trust_disappointed_VLK",
                   "trust_disappointed_VOR",
                   ]

class ChildrenQualities(Page):
    form_fields = ["good_manners",
                   "independence",
                   "hard_work",
                   "responsibility",
                   "imagination",
                   "thrift",
                   "determination",
                   "religious",
                   "unselfishness",
                   "obedience",
                   ]

page_sequence = [
    Income,
    AltruismAndTrust,
    Big5,
    Risk,
    Patience,
    SES,
    ChildrenQualities,
    CityInteractionsTrustPaid,
    CityInteractionsTrustDisappointed
]
