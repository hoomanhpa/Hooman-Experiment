from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass

class GeneralInformation(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'musical_background']

class Senario(Page):
    pass

class Structure(Page):
    pass

class Payment(Page):
    pass

class Questions(Page):
    form_model = 'player'
    form_fields = ['question1', 'question2', 'question3', 'question4', 'question5']

page_sequence = [GeneralInformation, Senario, Structure, Payment, Questions]
