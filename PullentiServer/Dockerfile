FROM mcr.microsoft.com/dotnet/runtime:2.1

ENTRYPOINT ["dotnet", "Pullenti.Server.dll", "-noterminal", "false"]

COPY ./PullentiServer/Pullenti.Server.runtimeconfig.json /app/
COPY ./PullentiServer/Pullenti.Server.dll /app/

WORKDIR /app
