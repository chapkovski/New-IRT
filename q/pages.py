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


class IncomeScale(Page):
    template_name = 'q/IncomeScale.html'

    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('income_scale')
        self.player.income_scale = data
        return super().post()


class IncomeScaleFamily(Page):
    template_name = 'q/IncomeScaleFamily.html'

    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('income_scale_family')
        self.player.income_scale_family = data
        return super().post()


class Lits2020(Page):
    template_name = 'q/Lits2020.html'

    def vars_for_template(self):
        items = [
            dict(name='lits_equal',
                 left="Incomes should be made more equal",
                 right="We need larger income differences as incentives for individual effort"),
            dict(name='lits_ownership', left="Private ownership of business and industry should be increased",
                 right="Government ownership of business and industry should be increased"),
            dict(name='lits_competition',
                 left="Competition is good. It stimulates people to word hard and develop new ideas",
                 right="Competition is harmful. It brings out the worse in people"),
            dict(name='lits_obey', left="People should obey the law without exception",
                 right="Therea are times when people hoave good reasons to break the law", ),
            dict(name='lits_authorities',
                 left='As citizens, we should be more active in questioning the actions of our authorities',
                 right='In our country today, we should show more sepcect for our authoriteies'),
            dict(name='lits_wealthy',
                 left="There is no problem with the influence of wealthy individuals on the way government is run in this country",
                 right="Wealthy individuals often use their influence on government for their own interests and there need to be stricter rules to prevent this."),
            dict(name='lits_party',
                 left="Financial support by companies to political parties and candidates should be banned completely",
                 right="Tere should be no limits on financial support by companies to political parties or candidates")

        ]
        return dict(choices=range(1, 11), items=items)


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
    form_model = 'player'
    form_fields = ['income_pyramid']


class IncomePyramidRegional(Page):
    template_name = 'q/IncomePyramidRegional.html'
    form_model = 'player'
    form_fields = ['income_pyramid_regional']


page_sequence = [
    Income,
    IncomeScale,
    IncomeScaleFamily,
    IncomePyramid,
    IncomePyramidRegional,
    Lits2020,
    AltruismAndTrust,
    Big5,
    Risk,
    Patience,
    SES,
    ChildrenQualities,
    TrustPaidBack,
    CityInteractionsTrustDisappointed,

]
