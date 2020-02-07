# -*- coding: utf-8 -*-
from dataclasses import dataclass, field, asdict, astuple, make_dataclass
from typing import List


@dataclass
class User:
    name: str = ""
    agree: bool = True
    tag: List[str] = field(default_factory=list)


if __name__ == '__main__':

    p = User("Kim", True)

    assert asdict(p) == {'name': "Kim", 'agree': True, 'tag':[]}
    assert type(p) == User
    assert type(asdict(p)) == dict

    Article = make_dataclass('article',
                             [('title', str),
                              ('text', str),
                              ('index', int, field(default=5))])

    a = Article("title", "text", 1)
    assert type(a) == Article
    assert type(asdict(a)) == dict
    assert type(astuple(a)) == tuple

