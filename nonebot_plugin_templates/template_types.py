from typing import List

"""Card Template"""


class Tag:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __add__(self, other):
        if isinstance(other, Tag):
            return Tags([self, other])
        elif isinstance(other, Tags):
            return other + self


class Tags:

    def __init__(self, tags):
        """tags 可以为Tag,Tags,[Tag]"""
        self.tags: List[Tag] = None
        if isinstance(tags, Tags):
            self.tags = tags.tags
        if isinstance(tags, Tag):
            self.tags = [tags]
        if isinstance(tags, List):
            self.tags = tags

    def add(self, tag):
        self.tags.append(tag)

    def __iter__(self):
        return iter(self.tags)

    def __add__(self, other):
        if isinstance(other, Tag):
            return self + Tags([other])
        elif isinstance(other, Tags):
            return Tags(self.tags + other.tags)


# Line class
class Line:

    def __init__(self, main, title=None):
        self.main = main
        self.title = title

    def __add__(self, other):
        if isinstance(other, Line):
            return Content([self, other])
        elif isinstance(other, Content):
            return other + self


class Content:

    def __init__(self, lines=None):
        """lines 可以为Line,Content,[Line]"""
        self.lines: List[Line]
        if isinstance(lines, Line):
            self.lines = [lines]
        elif isinstance(lines, Content):
            self.lines = lines.lines
        else:
            self.lines = lines

    def add(self, line):
        self.lines.append(line)

    def __iter__(self):
        return iter(self.lines)

    def __add__(self, other):
        if isinstance(other, Line):
            return Content(self.lines + [other])
        elif isinstance(other, Content):
            return Content(self.lines + other.lines)


# Card class
class Card:

    def __init__(self, name, content, tags=None):
        self.name = name
        self.content = content
        self.tags = tags

    def __add__(self, other):
        if isinstance(other, Card):
            return Cards([self, other])
        if isinstance(other, Cards):
            return Cards(other.cards + [self])


# Cards class
class Cards:
    def __init__(self, cards=None):
        """cards 可以为Card,Cards,[Card]"""
        self.cards: List[Card]
        if isinstance(cards, Cards):
            self.cards = cards.cards
        elif isinstance(cards, List):
            self.cards = cards
        elif isinstance(cards, Card):
            self.cards = [cards]

    def add(self, card):
        self.cards.append(card)

    def __iter__(self):
        return iter(self.cards)

    def __add__(self, other):
        if isinstance(other, Cards):
            return Cards(self.cards + other.cards)
        if isinstance(other, Card):
            return Cards(self.cards + [other])

    def to_dict(self):
        data = {}
        for card in self.cards:
            card_dict = {}
            if card.tags is not None:
                if card.tags.tags:
                    card_dict["tags"] = {tag.name: tag.color for tag in card.tags.tags}

            card_dict["content"] = {}
            for i, line in enumerate(card.content.lines):
                line_dict = {"main": line.main}
                if line.title:
                    line_dict["title"] = line.title
                card_dict["content"][f"line{i + 1}"] = line_dict

            data[card.name] = card_dict

        return data


"""Menu Template"""


class Func:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __add__(self, other):
        if isinstance(other, Func):
            return Funcs([self, other])
        if isinstance(other, Funcs):
            return Funcs(other.funcs + [self])


class Funcs:
    def __init__(self, funcs):
        """funcs 可以为Func,Funcs,[Func]"""
        self.funcs: List[Func]
        if isinstance(funcs, Func):
            self.funcs = [funcs]
        elif isinstance(funcs, Funcs):
            self.funcs = funcs.funcs
        else:
            self.funcs = funcs

    def __iter__(self):
        return iter(self.funcs)

    def __add__(self, other):
        if isinstance(other, Func):
            return Funcs(self.funcs + [other])
        elif isinstance(other, Funcs):
            return Funcs(self.funcs + other.funcs)


class Menu:
    def __init__(self, name, funcs, des=None):
        self.name = name
        self.des = des
        self.funcs = funcs

    def __add__(self, other):
        if isinstance(other, Menu):
            return Menus([self, other])
        if isinstance(other, Menus):
            return Menus(other.menus + [self])


class Menus:
    def __init__(self, menus=None):
        """menus 可以为Menu,Menus,[Menu]"""
        self.menus: List[Menu]
        if menus is None:
            self.menus = []
        elif isinstance(menus, Menu):
            self.menus = [menus]
        elif isinstance(menus, Menus):
            self.menus = menus.menus
        else:
            self.menus = menus

    def __add__(self, other):
        if isinstance(other, Menu):
            return Menus(self.menus + [other])
        elif isinstance(other, Menus):
            return Menus(self.menus + other.menus)

    def to_dict(self):
        d = {}
        for menu in self.menus:
            if menu.des:
                d[menu.name] = {"des": menu.des, "funcs": {f.name: f.desc for f in menu.funcs}}
            else:
                d[menu.name] = {"funcs": {f.name: f.desc for f in menu.funcs}}
        return d
