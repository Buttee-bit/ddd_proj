from functools import lru_cache
from punq import Container, Scope
from backend.aplications.parser_tg.setings.setting import ParserTgSettings


@lru_cache(1)
def init_container() -> Container:
    return _init_container()

def  _init_container() -> Container:
    container = Container()
    container.register(ParserTgSettings, instance=ParserTgSettings(), scope=Scope.singleton)
    parserTgSettings = container.resolve(ParserTgSettings)

    return container