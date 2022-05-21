# Possible values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K (4 of each)
# Possible suits: C, D, H, S

from itertools import islice
from itertools import chain
from itertools import combinations
import json

class Crib:
    def __init__(self, c1, c2, c3, c4):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4

    def big_func(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        c4 = self.c4

        card_num_vals = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        }

        hand = [c1, c2, c3, c4]

        C = 0
        D = 0
        H = 0
        S = 0

        for i in range(4):
            if(hand[i].suit == "C"):
                C += 1
            if(hand[i].suit == "D"):
                D += 1
            if(hand[i].suit == "H"):
                H += 1
            if(hand[i].suit == "S"):
                S += 1

        suits = [C, D, H, S]
        suits_names = ["C", "D", "H", "S"]

        suits_sum = 0

        print("\n")

        for i in range(4):
            if(suits[i] == 4):
                suits_sum += 4
                print(suits_names[i] + " is a four card flush")
            if(suits[i] == 5):
                suits_sum += 5
                print(suits_names[i] + " is a five card flush")

        print("suits sum is: " + str(suits_sum) + "\n")

        As = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0
        sevens = 0
        eights = 0
        nines = 0
        tens = 0
        Js = 0
        Qs = 0
        Ks = 0

        for i in range(4):
            if(hand[i].value == "A"):
                As += 1
            if(hand[i].value == "2"):
                twos += 1
            if(hand[i].value == "3"):
                threes += 1
            if(hand[i].value == "4"):
                fours += 1
            if(hand[i].value == "5"):
                fives += 1
            if(hand[i].value == "6"):
                sixes += 1
            if(hand[i].value == "7"):
                sevens += 1
            if(hand[i].value == "8"):
                eights += 1
            if(hand[i].value == "9"):
                nines += 1
            if(hand[i].value == "10"):
                tens += 1
            if(hand[i].value == "J"):
                Js += 1
            if(hand[i].value == "Q"):
                Qs += 1
            if(hand[i].value == "K"):
                Ks += 1

        values = [As, twos, threes, fours, fives, sixes, sevens, eights, nines, tens, Js, Qs, Ks]
        values_names = ["As", "twos", "threes", "fours", "fives", "sixes", "sevens", "eights", "nines", "tens", "Js", "Qs", "Ks"]

        values_sum = 0

        for i in range(13):
            if(values[i] == 2):
                values_sum += 2
                print(values_names[i] + " is a pair.")
            if(values[i] == 3):
                values_sum += 6
                print(values_names[i] + " is a pair royal")
            if(values[i] == 4):
                values_sum += 12
                print(values_names[i] + "is a double pair royal")

        print("values sum is: " + str(values_sum))

        def powerset(iterable):
            "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

        fifteen_dict = {
        }

        newnew = powerset([card_num_vals[c1.value], card_num_vals[c2.value], card_num_vals[c3.value], card_num_vals[c4.value]])
        newnew2 = powerset(["c1","c2","c3","c4"])
        for i in range(2**4):
            fifteen_dict[next(newnew2)] = sum(list(next(newnew)))

        fifteen_sum = 0

        print("\n")
        for x in fifteen_dict:
            if fifteen_dict[x] == 15:
                for i in range(len(list(x))):
                    print(locals()[list(x)[i]].value + " of " + locals()[list(x)[i]].suit)
                print(" is 15\n")
                fifteen_sum += 2

        print("fifteen sum is: " + str(fifteen_sum))

        run_sum = 0
        run_dict = {
        }

        card_num_run_vals = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        }

        newnew = powerset([card_num_run_vals[c1.value], card_num_run_vals[c2.value], card_num_run_vals[c3.value], card_num_run_vals[c4.value]])
        newnew2 = powerset(["c1","c2","c3","c4"])
        for i in range(2**4):
            new = list(next(newnew))
            run_dict[next(newnew2)] = sorted(new)

        print("\n")
        list_of_lists = []
        for x in run_dict:
            if len(run_dict[x]) > 2:
                if run_dict[x] == list(range(min(run_dict[x]), max(run_dict[x])+1)):
                    new_list = []
                    for i in range(len(list(x))):
                        #print(locals()[list(x)[i]].value + " of " + locals()[list(x)[i]].suit)
                        new_list.append(locals()[list(x)[i]])
                    #print(" is a run\n")
                    list_of_lists.append(new_list)
                    #run_sum += len(run_dict[x])
        
        newernewerlist = []
        list_of_lists.sort(key=len)
        for i in range(len(list_of_lists)):
            flag = 0
            for j in range(len(list_of_lists)):
                if i != j:
                    if(all(x in list_of_lists[j] for x in list_of_lists[i])):
                        flag = 1
            if flag == 0:
                newernewerlist.append(list_of_lists[i])
                
        for i in range(len(newernewerlist)):
            for j in range(len(newernewerlist[i])):
                print(newernewerlist[i][j].value + " of " + newernewerlist[i][j].suit)
            print(" is a run\n")
            run_sum += len(newernewerlist[i])

        print("run sum is " + str(run_sum))
        total_sum = suits_sum + values_sum + fifteen_sum + run_sum
        print("total sum is: " + str(total_sum))
        return total_sum

