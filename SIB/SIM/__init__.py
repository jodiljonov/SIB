from otree.api import *

c = Currency

doc = """
SIM
"""


class Constants(BaseConstants):
    name_in_url = 'SIM'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
   pass


# PAGES
class Instructions(Page):
    pass



page_sequence = [Instructions]