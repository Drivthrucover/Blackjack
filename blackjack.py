import random
class BlackJack:

    def __init__(self):
        self.deck = [
            'A',2,3,4,5,6,7,8,9,10,'J','Q','K'
        ]
        self.values=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        card1=self.deck[random.randint(0,12)]
        card2=self.deck[random.randint(0,12)]
        self.hand=[card1,card2]
        self.current_total=0
        for i in self.hand:
            self.current_total+=self.values[self.deck.index(i)]

        dealer_card1=self.deck[random.randint(0,12)]
        dealer_card2=self.deck[random.randint(0,12)]
        self.dealer_hand=[dealer_card1,dealer_card2]
        self.dealer_current_total=0
        for i in self.dealer_hand:
            self.dealer_current_total+=self.values[self.deck.index(i)]

    def deal_cards(self):
        new_addition=self.deck[random.randint(0,12)]
        self.hand.append(new_addition)
        self.current_total+=self.values[self.deck.index(new_addition)]
        
    def play_game(self):
        print('[{}, ??]'.format(self.dealer_hand[0]))
        while self.current_total<21:
            print('{} | Your Current Total is:{}'.format(self.hand,self.current_total))
            decision=input('Would you like to HIT or STAY? ').upper()
            if decision=='HIT':
                self.deal_cards()
            elif decision=='STAY':
                return self.dealer_game()
            if self.current_total>21:
                if 'A' in self.hand:
                    self.current_total-=10
                else:
                    return 'YOU BUSTED {}'.format(self.hand)
            # if self.current_total==21:
            #      return 'YOU WON WITH A BLACKJACK | {} | {}'.format(self.hand, self.current_total)
    
    # def test_method(self):
    #     return 'Did it work?'
            
    def dealer_game(self):
        if self.dealer_current_total==21 or self.dealer_current_total>self.current_total:
            return 'YOU LOSE | {} vs {}'.format(self.hand, self.dealer_hand)
        if self.dealer_current_total==self.current_total:
            return 'PUSH | {} vs {} | tied at {}'.format(self.hand, self.dealer_hand, self.current_total)
        print('{} | {}'.format(self.dealer_hand, self.dealer_current_total))
        while self.dealer_current_total<self.current_total:
                card=self.deck[random.randint(0,12)]

                if self.dealer_current_total>self.current_total and self.dealer_current_total<=21:
                    return 'YOU LOSE | {} vs {}'.format(self.hand, self.dealer_hand)
                self.dealer_hand.append(card)
                self.dealer_current_total+=self.values[self.deck.index(card)]
                print('{} | {}'.format(self.dealer_hand, self.dealer_current_total))

                if self.dealer_current_total==self.current_total:
                    return 'PUSH | {} vs {} | tied at {}'.format(self.hand, self.dealer_hand, self.current_total)
                if self.dealer_current_total>self.current_total and self.dealer_current_total<=21:
                    return 'YOU LOSE | {} vs {}'.format(self.hand, self.dealer_hand)

                if self.dealer_current_total>21:
                    if 'A' in self.dealer_hand:
                        self.dealer_current_total-=10
                    else:
                        return 'YOU WIN | {} vs {}'.format(self.hand, self.dealer_hand)
        
game=BlackJack()
print(game.play_game())