cards_points_dict = {}

def other_func(c1, c2, c3, c4, c5, c6):

    total_hand = [c1, c2, c3, c4, c5, c6]

    cards_list = []

    for i in range(15):
        print("\n\n\nTHIS DECK IS: " + str(list(combinations(total_hand, 4))[i][0].value) + " of " + str(list(combinations(total_hand, 4))[i][0].suit) + " and " + str(list(combinations(total_hand, 4))[i][1].value) + " of " + str(list(combinations(total_hand, 4))[i][1].suit) + " and " + str(list(combinations(total_hand, 4))[i][2].value) + " of " + str(list(combinations(total_hand, 4))[i][2].suit) + " and " + str(list(combinations(total_hand, 4))[i][3].value) + " of " + str(list(combinations(total_hand, 4))[i][3].suit))
        newcrib = Crib(list(combinations(total_hand, 4))[i][0], list(combinations(total_hand, 4))[i][1], list(combinations(total_hand, 4))[i][2], list(combinations(total_hand, 4))[i][3])
        cards_list.append(str(list(combinations(total_hand, 4))[i][0].value) + " of " + str(list(combinations(total_hand, 4))[i][0].suit) + " and " + str(list(combinations(total_hand, 4))[i][1].value) + " of " + str(list(combinations(total_hand, 4))[i][1].suit) + " and " + str(list(combinations(total_hand, 4))[i][2].value) + " of " + str(list(combinations(total_hand, 4))[i][2].suit) + " and " + str(list(combinations(total_hand, 4))[i][3].value) + " of " + str(list(combinations(total_hand, 4))[i][3].suit))
        cards_points_dict[str(list(combinations(total_hand, 4))[i][0].value) + " of " + str(list(combinations(total_hand, 4))[i][0].suit) + " and " + str(list(combinations(total_hand, 4))[i][1].value) + " of " + str(list(combinations(total_hand, 4))[i][1].suit) + " and " + str(list(combinations(total_hand, 4))[i][2].value) + " of " + str(list(combinations(total_hand, 4))[i][2].suit) + " and " + str(list(combinations(total_hand, 4))[i][3].value) + " of " + str(list(combinations(total_hand, 4))[i][3].suit)] = newcrib.big_func()

    pretty = json.dumps(dict(sorted(cards_points_dict.items(), key=lambda item: item[1], reverse = True)), indent = 4)

    print(pretty)

    print("\n\nThe suggested play is to keep: " + str(list(dict(sorted(cards_points_dict.items(), key=lambda item: item[1], reverse = True)).keys())[0]))

#Later could add probabilities using known cards,
#for example there are 16 cards worth "10" with only
#4 cards worth every other value, so out of 52 cards
#there is a 16/52 chance that the starter card
#is worth 10 points

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

firstvalue = input("First card value: ")
firstsuit = input("First card suit: ")
secondvalue = input("Second card value: ")
secondsuit = input("Second card suit: ")
thirdvalue = input("Third card value: ")
thirdsuit = input("Third card suit: ")
fourthvalue = input("Fourth card value: ")
fourthsuit = input("Fourth card suit: ")
fifthvalue = input("Fifth card value: ")
fifthsuit = input("Fifth card suit: ")
sixthvalue = input("Sixth card value: ")
sixthsuit = input("Sixth card suit: ")

c1 = Card(firstvalue, firstsuit)
c2 = Card(secondvalue, secondsuit)
c3 = Card(thirdvalue, thirdsuit)
c4 = Card(fourthvalue, fourthsuit)
c5 = Card(fifthvalue, fifthsuit)
c6 = Card(sixthvalue, sixthsuit)

