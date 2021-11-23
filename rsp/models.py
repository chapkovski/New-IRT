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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'rsp'
    players_per_group = None
    num_rounds = 1
    loss = 0
    win = 2
    tie = 1
    num_rounds = 10
    payoff_matrix = {
        0: {0: tie,
            1: win,
            2: loss},
        1: {0: loss,
            1: tie,
            2: win},
        2: {0: win,
            1: loss,
            2: tie},
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    blocked = models.BooleanField(initial=False)

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.payoff_matrix[p1.decision][p2.decision]
        p2.payoff = Constants.payoff_matrix[p2.decision][p1.decision]
        for p in self.get_players():
            p.written_outcome = p.get_written_outcome()


class Player(BasePlayer):
    @property
    def other(self):
        return self.get_others_in_group()[0]

    def get_written_outcome(self):
        if self.payoff == Constants.win:
            return 'won'
        if self.payoff == Constants.loss:
            return 'lost'
        if self.payoff == Constants.tie:
            return 'tie'

    def outcome(self):
        if self.payoff == Constants.win:
            return 'Вы выиграли!'
        if self.payoff == Constants.loss:
            return 'Вы проиграли'
        if self.payoff == Constants.tie:
            return 'Ничья!'

    written_outcome = models.StringField()
    decision = models.IntegerField(label='Выберите одно из:',
                                   choices=[
                                       (0, 'Камень'),
                                       (1, 'Ножницы'),
                                       (2, 'Бумага'),
                                   ],
                                   widget=widgets.RadioSelect)
