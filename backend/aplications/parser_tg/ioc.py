from functools import lru_cache
from punq import Container, Scope
from telethon import TelegramClient
from backend.aplications.parser_tg.setings.setting import Settings
from backend.aplications.parser_tg.application.services.tg import TgParsServices


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()
    container.register(
        Settings, instance=Settings(), scope=Scope.singleton
    )
    parserTgSettings: Settings = container.resolve(Settings)

    def _init_TgServices() -> TgParsServices:
        return TgParsServices(
            tg_client=TelegramClient(
                parserTgSettings.session_file,
                parserTgSettings.tg_api_id,
                parserTgSettings.tg_api_hash,
            ),
            watcher_groups=[
                "https://t.me/Ukr_G_M",
                "https://t.me/boris_rozhin",
                "https://t.me/infantmilitario",
                "https://t.me/test_v123123",
                "https://t.me/poisk_mil",
                "https://t.me/Belarus_VPO",
                "https://t.me/joker_ukr",
                "https://t.me/truexanewsua",
                "https://t.me/vert_i_call",
                "https://t.me/pandoras_box_ua",
                "https://t.me/ragnarockkyiv",
                "https://t.me/oko18_channel",
                "https://t.me/okoo_ua",
                "https://t.me/insiderUKR",
                "https://t.me/kpszsu",
                "https://t.me/kievreal1",
                "https://t.me/monitor_ukr",
                "https://t.me/voynareal",
                "https://t.me/vanek_nikolaev",
                "https://t.me/lost_warinua",
                "https://t.me/war_monitor",
                "https://t.me/DeepStateUA",
                "https://t.me/cgt_analitics",
                "https://t.me/ukrnastup",
                "https://t.me/novinach",
                "https://t.me/lachentyt",
            ],
            # message_handler=lambda x: None
        )

    container.register(TgParsServices, factory=_init_TgServices, scope=Scope.singleton)

    return container