new = other_func(c1,c2,c3,c4,c5,c6)

print("\n\nNow commencing play portion of game. Flip over a starter card.\n")

print("Do not play a 5 if you are starting! There's a 16/52 chance that a card has a value of 10 versus a 4/52 chance that it has any other value!\n")

def big_func(c1,c2,c3,c4):
    card_num_vals = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    }
    card_num_run_vals = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    }
    sum = 0
    hand = [c1,c2,c3,c4]
    previous_suits = []
    previous_run_values = []
    previous_values = []
    truth = True
    while truth is True:
        if(len(previous_values) > 2):
            print(sorted(list(islice(reversed(previous_values), 0, 3))))
        if(len(previous_values) > 3):
            print(sorted(list(islice(reversed(previous_values), 0, 4))))
        if(len(previous_values) > 4):
            print(sorted(list(islice(reversed(previous_values), 0, 5))))
        if(len(previous_values) > 5):
            print(sorted(list(islice(reversed(previous_values), 0, 6))))
        if(len(previous_values) > 6):
            print(sorted(list(islice(reversed(previous_values), 0, 7))))
        sum_of_over = 0
        for k in range(len(hand)):
            if(sum + card_num_vals[hand[k].value] == 15):
                print(str(hand[k].value) + " of " + str(hand[k].suit) + " goes to 15!\n")
            if(sum + card_num_vals[hand[k].value] == 31):
                print(str(hand[k].value) + " of " + str(hand[k].suit) + " goes to 31!\n")
            if(len(previous_values) > 0 and previous_values[-1] == hand[k].value):
                print(str(hand[k].value) + " of " + str(hand[k].suit) + " is a pair!\n")
            if(sum + card_num_vals[hand[k].value] > 31):
                sum_of_over += 1
        if sum_of_over == len(hand):
            print("\nGo!\n")
            value = input("Reset?: ")
            if value == "Yes":
                sum = 0
            value = input("Is round over?: ")
            if value == "Yes":
                truth = False
        if sum_of_over != len(hand):
            for i in range(len(hand)):
                print(str(i) + ") " + str(hand[i].value) + " of " + str(hand[i].suit) + "\n")
            print(str(9) + ") " + "skip\n")
            value = input("Which do you wish to use?: ")
            if int(value) != 9:    
                sum += card_num_vals[hand[int(value)].value]
                previous_suits.append(hand[int(value)].suit)
                previous_run_values.append(int(card_num_run_vals[hand[int(value)].value]))
                previous_values.append(hand[int(value)].value)
                hand.pop(int(value))
            if sum == 15:
                print("\nRemember to get 2 points!\n")
            if sum == 31:
                print("\nRemember to get 2 points!\n")
                sum = 0
        print("\nThe current sum is: " + str(sum) + "\n")
        value = input("Did opponent say 'go'?: ")
        if value == "Yes":
            newvalue = input("Reset?: ")
            if newvalue == "Yes":
                sum = 0
                print("\nRemember to get 1 point!\n")
            newervalue = input("Is round over?: ")
            if newervalue == "Yes":
                truth = False
        if value == "No":
            value1 = input("\nWhat value did opponent use?: ")   
            previous_run_values.append(int(card_num_run_vals[value1]))
            previous_values.append(value1)
            sum += int(card_num_vals[value1])
            value = input("\nWhat suit did opponent use?: ") 
            previous_suits.append(value)
            if sum == 15:
                print("\Opponent gets 2 points!\n")
            if sum == 31:
                print("\Opponent get 2 points!\n")
                sum = 0
        print("\n The previous suits: " + str(previous_suits))
        print("\n The previous run values: " + str(previous_run_values))
        print("\n The previous card values: " + str(previous_values))
        print("\nThe current sum is: " + str(sum) + "\n")    

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

firstvalue = input("First card value: ")
firstsuit = input("First card suit: ")
secondvalue = input("Second card value: ")
secondsuit = input("Second card suit: ")
thirdvalue = input("Third card value: ")
thirdsuit = input("Third card suit: ")
fourthvalue = input("Fourth card value: ")
fourthsuit = input("Fourth card suit: ")

c1 = Card(firstvalue, firstsuit)
c2 = Card(secondvalue, secondsuit)
c3 = Card(thirdvalue, thirdsuit)
c4 = Card(fourthvalue, fourthsuit)

