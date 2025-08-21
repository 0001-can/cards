
import random
cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
cards_values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

def draw_card():
    return random.choice(cards)
def calculate_score(hand):
    score=sum(cards_values[card] for card in hand)

    if score>21 and 'A' in hand:
        ace_count=hand.count('A')

        while ace_count>0 and score >21:
            score -=10
            ace_count-=1
    return score

def print_hands(player_hand,dealer_hand,show_dealer=False):
    print("\n Senin kartların:",player_hand,"Toplam:",calculate_score(player_hand))

    if show_dealer:
        print("Krupiyenin kartları:",dealer_hand,"Toplam:",calculate_score(dealer_hand))
    else:
        print("Krupiyerin görünen kartı:",dealer_hand[0])

def blackjack():
    print("===Blackjack oyununa hosgeldınız!===")
    player=[draw_card(),draw_card()]
    dealer=[draw_card(),draw_card()]

    while True:
        print_hands(player,dealer)
        if calculate_score(player)==21:
            print("21 yaptın! kazandın!")
            return
        elif calculate_score(player)>21:
            print("Fazla cektin! Yandın!")
            return
        secim=input("Kart çekmek ister misin?(y/n):").lower()
        if secim=="y":
            player.append(draw_card())
        elif secim=="n":
            break
        else:
            print("Gecersiz secim.")
    print_hands(player,dealer,show_dealer=True)

    while calculate_score(dealer)<17:
        dealer.append(draw_card())
        print("Krupiye kart cekti.....")
    oyuncu=calculate_score(player)
    krupiye=calculate_score(dealer)
    print("\n Sonuclar:")
    print_hands(player,dealer,show_dealer=True)

    if krupiye>21:
        print("Krupiye yandı Kazandın")
    elif oyuncu>krupiye:
        print("Tebrikler sen kazandın")
    elif oyuncu==krupiye:
        print("berabere")
    else:
        print("Krupiye kazandı!")
try:
    blackjack()
except Exception as e:
    print("Bir hata oluştu:",e)
        

    