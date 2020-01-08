class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc


class Unicorn(GameObject):
    def __init__(self, name):
        self.class_name = "unicorn"
        self.health = 6
        self._desc = "A beautiful creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 6:
            return self._desc
        elif self.health == 5:
            health_line = "It has been hurt a little bit."
        elif self.health == 4:
            health_line = "Oh no, it's bleeding."
        elif self.health == 3:
            health_line = "Bleeding is getting worse."
        elif self.health == 2:
            health_line = "It's gonna die :(."
        elif self.health == 1:
            health_line = "Use \"heal\" or it's gonna die."
        elif self.health <= 0:
            health_line = "You killed a unicorn, why would you do that? Pls use \"revive\" to bring it back to life."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on it's knee."
        elif self.health == 1:
            health_line = "It's left arm has been cut off."
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin or Unicorn:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You killed the {}.".format(thing.class_name)
            else:
                msg = "You hit the {}.".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg


def revive(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if thing.health <= 0:
            thing.health = 2
            msg = "You revived the {}.".format(thing.class_name)
        elif thing.health > 0:
            msg = "{} is alive, use \"heal\" if you want to increase it's health.".format(
                thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg


def heal(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if thing.health <= 0:
            msg = "{} is dead, use \"revive\" if you want to bring it back to life.".format(
                thing.class_name)
        if thing.health >= 1:
            thing.health += 1
            msg = "You've increased {}'s health by +1".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here".format(noun)


def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))


def say(noun):
    return '"You said "{}"'.format(noun)


verb_dict = {
    "say": say,
    "examine": examine,
    "hit": hit,
    "heal": heal,
    "revive": revive,
}

goblin = Goblin("Nakaza")
unicorn = Unicorn("Jednorog")

while True:
    get_input()
