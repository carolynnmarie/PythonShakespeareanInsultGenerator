import random


class ShakespeareanInsultsGenerator:
    def __init__(self):
        self.insults = ["mountain of mad flesh", "light of brain", "bolting-hutch of beastliness",
                        "not so much brain as ear wax", "long-tongued gossip", "thou art a boil, a plague sore",
                        "you rampallian! You fustilarian!", "Veriest varlet that ever chewed with a tooth",
                        "I do desire we may be better strangers", "all eyes and no sight",
                        "all the infections that the sun sucks up", "elvish-marked abortive, rooting hog",
                        "highly fed and lowly taught", "infinite and endless liar, an hourly promise-breaker",
                        "clod of wayward marl", "o gull, o dolt, as ignorant as dirt", "roast-meat for worms",
                        "false of heart, light of ear, bloody of hand", "anointed sovereign of sighs and groans",
                        "the soul of this man is his clothes", "quintessence of dust", "canker-blossom",
                        "poisonous bunch-backed toad", "a fusty nut with no kernel", "lewdly inclined",
                        "beetle-headed, flap-eared knave"]

    def randominsult(self):
        x = input("Welcome to the Shakespearean Insult Generator! Press any letter key to get insulted")
        if x.isalpha():
            rinsult = random.randrange(0, 26)
            print(self.insults[rinsult])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
