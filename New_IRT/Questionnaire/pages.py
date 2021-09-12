from django.utils.translation import gettext_lazy as _
from .generic_pages import Page
from django.conf import settings



class IntroQ(Page):
    pass


class Page_1(Page):
    form_model = 'player'
    form_fields = ['gender',
                   'best_intensions',
                   'smoke',
                   'fast_drive',
                   'income_diff',
                   'reduce_income_diff',
                   'income',
                   'fin_situation_change',
                   'avg_monthly_income',
                   'regional_diff',
                   'regional_income_changed',
                   'relative_income',
                   'Patience_10_1',
                   'Patience_10_2',
                   'Patience_10_3',
                   'Patience_10_4',
                   'risk_general',
                   'risk_fin',
                   'risk_sport',
                   'risk_prof',
                   'risk_health',
                   'risk_strangers',
                   'risk_drive',
                   'ready_help,
                   'donated_money',
                   'count_on_relatives',
                   'help_stranger',
                   'self_employed',
                   'own_business',
                   'save_money',
                   'fin_help',
                   'vote_official',
                   'volunteer',
                   'police_confidence',
                   'safety',
                   'stolen_money',
                   'used_trust',
                   'reciprocated_trust',
                   'disappointed_trust',
                   'donated_blood',
                   'big5_1',
                   'big5_2',
                   'big5_3',
                   'big5_4',
                   'big5_5',
                   'big5_6',
                   'big5_7',
                   'big5_8',
                   'big5_9',
                   'big5_10',
                   'big5_11',
                   ]

    joined_fields = [
        {"title": _("""People can behave differently in different situations. How would you assess your desire to take risks in the following situations?
For the answer, choose a value on a scale from 0 to 10, where 0 means that you are "absolutely not ready to take risks", and 10 means that you are "willing to take risks».
                """),
         "fields": [

             'risk_fin',
             'risk_sport',
             'risk_prof',
             'risk_health',
             'risk_strangers',
             'risk_drive'
         ]}
