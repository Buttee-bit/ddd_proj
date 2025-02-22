from dishka import Provider, provide, Scope, make_async_container, make_container
from telethon import TelegramClient
from backend.aplications.parser_tg.setings.setting import ParserTgSettings


class ConfigTgAppProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_tg_settings(self) -> ParserTgSettings:
        return ParserTgSettings()

    @provide(scope=Scope.APP)
    def init_tg_client(self) -> TelegramClient:
        return TelegramClient(
            session=self.get_tg_settings().session_file,
            api_id=self.get_tg_settings().tg_api_id,
            api_hash=self.get_tg_settings().tg_api_hash,
        )


container = make_async_container(ConfigTgAppProvider())

# with container() as request_container:
#     tg_settings = request_container.get(ParserTgSettings)
#     tg_client = request_container.get(TelegramClient)
#     # print(tg_settings.session_file)
#     print(tg_client)
