from typing import Protocol

from abc import abstractmethod
from dataclasses import dataclass

from dishka import Provider, provide, Scope, make_async_container, make_container

@dataclass
class Connection:
    uri: str


class DataGateway(Protocol):
    @abstractmethod
    def hello_world(self) -> str: ...



class DataGatewayInpl(DataGateway):
    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def hello_world(self):
        return f'Hello from DataGatewayInpl: {self.connection.uri}'


class Service:
    def __init__(self, data_gatewat:DataGateway)-> None:
        self.data_gatewat = data_gatewat


    def say(self) -> str:
        return self.data_gatewat.hello_world()


class DataGatewayProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_connection(self) -> Connection:
        return Connection('postgresql://localhost:5432/test_db')

    data_gateway_impl = provide(DataGatewayInpl, scope=Scope.REQUEST, provides=DataGateway)


class ServiceProvider(Provider):
    scope = Scope.REQUEST
    service = provide(Service)


container = make_container(DataGatewayProvider(), ServiceProvider())

with container() as request_container:
    service = request_container.get(Service)
    print(service.say())