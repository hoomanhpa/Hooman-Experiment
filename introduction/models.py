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
    name_in_url = 'introduction'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.StringField(choices=["male", "female"], widget=widgets.RadioSelectHorizontal, label="Gender")
    age = models.IntegerField(label="How old are you?:")
    musical_background = models.StringField(choices=["Yes", "No"], label="Do you have a muisical background? (for example playing an instrument or ...)")
    """ question1 = models.StringField(choices=[["right","right"],["false","false"]], widget=widgets.RadioSelectHorizontal, label="The client cares the most about owning special items. Quality and price are the next priorities for him.")
    question2 = models.StringField(choices=[["right","right"],["false", "false"]], widget=widgets.RadioSelectHorizontal, label="There are 4 products on the shopping list. Those producst have to be purchased.")
    question3 = models.StringField(choices=[["false","right"],["right","false"]], widget=widgets.RadioSelectHorizontal, label="Products with higher prices will definitely result in higher payout for you.")
    question4 = models.StringField(choices=[["right","right"], ["false","false"]], widget=widgets.RadioSelectHorizontal, label="If you buy more than 4 products, you have a chance for a higher payout, but also the risk of a reducing your payout")
    question5 = models.StringField(choices=[["false","right"],["right","false"]], widget=widgets.RadioSelectHorizontal, label="Items not included on the shopping list have to be purchased")
     """
    question1 = models.StringField()
    question2 = models.StringField()
    question3 = models.StringField()
    question4 = models.StringField()
    question5 = models.StringField() 