startervalue = input("Starter card value: ")
startersuit = input("Starter card suit: ") 
starter = Card(startervalue, startersuit)

big_func(c1,c2,c3,c4)

class Crib:
    def __init__(self, c1, c2, c3, c4, starter):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.starter = starter

    def big_func(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        c4 = self.c4
        starter = self.starter

        card_num_vals = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        }

        hand = [c1, c2, c3, c4, starter]

        C = 0
        D = 0
        H = 0
        S = 0

        for i in range(4):
            if(hand[i].suit == "C"):
                C += 1
            if(hand[i].suit == "D"):
                D += 1
            if(hand[i].suit == "H"):
                H += 1
            if(hand[i].suit == "S"):
                S += 1

        suits = [C, D, H, S]
        suits_names = ["C", "D", "H", "S"]

        suits_sum = 0

        print("\n")

        for i in range(4):
            if(suits[i] == 4 and starter.suit == suits_names[i]):
                suits_sum += 5
                print(suits_names[i] + " is a five card flush")
            elif(suits[i] == 4):
                suits_sum += 4
                print(suits_names[i] + " is a four card flush") 

        print("suits sum is: " + str(suits_sum) + "\n")

        As = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0
        sevens = 0
        eights = 0
        nines = 0
        tens = 0
        Js = 0
        Qs = 0
        Ks = 0

        for i in range(5):
            if(hand[i].value == "A"):
                As += 1
            if(hand[i].value == "2"):
                twos += 1
            if(hand[i].value == "3"):
                threes += 1
            if(hand[i].value == "4"):
                fours += 1
            if(hand[i].value == "5"):
                fives += 1
            if(hand[i].value == "6"):
                sixes += 1
            if(hand[i].value == "7"):
                sevens += 1
            if(hand[i].value == "8"):
                eights += 1
            if(hand[i].value == "9"):
                nines += 1
            if(hand[i].value == "10"):
                tens += 1
            if(hand[i].value == "J"):
                Js += 1
            if(hand[i].value == "Q"):
                Qs += 1
            if(hand[i].value == "K"):
                Ks += 1

        values = [As, twos, threes, fours, fives, sixes, sevens, eights, nines, tens, Js, Qs, Ks]
        values_names = ["As", "twos", "threes", "fours", "fives", "sixes", "sevens", "eights", "nines", "tens", "Js", "Qs", "Ks"]

        values_sum = 0

        for i in range(13):
            if(values[i] == 2):
                values_sum += 2
                print(values_names[i] + " is a pair.")
            if(values[i] == 3):
                values_sum += 6
                print(values_names[i] + " is a pair royal")
            if(values[i] == 4):
                values_sum += 12
                print(values_names[i] + " is a double pair royal")

        print("values sum is: " + str(values_sum))

        def powerset(iterable):
            "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

        fifteen_dict = {
        }

        newnew = powerset([card_num_vals[c1.value], card_num_vals[c2.value], card_num_vals[c3.value], card_num_vals[c4.value], card_num_vals[starter.value]])
        newnew2 = powerset(["c1","c2","c3","c4", "starter"])
        for i in range(2**5):
            fifteen_dict[next(newnew2)] = sum(list(next(newnew)))

        fifteen_sum = 0

        print("\n")
        for x in fifteen_dict:
            if fifteen_dict[x] == 15:
                for i in range(len(list(x))):
                    print(locals()[list(x)[i]].value + " of " + locals()[list(x)[i]].suit)
                print(" is 15\n")
                fifteen_sum += 2

        print("fifteen sum is: " + str(fifteen_sum))

        run_sum = 0
        run_dict = {
        }

        card_num_run_vals = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        }

        newnew = powerset([card_num_run_vals[c1.value], card_num_run_vals[c2.value], card_num_run_vals[c3.value], card_num_run_vals[c4.value], card_num_run_vals[starter.value]])
        newnew2 = powerset(["c1","c2","c3","c4", "starter"])
        for i in range(2**5):
            new = list(next(newnew))
            run_dict[next(newnew2)] = sorted(new)

        print("\n")
        list_of_lists = []
        for x in run_dict:
            if len(run_dict[x]) > 2:
                if run_dict[x] == list(range(min(run_dict[x]), max(run_dict[x])+1)):
                    new_list = []
                    for i in range(len(list(x))):
                        #print(locals()[list(x)[i]].value + " of " + locals()[list(x)[i]].suit)
                        new_list.append(locals()[list(x)[i]])
                    #print(" is a run\n")
                    list_of_lists.append(new_list)
                    #run_sum += len(run_dict[x])
        
        newernewerlist = []
        list_of_lists.sort(key=len)
        for i in range(len(list_of_lists)):
            flag = 0
            for j in range(len(list_of_lists)):
                if i != j:
                    if(all(x in list_of_lists[j] for x in list_of_lists[i])):
                        flag = 1
            if flag == 0:
                newernewerlist.append(list_of_lists[i])
                
        for i in range(len(newernewerlist)):
            for j in range(len(newernewerlist[i])):
                print(newernewerlist[i][j].value + " of " + newernewerlist[i][j].suit)
            print(" is a run\n")
            run_sum += len(newernewerlist[i])

        print("run sum is " + str(run_sum) + "\n")

        nobs_sum = 0
        for i in range(4):
            if hand[i].value == "J" and hand[i].suit == starter.suit:
                nobs_sum += 1

        print("nobs sum is: " + str(nobs_sum) + "\n")

        total_sum = suits_sum + values_sum + fifteen_sum + run_sum + nobs_sum
        print("total sum is: " + str(total_sum) + "\n")
        return total_sum

