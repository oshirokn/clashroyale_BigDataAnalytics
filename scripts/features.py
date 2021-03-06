import os
import pandas as pd
from numpy import asarray
from numpy import save

def features():
    win_columns = ['winner.card1.id', 
            'winner.card2.id',
            'winner.card3.id', 
            'winner.card4.id',
            'winner.card5.id', 
            'winner.card6.id',
            'winner.card7.id', 
            'winner.card8.id',
            "winner.totalcard.level",
            "winner.troop.count",
            'winner.structure.count',
            'winner.spell.count',
            'winner.common.count',
            'winner.rare.count',
            'winner.epic.count',
            'winner.legendary.count']

    loose_columns = ['loser.card1.id', 
            'loser.card2.id',
            'loser.card3.id', 
            'loser.card4.id',
            'loser.card5.id', 
            'loser.card6.id',
            'loser.card7.id', 
            'loser.card8.id',
            "loser.totalcard.level",
            "loser.troop.count",
            'loser.structure.count',
            'loser.spell.count',
            'loser.common.count',
            'loser.rare.count',
            'loser.epic.count',
            'loser.legendary.count']
    return win_columns,loose_columns