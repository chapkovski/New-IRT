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
    HARD_TO_SAY_CHOICE = [999, _('Затрудняюсь ответить')]
    GENDER_CHOICES = [[0, _('Мужской')], [1, _('Женский')]]

    BEST_INTENSIONS_CHOICES = [
        [0, _('0 - Совершенно не согласен/согласна')],
        [1, '1'],
        [2, '2'],
        [3, '3'],
        [4, '4'],
        [5, '5'],
        [6, '6'],
        [7, '7'],
        [8, '8'],
        [9, '9'],
        [10, _('10 - Совершенно согласен/согласна')],

    ]

    smoke_choices = [
        [0, _('Никогда')],
        [1, _('Время от времени')],
        [2, _('Часто')],
        HARD_TO_SAY_CHOICE
    ]

    fast_drive_choices = [
        [0, _('Никогда')],
        [1, _('Время от времени')],
        [2, _('Часто')],
        [3, _('Я не вожу машину')],
        HARD_TO_SAY_CHOICE
    ]

    agreement_choices_5DNK = [
        [1, _('Совершенно не согласен/согласна')],
        [2, _('Скорее не согласен/согласна')],
        [3, _('Ни то чтобы согласен/согласна – ни то чтобы нет')],
        [4, _('Скорее согласен/согласна')],
        [5, _('Совершенно согласен/согласна')],
        HARD_TO_SAY_CHOICE
    ]

    income_choices = [
        [1, _('Не хватает денег даже на еду')],
        [2, _('Хватает на еду, но не хватает на покупку одежды и обуви')],
        [3, _('Хватает на одежду и обувь, но не хватает на покупку мелкой бытовой техники')],
        [4, _(
            'Хватает денег на небольшие покупки, но покупка дорогих вещей (компьютера, стиральной машины, холодильника) требует накоплений или кредита')],
        [5, _(
            'Хватает денег на покупки для дома, но на покупку машины, дачи, квартиры необходимо копить или брать кредит')],
        [6, _('Можем позволить себе любые покупки без ограничений и кредитов')],
        HARD_TO_SAY_CHOICE
    ]

    regional_income_changed_choices = [
        [1, _('Он стал значительно меньше, чем год назад')],
        [2, _('Он стал немного меньше, чем год назад')],
        [3, _('Он не изменился')],
        [4, _('Он стал немного больше, чем год назад')],
        [5, _('Он стал значительно больше, чем год назад')],
        HARD_TO_SAY_CHOICE
    ]

    relative_income_choices = [
        [1, _('ниже, чем в среднем в вашем городе')],
        [2, _('такой же, как в среднем в вашем городе')],
        [3, _('выше, чем в среднем в вашем городе')],
        HARD_TO_SAY_CHOICE
    ]

    Patience_10 = [
        [0, _('0 - совершенно не готов(а) так поступать')],
        [1, '1'],
        [2, '2'],
        [3, '3'],
        [4, '4'],
        [5, '5'],
        [6, '6'],
        [7, '7'],
        [8, '8'],
        [9, '9'],
        [10, _('10 - готов(а) поступать именно так')],
        HARD_TO_SAY_CHOICE
    ]

    RISK_CHOICES = range(0, 11)

    Yes_No = [
        [0, _('Нет')],
        [1, _('Да')],
        HARD_TO_SAY_CHOICE
    ]

    City_interaction = [
        [0, _('Нет')],
        [1, _('Да')],
        [2, _('Не взаимодействовал(а)')],
        HARD_TO_SAY_CHOICE
    ]
    general_trust_choices = [
        [0, _('Нужно быть очень осторожным с другими людьми')],
        [1, _('Большинству людей вполне можно доверять')],
        HARD_TO_SAY_CHOICE
    ]
    cities = [
        [1, _('Воронеж (Воронежская область)')],
        [2, _('Владивосток (Приморский край)')],
        [3, _('Санкт-Петербург')],
        [4, _('Ростов-на-Дону (Ростовская область)')],
        [5, _('Пермь (Пермский край)')],
        [6, _('Новосибирск (Новосибирская область)')],
        [7, _('Москва')],
        [8, _('Махачкала (Дагестан)')],
        [9, _('Хабаровск (Хабаровский край)')],
        [10, _('Казань (Татарстан)')],
        [11, _('Екатеринбург (Свердловская область)')],
        [12, _('Архангельск (Архангельская область)')],
        [13, _('Другой')],

    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.BooleanField(initial=None,
                                 choices=Constants.GENDER_CHOICES,
                                 label=_('Укажите Ваш пол:'),
                                 widget=widgets.RadioSelect()
                                 )

    smoke = models.PositiveIntegerField(
        label=_('Как часто Вы курите?'),
        choices=Constants.smoke_choices,
        widget=widgets.RadioSelect()
    )
    general_trust = models.PositiveIntegerField(
        label=_(
            'Как Вы считаете, в целом большинству людей можно доверять, или же при общении с другими людьми осторожность никогда не повредит?'),
        choices=Constants.general_trust_choices,
        widget=widgets.RadioSelect()
    )

    best_intentions = models.PositiveIntegerField(
        label='Насколько хорошо следующее утверждение описывает вас как личность? <br> <i>"Я считаю, что люди имеют только лучшие намерения"</i>'
              '<br><small>Пожалуйста, дайте ответ по шкале от 0 до 10, где 0 означает “не описывает меня вообще,” а 10 означает “абсолютно верно меня описывает.”</small>',
        choices=Constants.BEST_INTENSIONS_CHOICES,
        widget=widgets.RadioSelect()
    )
    fast_drive = models.PositiveIntegerField(
        label=_('Как часто Вы ездите на своем автомобиле быстрее, чем разрешено правилами дорожного движения?'),
        choices=Constants.fast_drive_choices,
        widget=widgets.RadioSelect()
    )

    income_diff = models.PositiveIntegerField(
        label=_('Различия в доходах в России слишком велики:'),
        choices=Constants.agreement_choices_5DNK,
        widget=widgets.RadioSelect()
    )

    reduce_income_diff = models.PositiveIntegerField(
        label=_(
            'Правительство несет ответственность за сокращение различий в доходах между людьми с высокими доходами и людьми с низкими доходами:'),
        choices=Constants.agreement_choices_5DNK,
        widget=widgets.RadioSelect()
    )

    income = models.PositiveIntegerField(
        label=_('Какое высказывание наиболее точно описывает финансовое положение Вашей семьи?'),
        choices=Constants.income_choices,
        widget=widgets.RadioSelect()
    )
    fin_situation_change = models.PositiveIntegerField(
        blank=True,
        choices=Constants.income_choices,
        widget=widgets.RadioSelect,
        label=_(
            """Изменилось ли финансовое положение Вашей семьи за последние 12 месяцев? - Как бы Вы ответили на предыдущий вопрос год назад?""")
    )

    regional_average_income = models.PositiveIntegerField(
        label=_(
            'Как Вы считаете, каков среднемесячный доход жителей Вашего региона? Напишите, пожалуйста, Вашу оценку (в рублях в месяц):'),
    )

    regional_diff = models.PositiveIntegerField(
        label=_(
            'Согласны ли Вы с утверждением, что различия в уровне доходов между регионами России неоправданно велики?'),
        choices=Constants.agreement_choices_5DNK,
        widget=widgets.RadioSelect()
    )

    regional_income_changed = models.PositiveIntegerField(
        label=_(
            'По Вашему мнению, изменился ли среднемесячный доход жителей вашего региона за последние 12 месяцев?'),
        choices=Constants.regional_income_changed_choices,
        widget=widgets.RadioSelect()
    )

    relative_income = models.PositiveIntegerField(
        label=_('Ваш средний ежемесячный доход…'),
        choices=Constants.relative_income_choices,
        widget=widgets.RadioSelect()
    )
    # LITS
    lits_equal = models.IntegerField()
    lits_ownership = models.IntegerField()
    lits_competition = models.IntegerField()
    lits_obey = models.IntegerField()
    lits_authorities = models.IntegerField()
    lits_wealthy = models.IntegerField()
    lits_party = models.IntegerField()
    # LITS END

    # Patience_10
    patience_1 = models.IntegerField(label=_(
        'Насколько Вы готовы отказаться от чего-то выгодного для Вас сегодня, в пользу того, чтобы получить еще большую выгоду от этого в будущем?'),
        choices=Constants.Patience_10, widget=widgets.RadioSelect)
    patience_2 = models.IntegerField(label=_(
        'Насколько Вы готовы наказать кого-то, кто поступает несправедливо с другими, даже если это может дорого Вам обойтись?'),
        choices=Constants.Patience_10, widget=widgets.RadioSelect)
    patience_3 = models.IntegerField(label=_('Когда кто-либо мне помогает, я стараюсь ответить тем же.'),
                                     choices=Constants.Patience_10, widget=widgets.RadioSelect)
    patience_4 = models.IntegerField(label=_(
        'Если со мной поступили несправедливо, я отомщу при первом же удобном случае, даже если это дорого мне обойдется.'),
        choices=Constants.Patience_10, widget=widgets.RadioSelect)
    patience_5 = models.IntegerField(label=_(
        'Насколько Вы готовы совершать благородные поступки, ничего не ожидая взамен?'),
        choices=Constants.Patience_10, widget=widgets.RadioSelect)

    # Risk
    risk_general = models.PositiveIntegerField(
        label='',
        choices=Constants.RISK_CHOICES,
        widget=LikertWidget(
            quote=_(
                "Укажите, пожалуйста, насколько Вы любите рисковать?"),
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

    ## Income block 4 картинки вставить
    income_scale = models.IntegerField()
    income_scale_family = models.IntegerField()
    income_pyramid = models.IntegerField()
    income_pyramid_regional = models.IntegerField()
    # Yes/No questions
    donated_money = models.IntegerField(label=_('Жертвовали ли Вы деньги за предыдущие 12 месяцев?'),
                                        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    count_on_relatives = models.IntegerField(
        label=_(
            'Есть ли у Вас родственники или друзья, на помощь которых Вы можете рассчитывать в случае необходимости?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    help_stranger = models.IntegerField(
        label=_('Помогали ли Вы незнакомцу, который нуждался в помощи, за предыдущие 12 месяцев?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    self_employed = models.IntegerField(label=_('Являетесь ли Вы в настоящее время самозанятым?'),
                                        choices=Constants.Yes_No,
                                        widget=widgets.RadioSelect)
    own_business = models.IntegerField(
        label=_('Для тех, кто не является самозанятым: Планируете ли Вы начать свой собственный бизнес?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    save_money = models.IntegerField(label=_('Сэкономили ли Вы какие-либо деньги за предыдущие 12 месяцев?'),
                                     choices=Constants.Yes_No, widget=widgets.RadioSelect)
    fin_help = models.IntegerField(
        label=_('Отправляли ли Вы помощь (деньги или товары) другому лицу в течение предыдущих 12 месяцев?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    vote_official = models.IntegerField(
        label=_('Высказывали ли Вы свое мнение государственному должностному лицу в течение предыдущих 12 месяцев?'),
        choices=Constants.Yes_No,
        widget=widgets.RadioSelect)
    volunteer = models.IntegerField(
        label=_('Посвящали ли Вы добровольно время какой-либо организации в течение предыдущих 12 месяцев?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    police_confidence = models.IntegerField(
        label=_('В городе или районе, где Вы живете, доверяете ли Вы местной полиции?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    safety = models.IntegerField(
        label=_('Чувствуете ли Вы себя в безопасности, гуляя ночью в одиночестве по городу или району, где Вы живете?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    stolen_money = models.IntegerField(
        label=_('Были ли украдены деньги или имущество у Вас или другого члена семьи в течение последних 12 месяцев?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    used_trust = models.IntegerField(label=_('Воспользовался ли кто-нибудь Вашим доверием за последние 12 месяцев?'),
                                     choices=Constants.Yes_No, widget=widgets.RadioSelect)
    reciprocated_trust = models.IntegerField(
        label=_('За последние 12 месяцев, когда Вы кому-то доверяли, было ли Ваше доверие вознаграждено?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    disappointed_trust = models.IntegerField(
        label=_('За последние 12 месяцев разочаровывали ли Вы кого-то, кто Вам доверял? '), choices=Constants.Yes_No,
        widget=widgets.RadioSelect)
    donated_blood = models.IntegerField(label=_('Вы сдавали донорскую кровь в течение последних 12 месяцев?'),
                                        choices=Constants.Yes_No, widget=widgets.RadioSelect)

    # Children qualities
    good_manners = models.IntegerField(label=_(''),
                                       choices=Constants.Yes_No, widget=widgets.RadioSelect)

    independence = models.IntegerField(label=_(''),
                                       choices=Constants.Yes_No, widget=widgets.RadioSelect)

    hard_work = models.IntegerField(label=_(''),
                                    choices=Constants.Yes_No, widget=widgets.RadioSelect)

    responsibility = models.IntegerField(label=_(''),
                                         choices=Constants.Yes_No, widget=widgets.RadioSelect)

    imagination = models.IntegerField(label=_(''),
                                      choices=Constants.Yes_No, widget=widgets.RadioSelect)

    respectful_and_tolerant = models.IntegerField(label=_(''),
                                                  choices=Constants.Yes_No, widget=widgets.RadioSelect)

    thrift = models.IntegerField(label=_(''),
                                 choices=Constants.Yes_No, widget=widgets.RadioSelect)

    determination = models.IntegerField(label=_(''),
                                        choices=Constants.Yes_No, widget=widgets.RadioSelect)

    religious = models.IntegerField(label=_(''),
                                    choices=Constants.Yes_No, widget=widgets.RadioSelect)

    unselfishness = models.IntegerField(label=_(''),
                                        choices=Constants.Yes_No, widget=widgets.RadioSelect)

    obedience = models.IntegerField(label=_(''),
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

    # Demographics
    years_lived_current_city = models.PositiveIntegerField(
        label=_(
            'Пожалуйста, припомните город, в котором Вы жили в июле 2020 года. Сколько лет Вы уже прожили в названном городе на июль 2020 года?'),
    )
    years_lived_birth_city = models.PositiveIntegerField(
        label=_(
            'Сколько лет Вы прожили в городе, в котором Вы родились?'),
    )
    lived_other_city = models.IntegerField(label=_(
        'Жили ли Вы в каком-либо другом городе в октябре 2020 года?'),
        choices=Constants.Yes_No, widget=widgets.RadioSelect)
    previous_experiment = models.LongStringField(label="""
     В другом эксперименте на "Толоке" Вы взаимодействовали с участниками из других городов. Вы помните, в чем заключался эксперимент?""")
    previous_experiment_cities = models.LongStringField(
        label="""Помните ли Вы какие-либо другие города, откуда были участники, с которыми Вы взаимодействовали?""")

    your_city = models.IntegerField(label=_(
        'В каком городе Вы живете?'),
        choices=Constants.cities, widget=widgets.RadioSelect)
    plans_to_move_WP85 = models.IntegerField(
        label='В ближайшие 12 месяцев какова вероятность того, что вы переедете из города или района, где вы сейчас живете?',
        choices=[(1, "Да, это вероятно"),
                 (2, "Нет, это маловероятно"),
                 (999, 'Затрудняюсь ответить')
                 ],
        widget=widgets.RadioSelect
    )
    where_to_move_WP3120 = models.StringField(
        blank=True,
        label='Если есть вероятность, что вы переедете, то куда конкретно?',

    )
