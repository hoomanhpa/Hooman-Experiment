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
import json 
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'experimentMusic'
    players_per_group = None
    num_rounds = 1
 
    with open('C:\\Files\\Test\\oTreeonlineshop-master\\shop\\oTree\\experimentMusic\\products.json', 'r', encoding='utf-8') as jsonfile:
        data=jsonfile.read()
        shoppinglist = json.loads(data)
    
    with open('C:\\Files\\Test\\oTreeonlineshop-master\\shop\\oTree\\experimentMusic\\music.json', 'r', encoding='utf-8') as jsonfile:
        data=jsonfile.read()
        musiclist = json.loads(data)
   
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    arousal = models.StringField(choices=[["1", ""], ["2", ""], ["3", ""], ["4", ""], ["5", ""]], widget=widgets.RadioSelectHorizontal, label="labb")
    pleasure = models.StringField(choices=[["1", ""], ["2", ""], ["3", ""], ["4", ""], ["5", ""]], widget=widgets.RadioSelectHorizontal, label="labb")
    dominance = models.StringField(choices=[["1", ""], ["2", ""], ["3", ""], ["4", ""], ["5", ""]], widget=widgets.RadioSelectHorizontal, label="labb")
    paymentplayer = models.StringField(blank=True)
    sumofprices = models.StringField(blank=True)
    musicPlayed = models.StringField(blank=True)
    volume_button_clicked = models.StringField(blank=True) 
    time_choice0 = models.StringField(blank=True)
    time_choice1 = models.StringField(blank=True)
    time_choice2 = models.StringField(blank=True)
    time_choice3 = models.StringField(blank=True)
    time_choice4 = models.StringField(blank=True)
    time_choice5 = models.StringField(blank=True)
    time_choice6 = models.StringField(blank=True)
    time_choice7 = models.StringField(blank=True)
    
    choice00 = models.StringField(blank=True)
    choice01 = models.StringField(blank=True)
    choice02 = models.StringField(blank=True)
    choice03 = models.StringField(blank=True)
    choice04 = models.StringField(blank=True)
    choice05 = models.StringField(blank=True)
    choice06 = models.StringField(blank=True)
    choice07 = models.StringField(blank=True)
    choice10 = models.StringField(blank=True)
    choice11 = models.StringField(blank=True)
    choice12 = models.StringField(blank=True)
    choice13 = models.StringField(blank=True)
    choice14 = models.StringField(blank=True)
    choice15 = models.StringField(blank=True)
    choice16 = models.StringField(blank=True)
    choice17 = models.StringField(blank=True)
    choice20 = models.StringField(blank=True)
    choice21 = models.StringField(blank=True)
    choice22 = models.StringField(blank=True)
    choice23 = models.StringField(blank=True)
    choice24 = models.StringField(blank=True)
    choice25 = models.StringField(blank=True)
    choice26 = models.StringField(blank=True)
    choice27 = models.StringField(blank=True)
    choice30 = models.StringField(blank=True)
    choice31 = models.StringField(blank=True)
    choice32 = models.StringField(blank=True)
    choice33 = models.StringField(blank=True)
    choice34 = models.StringField(blank=True)
    choice35 = models.StringField(blank=True)
    choice36 = models.StringField(blank=True)
    choice37 = models.StringField(blank=True)
    choice40 = models.StringField(blank=True)
    choice41 = models.StringField(blank=True)
    choice42 = models.StringField(blank=True)
    choice43 = models.StringField(blank=True)
    choice44 = models.StringField(blank=True)
    choice45 = models.StringField(blank=True)
    choice46 = models.StringField(blank=True)
    choice47 = models.StringField(blank=True)
    choice50 = models.StringField(blank=True)
    choice51 = models.StringField(blank=True)
    choice52 = models.StringField(blank=True)
    choice53 = models.StringField(blank=True)
    choice54 = models.StringField(blank=True)
    choice55 = models.StringField(blank=True)
    choice56 = models.StringField(blank=True)
    choice57 = models.StringField(blank=True)
    choice60 = models.StringField(blank=True)
    choice61 = models.StringField(blank=True)
    choice62 = models.StringField(blank=True)
    choice63 = models.StringField(blank=True)
    choice64 = models.StringField(blank=True)
    choice65 = models.StringField(blank=True)
    choice66 = models.StringField(blank=True)
    choice67 = models.StringField(blank=True)
    choice70 = models.StringField(blank=True)
    choice71 = models.StringField(blank=True)
    choice72 = models.StringField(blank=True)
    choice73 = models.StringField(blank=True)
    choice74 = models.StringField(blank=True)
    choice75 = models.StringField(blank=True)
    choice76 = models.StringField(blank=True)
    choice77 = models.StringField(blank=True)




    

