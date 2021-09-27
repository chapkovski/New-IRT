from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
# from .widgets import OtherRadioSelect
from django.utils.translation import gettext_lazy as _

from .widgets import LikertWidget


doc = """
 Questionnaire for new IRT project. 
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1
    HARD_TO_SAY_CHOICE = [999, _('Hard to say')]
    GENDER_CHOICES = [[0, _('Male')], [1, _('Female')]]

    BEST_INTENSIONS_CHOICES = [
        [0, _('0 - Totally disagree')],
        [1, '1'],
        [2, '2'],
        [3, '3'],
        [4, '4'],
        [5, '5'],
        [6, '6'],
        [7, '7'],
        [8, '8'],
        [9, '9'],
        [10, _('10 - Totally agree')],
        HARD_TO_SAY_CHOICE
    ]

    smoke_choices = [
        [0, _('Never')],
        [1, _('Occasionally')],
        [2, _('Frequently')],
        HARD_TO_SAY_CHOICE
    ]

    fast_drive_choices = [
        [0, _('Never')],
        [1, _('Occasionally')],
        [2, _('Frequently')],
        [3, _('I do not drive')],
        HARD_TO_SAY_CHOICE
    ]

    agreement_choices_5DNK = [
        [1, _('Totally disagree')],
        [2, _('Somewhat disagree')],
        [3, _('Neither agree nor disagree')],
        [4, _('Somewhat agree')],
        [5, _('Absolutely agree')],
        HARD_TO_SAY_CHOICE
    ]

    income_choices = [
        [1, _('Not even enough money for food')],
        [2, _('Enough for food, but not enough to buy clothes and shoes')],
        [3, _('Enough for clothes and shoes, but not enough to buy small appliances')],
        [4, _(
            'Enough money for small purchases, but buying expensive things (computer, washing machine, refrigerator) requires savings or credit')],
        [5, _(
            'Have enough money to buy for the house, but to buy a car, dacha, apartment requires saving or taking a loan')],
        [6, _('Can afford any purchases without restrictions or credit')],
        HARD_TO_SAY_CHOICE
    ]

    regional_income_changed_choices = [
        [1, _('It became substantially smaller than a year ago')],
        [2, _('It became a bit smaller than a year ago')],
        [3, _('It did not change')],
        [4, _('It became a bit larger than a year ago')],
        [5, _('It became substantially large than a year ago')],
        HARD_TO_SAY_CHOICE
    ]

    relative_income_choices = [
        [1, _('lower than the average in your city')],
        [2, _('the same as the average in your city')],
        [3, _('higher than the average in your city')],
        HARD_TO_SAY_CHOICE
    ]

    Patience_10 = [
        [0, _('0 - Totally unwilling to so')],
        [1, '1'],
        [2, '2'],
        [3, '3'],
        [4, '4'],
        [5, '5'],
        [6, '6'],
        [7, '7'],
        [8, '8'],
        [9, '9'],
        [10, _('10 - Totally willing to do so')],
        HARD_TO_SAY_CHOICE
    ]

    RISK_CHOICES = range(0, 11)

    ready_help_choices = [
        [0, _('0 - Completely unwilling to spend money')],
        [1, '1'],
        [2, '2'],
        [3, '3'],
        [4, '4'],
        [5, '5'],
        [6, '6'],
        [7, '7'],
        [8, '8'],
        [9, '9'],
        [10, _('10 - Very willing to spend money')],
        HARD_TO_SAY_CHOICE
    ]

    Yes_No = [
        [0, _('No')],
        [1, _('Yes')],
        HARD_TO_SAY_CHOICE
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    inequality_with_images =models.IntegerField(label='Dont forget about images!!!')
    gender = models.BooleanField(initial=None,
                                 choices=Constants.GENDER_CHOICES,
                                 label=_('Indicate your gender'),
                                 widget=widgets.RadioSelect()
                                 )

    smoke = models.PositiveIntegerField(
        label=_('How frequently do you smoke?'),
        choices=Constants.smoke_choices,
        widget=widgets.RadioSelect()
    )
    best_intentions = models.PositiveIntegerField(
        label=_('I assume that people have only the best intentions'),
        choices=Constants.BEST_INTENSIONS_CHOICES,
        widget=widgets.RadioSelect()
    )
    fast_drive = models.PositiveIntegerField(
        label=_('How often do you drive faster with your car than allowed by the traffic regulations?'),
        choices=Constants.fast_drive_choices,
        widget=widgets.RadioSelect()
    )




    income_diff = models.PositiveIntegerField(
        label=_('Differences in income in Russia are too large'),
        choices=Constants.agreement_choices_5DNK,
        widget=widgets.RadioSelect()
    )

    reduce_income_diff = models.PositiveIntegerField(
        label=_(
            'It is the responsibility of the government to reduce the differences in income between people with high incomes and those with low incomes'),
        choices=Constants.agreement_choices_5DNK,
        widget=widgets.RadioSelect()
    )

    income = models.PositiveIntegerField(
        label=_('Which statement best describes the financial situation in your family?'),
        choices=Constants.income_choices,
        widget=widgets.RadioSelect()
    )
    fin_situation_change = models.PositiveIntegerField(
        blank=True,
        choices=Constants.income_choices,
        widget=widgets.RadioSelect,
        label=_(
            """Did your family financial situation change over the last year - How would you answer the previous question a year ago?""")
    )

    regional_average_income = models.PositiveIntegerField(
        label=_(
            'In your opinion, what is the average monthly income of the residents of your region? Please write your estimate (in rubles per month)'),
    )

    regional_diff = models.PositiveIntegerField(
        label=_(
            'Do you agree with the statement that the differences in the level of income between the regions of Russia are unjustifiably large?'),
        choices=Constants.agreement_choices_5DNK,
        widget=widgets.RadioSelect()
    )

    regional_income_changed = models.PositiveIntegerField(
        label=_(
            'In your opinion, did the the average monthly income of the residents of your region change over the last year?'),
        choices=Constants.regional_income_changed_choices,
        widget=widgets.RadioSelect()
    )

    relative_income = models.PositiveIntegerField(
        label=_('Your average monthly income...'),
        choices=Constants.relative_income_choices,
        widget=widgets.RadioSelect()
    )

    # Patience_10
    patience_1 = models.IntegerField(label=_(
        'How willing are you to give up something that is beneficial for you today in order to benefit more from that in the future?'),
                                        choices=Constants.Patience_10, widget=widgets.RadioSelect)
    patience_2 = models.IntegerField(label=_(
        ' How willing are you to punish someone who treats others unfairly, even if there may be costs for you?'),
                                        choices=Constants.Patience_10, widget=widgets.RadioSelect)
    patience_3 = models.IntegerField(label=_('When someone does me a favor, I am willing to return it'),
                                        choices=Constants.Patience_10, widget=widgets.RadioSelect)
    patience_4 = models.IntegerField(label=_(
        'If I have been treated unfairly, I will retaliate at the first opportunity, even if it costs me a lot'),
                                        choices=Constants.Patience_10, widget=widgets.RadioSelect)

    # Risk
    risk_general = models.PositiveIntegerField(
        label='',
        choices=Constants.RISK_CHOICES,
        widget=LikertWidget(
            quote=_(
                "Please, indicate your general attitude to risk"),
            label=_(
                """. Please indicate your answer on a scale from 0 to 10. A 0 means “completely unwilling to take risk,” and a 10 means “very willing to take risk.”
                """),
            left=_('I am completely unwilling to take risk'),
            right=_('I am very willing to take risk'),
        )
    )

    risk_fin = models.PositiveIntegerField(
        label=_("""In financial matters'"""),
        choices=Constants.RISK_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    risk_sport = models.PositiveIntegerField(
        label=_("""In leisure and sport"""),
        choices=Constants.RISK_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    risk_prof = models.PositiveIntegerField(
        label=_("""In professional career"""),
        choices=Constants.RISK_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    risk_health = models.PositiveIntegerField(
        label=_("""In health"""),
        choices=Constants.RISK_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    risk_strangers = models.PositiveIntegerField(
        label=_("""With strangers"""),
        choices=Constants.RISK_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )
    risk_drive = models.PositiveIntegerField(
        label=_("""While driving"""),
        choices=Constants.RISK_CHOICES,
        widget=widgets.RadioSelectHorizontal()
    )

    ready_help = models.IntegerField(
        label=_('Willingness to spend money even at not return'),
        choices=Constants.ready_help_choices,
        widget=widgets.RadioSelect)

    # Yes/No questions
    donated_money = models.IntegerField(label=_('Have you donated money in the previous 12 months?'),
                                        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    count_on_relatives = models.IntegerField(
        label=_('Do you have relatives or friends you can count on to help you whenever needed?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    help_stranger = models.IntegerField(label=_('Did you help a stranger in the previous 12 months who needed help?'),
                                        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    self_employed = models.IntegerField(label=_('Are you self-employed?'), choices=Constants.Yes_No,
                                        widget=widgets.RadioSelect)
    own_business = models.IntegerField(
        label=_('For those who are not self-employed: Are you planning to start your own business?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    save_money = models.IntegerField(label=_('Did you save any money in the previous 12 months?'),
                                     choices=Constants.Yes_No, widget=widgets.RadioSelect)
    fin_help = models.IntegerField(
        label=_('Did you send help (money or goods) to another individual in the previous 12 months?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    vore_official = models.IntegerField(
        label=_('Did you voice your opinion to a public official in the previous 12 months?'), choices=Constants.Yes_No,
        widget=widgets.RadioSelect)
    volunteer = models.IntegerField(
        label=_('Did you voluntarily devote time to an organization in the previous 12 months?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    police_confidence = models.IntegerField(
        label=_('In the city or area where you live, do you have confidence in the local police force?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    safety = models.IntegerField(label=_('Do you feel safe walking alone at night in the city or area where you live?'),
                                 choices=Constants.Yes_No, widget=widgets.RadioSelect)
    stolen_money = models.IntegerField(
        label=_('Has money or property been stolen from you or another household member within the last 12 months? '),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    used_trust = models.IntegerField(label=_('Did someone take advantage of your trust in the last 6 months?'),
                                     choices=Constants.Yes_No, widget=widgets.RadioSelect)
    reciprocated_trust = models.IntegerField(
        label=_('Did you experience a positive response in the last 6 months when you trusted someone?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    disappointed_trust = models.IntegerField(
        label=_('Have you disappointed someone in the last 6 months who has trusted you?'), choices=Constants.Yes_No,
        widget=widgets.RadioSelect)
    donated_blood = models.IntegerField(label=_('Did you donate blood during the last 6 months?'),
                                        choices=Constants.Yes_No, widget=widgets.RadioSelect)

    # Big 5
    big5_1 = models.IntegerField(label=_('I see myself as someone who is reserved'),
                                 choices=Constants.agreement_choices_5DNK, widget=widgets.RadioSelect)
    big5_2 = models.IntegerField(label=_('I see myself as someone who is generally trusting'),
                                 choices=Constants.agreement_choices_5DNK, widget=widgets.RadioSelect)
    big5_3 = models.IntegerField(label=_('I see myself as someone who tends to be lazy'),
                                 choices=Constants.agreement_choices_5DNK, widget=widgets.RadioSelect)
    big5_4 = models.IntegerField(label=_('I see myself as someone who is relaxed, handles stress well'),
                                 choices=Constants.agreement_choices_5DNK, widget=widgets.RadioSelect)
    big5_5 = models.IntegerField(label=_('I see myself as someone who has few artistic interests'),
                                 choices=Constants.agreement_choices_5DNK, widget=widgets.RadioSelect)
    big5_6 = models.IntegerField(label=_('I see myself as someone who is outgoing, sociable'),
                                 choices=Constants.agreement_choices_5DNK, widget=widgets.RadioSelect)
    big5_7 = models.IntegerField(label=_('I see myself as someone who tends to find fault with others'),
                                 choices=Constants.agreement_choices_5DNK, widget=widgets.RadioSelect)
    big5_8 = models.IntegerField(label=_('I see myself as someone who does a thorough job'),
                                 choices=Constants.agreement_choices_5DNK, widget=widgets.RadioSelect)
    big5_9 = models.IntegerField(label=_('I see myself as someone who gets nervous easily'),
                                 choices=Constants.agreement_choices_5DNK, widget=widgets.RadioSelect)
    big5_10 = models.IntegerField(label=_('I see myself as someone who has an active imagination'),
                                  choices=Constants.agreement_choices_5DNK, widget=widgets.RadioSelect)
    big5_11 = models.IntegerField(label=_('I see myself as someone who is reserved'),
                                  choices=Constants.agreement_choices_5DNK, widget=widgets.RadioSelect)
