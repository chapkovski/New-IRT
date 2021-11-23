from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants
import json
from pprint import pprint


class Page(oTreePage):
    def get_context_data(self, **context):
        r = super().get_context_data(**context)
        r['maxpages'] = self.participant._max_page_index
        r['page_index'] = self._index_in_pages
        r['progress'] = f'{int(self._index_in_pages / self.participant._max_page_index * 100):d}'
        return r

    def title(self):
        return self.__class__.__name__

    template_name = 'q/Q1.html'
    form_model = 'player'


class Consent(Page):
    template_name = 'q/Consent.html'


class Welcome(Page):
    template_name = 'q/Welcome.html'


class Last(Page):
    template_name = 'q/Last.html'


class SES(Page):
    form_fields = ["gender",
                   "smoke",
                   "income",
                   "fin_situation_change",
                   "best_intentions",
                   "fast_drive",
                   "general_trust",
                   "plans_to_move_WP85",
                   "where_to_move_WP3120",
                   ]


class Income(Page):
    form_fields = [
        "income_diff",
        "reduce_income_diff",
        "regional_diff",
        "regional_average_income",
        "regional_income_changed",
        "relative_income", ]


class City(Page):
    form_fields = [
        "your_city",
    ]


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
    form_model = 'player'
    form_fields = [
        'lits_equal',
        'lits_ownership',
        'lits_competition',
        'lits_obey',
        'lits_authorities',
        'lits_wealthy',
        'lits_party'

    ]

    def vars_for_template(self):
        items = [
            dict(name='lits_equal',
                 left="Нужно уменьшить разницу доходов",
                 right="Нужно увеличить разницу доходов, чтобы люди прилагали больше усилий"),
            dict(name='lits_ownership',
                 left="Долю частной собственности в бизнесе и промышленности следует увеличить",
                 right="Нужно увеличить долю государственной собственности в бизнесе и промышленности"),
            dict(name='lits_competition',
                 left="Конкуренция - это хорошо. Она побуждает людей напряженно работать и развивать новые идеи.",
                 right="Конкуренция вредна: она пробуждает у людей их худшие качества."),
            dict(name='lits_obey', left="Люди должны подчиняться закону без исключения",
                 right="Бывают моменты, когда у людей есть веские причины нарушать закон", ),
            dict(name='lits_authorities',
                 left='Как граждане мы должны более активно подвергать сомнению действия наших властей',
                 right='Сегодня в нашей стране мы должны проявлять больше уважения к нашим властям'),
            dict(name='lits_wealthy',
                 left="То, что богатые люди влияют на то, как правительство управляет этой страной, не является проблемой",
                 right="Богатые люди часто используют свое влияние на правительство в своих собственных интересах, и для предотвращения этого необходимы более строгие правила"),
            dict(name='lits_party',
                 left="Финансовая поддержка политических партий и кандидатов, оказываемая частными компаниями, должна быть полностью запрещена",
                 right="Не должно быть никаких ограничений на финансовую поддержку политических партий или кандидатов, оказываемую частными компаниями")

        ]
        return dict(choices=range(1, 11), items=items)


class Big5(Page):
    template_name = 'q/Big5.html'

    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('big5')
        if data:
            for k, v in data.items():
                setattr(self.player, k, v.get('col1'))
        return super().post()


class AltruismAndTrust(Page):
    template_name = 'q/AltruismAndTrust.html'

    def post(self):
        data = json.loads(self.request.POST.get('surveyholder'))
        altruism = data.get('altruism')
        if altruism:
            for k, v in altruism.items():
                setattr(self.player, k, v)
        return super().post()


class Risk(Page):
    template_name = 'q/Risk.html'

    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('risk')
        if data:
            for k, v in data.items():
                setattr(self.player, k, v.get('col1'))
        return super().post()


class Patience(Page):
    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('patience')
        if data:
            for k, v in data.items():
                setattr(self.player, k, v.get('col1'))
        return super().post()

    template_name = 'q/Patience.html'


class Demographics(Page):
    form_fields = [
        "years_lived_current_city",
        "years_lived_birth_city",
        "lived_other_city",
        'previous_experiment',
        "previous_experiment_cities"
    ]


class ChildrenQualities(Page):
    template_name = 'q/ChildrenQualities.html'

    def post(self):
        data = json.loads(self.request.POST.get('surveyholder')).get('children_qualities')
        if data:
            for i in data:
                if hasattr(self.player, i):
                    setattr(self.player, i, 1)
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
    # Consent,
    # Welcome,
    # City,
    # Income,
    IncomeScale,
    IncomeScaleFamily,
    IncomePyramid,
    IncomePyramidRegional,
    Lits2020,
    AltruismAndTrust,
    Patience,
    # Big5,
    # Risk,
    ChildrenQualities,
    Demographics,
    SES,
    Last
]