def other_func(c1, c2, c3, c4, starter):
    points_list = []
    newcrib = Crib(c1, c2, c3, c4, starter)
    points_list.append(newcrib.big_func())

#Later could add probabilities using known cards,
#for example there are 16 cards worth "10" with only
#4 cards worth every other value, so out of 52 cards
#there is a 16/52 chance that the starter card
#is worth 10 points

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

firstvalue = input("First card value: ")
firstsuit = input("First card suit: ")
secondvalue = input("Second card value: ")
secondsuit = input("Second card suit: ")
thirdvalue = input("Third card value: ")
thirdsuit = input("Third card suit: ")
fourthvalue = input("Fourth card value: ")
fourthsuit = input("Fourth card suit: ")
startervalue = input("Starter card value: ")
startersuit = input("Starter card suit: ")

c1 = Card(firstvalue, firstsuit)
c2 = Card(secondvalue, secondsuit)
c3 = Card(thirdvalue, thirdsuit)
c4 = Card(fourthvalue, fourthsuit)
starter = Card(startervalue, startersuit)

new = other_func(c1,c2,c3,c4,starter)

class Crib:
    def __init__(self, c1, c2, c3, c4, starter):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.starter = starter

    def big_func(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        c4 = self.c4
        starter = self.starter

        card_num_vals = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        }

        hand = [c1, c2, c3, c4, starter]

        C = 0
        D = 0
        H = 0
        S = 0

        for i in range(5):
            if(hand[i].suit == "C"):
                C += 1
            if(hand[i].suit == "D"):
                D += 1
            if(hand[i].suit == "H"):
                H += 1
            if(hand[i].suit == "S"):
                S += 1

        suits = [C, D, H, S]
        suits_names = ["C", "D", "H", "S"]

        suits_sum = 0

        print("\n")

        for i in range(4):
            if(suits[i] == 5):
                suits_sum += 5
                print(suits_names[i] + " is a five card flush")

        print("suits sum is: " + str(suits_sum) + "\n")

        As = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0
        sevens = 0
        eights = 0
        nines = 0
        tens = 0
        Js = 0
        Qs = 0
        Ks = 0

        for i in range(5):
            if(hand[i].value == "A"):
                As += 1
            if(hand[i].value == "2"):
                twos += 1
            if(hand[i].value == "3"):
                threes += 1
            if(hand[i].value == "4"):
                fours += 1
            if(hand[i].value == "5"):
                fives += 1
            if(hand[i].value == "6"):
                sixes += 1
            if(hand[i].value == "7"):
                sevens += 1
            if(hand[i].value == "8"):
                eights += 1
            if(hand[i].value == "9"):
                nines += 1
            if(hand[i].value == "10"):
                tens += 1
            if(hand[i].value == "J"):
                Js += 1
            if(hand[i].value == "Q"):
                Qs += 1
            if(hand[i].value == "K"):
                Ks += 1

        values = [As, twos, threes, fours, fives, sixes, sevens, eights, nines, tens, Js, Qs, Ks]
        values_names = ["As", "twos", "threes", "fours", "fives", "sixes", "sevens", "eights", "nines", "tens", "Js", "Qs", "Ks"]

        values_sum = 0

        for i in range(13):
            if(values[i] == 2):
                values_sum += 2
                print(values_names[i] + " is a pair.")
            if(values[i] == 3):
                values_sum += 6
                print(values_names[i] + " is a pair royal")
            if(values[i] == 4):
                values_sum += 12
                print(values_names[i] + " is a double pair royal")

        print("values sum is: " + str(values_sum))

        def powerset(iterable):
            "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

        fifteen_dict = {
        }

        newnew = powerset([card_num_vals[c1.value], card_num_vals[c2.value], card_num_vals[c3.value], card_num_vals[c4.value], card_num_vals[starter.value]])
        newnew2 = powerset(["c1","c2","c3","c4", "starter"])
        for i in range(2**5):
            fifteen_dict[next(newnew2)] = sum(list(next(newnew)))

        fifteen_sum = 0

        print("\n")
        for x in fifteen_dict:
            if fifteen_dict[x] == 15:
                for i in range(len(list(x))):
                    print(locals()[list(x)[i]].value + " of " + locals()[list(x)[i]].suit)
                print(" is 15\n")
                fifteen_sum += 2

        print("fifteen sum is: " + str(fifteen_sum))

        run_sum = 0
        run_dict = {
        }

        card_num_run_vals = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        }

        newnew = powerset([card_num_run_vals[c1.value], card_num_run_vals[c2.value], card_num_run_vals[c3.value], card_num_run_vals[c4.value], card_num_run_vals[starter.value]])
        newnew2 = powerset(["c1","c2","c3","c4", "starter"])
        for i in range(2**5):
            new = list(next(newnew))
            run_dict[next(newnew2)] = sorted(new)

        print("\n")
        list_of_lists = []
        for x in run_dict:
            if len(run_dict[x]) > 2:
                if run_dict[x] == list(range(min(run_dict[x]), max(run_dict[x])+1)):
                    new_list = []
                    for i in range(len(list(x))):
                        #print(locals()[list(x)[i]].value + " of " + locals()[list(x)[i]].suit)
                        new_list.append(locals()[list(x)[i]])
                    #print(" is a run\n")
                    list_of_lists.append(new_list)
                    #run_sum += len(run_dict[x])
        
        newernewerlist = []
        list_of_lists.sort(key=len)
        for i in range(len(list_of_lists)):
            flag = 0
            for j in range(len(list_of_lists)):
                if i != j:
                    if(all(x in list_of_lists[j] for x in list_of_lists[i])):
                        flag = 1
            if flag == 0:
                newernewerlist.append(list_of_lists[i])
                
        for i in range(len(newernewerlist)):
            for j in range(len(newernewerlist[i])):
                print(newernewerlist[i][j].value + " of " + newernewerlist[i][j].suit)
            print(" is a run\n")
            run_sum += len(newernewerlist[i])

        print("run sum is " + str(run_sum) + "\n")

        nobs_sum = 0
        for i in range(4):
            if hand[i].value == "J" and hand[i].suit == starter.suit:
                nobs_sum += 1

        print("nobs sum is: " + str(nobs_sum) + "\n")

        total_sum = suits_sum + values_sum + fifteen_sum + run_sum + nobs_sum
        print("total sum is: " + str(total_sum) + "\n")
        return total_sum

def other_func(c1, c2, c3, c4, starter):
    points_list = []
    newcrib = Crib(c1, c2, c3, c4, starter)
    points_list.append(newcrib.big_func())

#Later could add probabilities using known cards,
#for example there are 16 cards worth "10" with only
#4 cards worth every other value, so out of 52 cards
#there is a 16/52 chance that the starter card
#is worth 10 points

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

firstvalue = input("First card value: ")
firstsuit = input("First card suit: ")
secondvalue = input("Second card value: ")
secondsuit = input("Second card suit: ")
thirdvalue = input("Third card value: ")
thirdsuit = input("Third card suit: ")
fourthvalue = input("Fourth card value: ")
fourthsuit = input("Fourth card suit: ")
startervalue = input("Starter card value: ")
startersuit = input("Starter card suit: ")

c1 = Card(firstvalue, firstsuit)
c2 = Card(secondvalue, secondsuit)
c3 = Card(thirdvalue, thirdsuit)
c4 = Card(fourthvalue, fourthsuit)
starter = Card(startervalue, startersuit)

new = other_func(c1,c2,c3,c4,starter)