import re
class Card:
    def __init__(self, row):
        card_num, patte = row.split(':')
        self.card_num = int(re.findall(r'\d+', card_num)[0])
        jeete, mere_patte = patte.strip().split('|')
        self.jeete = re.findall(r'\d+', jeete)
        self.mere_patte = re.findall(r'\d+', mere_patte)
        self.matches=0
        
    def __repr__(self):
        return f'Winning cards: {self.jeete}\nMy cards: {self.mere_patte}'
    
    def calculate_points(self):
        matches=0
        for my_card in self.mere_patte:
            if my_card in self.jeete:
                matches+=1
        self.matches = matches
        return matches

    def calculate_score(self):
        matches = self.calculate_points()
        if matches==0:
            return 0
        else:
            return 2 ** (matches-1)
