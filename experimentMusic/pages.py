from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass

class SAM(Page):
    form_model = 'player'
    form_fields = ['pleasure', 'arousal', 'dominance']

class CognitionSurvey(Page):
    form_model = 'player'
    form_fields = ['cognition']

    def js_vars(self):
        return dict(
            round_current=self.round_number,
            cognition=self.player.cognition,   
        )

class PaymentFinal(Page):
    form_model = 'player'

    def js_vars(self):
        return dict(
            payment_final = self.player.paymentplayer,
        )


class Product(Page):
    form_model ='player'
    form_fields = ['musicPlayed','paymentplayer', 'sumofprices', 'volume_button_clicked',
                    'choice00','choice01','choice02','choice03','choice04','choice05','choice06','choice07',
                    'choice10','choice11','choice12','choice13','choice14','choice15','choice16','choice17',
                    'choice20','choice21','choice22','choice23','choice24','choice25','choice26','choice27',
                    'choice30','choice31','choice32','choice33','choice34','choice35','choice36','choice37',
                    'choice40','choice41','choice42','choice43','choice44','choice45','choice46','choice47',
                    'choice50','choice51','choice52','choice53','choice54','choice55','choice56','choice57',
                    'choice60','choice61','choice62','choice63','choice64','choice65','choice66','choice67',
                    'choice70','choice71','choice72','choice73','choice74','choice75','choice76','choice77',
                    'time_choice0', 'time_choice1', 'time_choice2', 'time_choice3', 'time_choice4', 'time_choice5', 'time_choice6', 'time_choice7'
                  ]
    

    #'hasAdded'

    def js_vars(self):
        return dict(
            paymentplayer = self.player.paymentplayer,
            sumofprices = self.player.sumofprices,
            round_current=self.round_number,
            shopList=Constants.shoppinglist,
            musicList=Constants.musiclist,
            choice00 = self.player.choice00,
            choice01 = self.player.choice01,
            choice02 = self.player.choice02,
            choice03 = self.player.choice03,
            choice04 = self.player.choice04,
            choice05 = self.player.choice05,
            choice06 = self.player.choice06,
            choice07 = self.player.choice07,
            choice10 = self.player.choice10,
            choice11 = self.player.choice11,
            choice12 = self.player.choice12,
            choice13 = self.player.choice13,
            choice14 = self.player.choice14,
            choice15 = self.player.choice15,
            choice16 = self.player.choice16,
            choice17 = self.player.choice17,
            choice20 = self.player.choice20,
            choice21 = self.player.choice21,
            choice22 = self.player.choice22,
            choice23 = self.player.choice23,
            choice24 = self.player.choice24,
            choice25 = self.player.choice25,
            choice26 = self.player.choice26,
            choice27 = self.player.choice27,
            choice30 = self.player.choice30,
            choice31 = self.player.choice31,
            choice32 = self.player.choice32,
            choice33 = self.player.choice33,
            choice34 = self.player.choice34,
            choice35 = self.player.choice35,
            choice36 = self.player.choice36,
            choice37 = self.player.choice37,
            choice40 = self.player.choice40,
            choice41 = self.player.choice41,
            choice42 = self.player.choice42,
            choice43 = self.player.choice43,
            choice44 = self.player.choice44,
            choice45 = self.player.choice45,
            choice46 = self.player.choice46,
            choice47 = self.player.choice47,
            choice50 = self.player.choice50,
            choice51 = self.player.choice51,
            choice52 = self.player.choice52,
            choice53 = self.player.choice53,
            choice54 = self.player.choice54,
            choice55 = self.player.choice55,
            choice56 = self.player.choice56,
            choice57 = self.player.choice57,
            choice60 = self.player.choice60,
            choice61 = self.player.choice61,
            choice62 = self.player.choice62,
            choice63 = self.player.choice63,
            choice64 = self.player.choice64,
            choice65 = self.player.choice65,
            choice66 = self.player.choice66,
            choice67 = self.player.choice67,
            choice70 = self.player.choice70,
            choice71 = self.player.choice71,
            choice72 = self.player.choice72,
            choice73 = self.player.choice73,
            choice74 = self.player.choice74,
            choice75 = self.player.choice75,
            choice76 = self.player.choice76,
            choice77 = self.player.choice77,
           
        )


page_sequence = [Product, SAM, PaymentFinal] #, CognitionSurvey, SAM]
