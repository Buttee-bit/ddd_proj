from dishka import Provider, provide, Scope, make_async_container, make_container
from setings.setting import ParserTgSettings


class ConfigTgAppProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_tg_settings(self) -> ParserTgSettings:
        return ParserTgSettings()


container = make_container(ConfigTgAppProvider())

with container() as request_container:
    tg_settings = request_container.get(ParserTgSettings)
