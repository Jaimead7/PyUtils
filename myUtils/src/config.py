import sys
from os import makedirs, path
from pathlib import Path
from typing import Any, Optional

import tomli

if getattr(sys, 'frozen', False):
    APPLICATIONPATH: str = path.abspath(path.join(path.dirname(sys.executable),'..'))
elif __file__:
    testPath: str = path.abspath(str(Path(__file__).parents[3]))
    if testPath[10:] == 'submodules':
        APPLICATIONPATH = path.abspath(str(Path(__file__).parents[5]))
    else:
        APPLICATIONPATH = path.abspath(str(Path(__file__).parents[2]))
DISTPATH: str = path.join(APPLICATIONPATH, 'dist')
CONFIGPATH: str = path.join(DISTPATH, 'config')


class ConfigDict(dict):
    def __init__(self,
                 *args,
                 route: Optional[list] = None,
                 filePath: Optional[str] = None,
                 **kwargs) -> None:
        self._route: Optional[list] = route
        self._filePath: Optional[str] = filePath
        super().__init__(*args, **kwargs)

    def __getattr__(self, name: str) -> Any:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            try:
                result: Any = self[str(name)]
            except KeyError:
                raise AttributeError(f'"{name}" not found in the route {self._route}')
            if isinstance(result, dict):
                newRoute: list | None = self._route
                try:
                    newRoute.append(str(name))
                except AttributeError:
                    newRoute = [str(name)]
                return ConfigDict(result,
                                  route= newRoute,
                                  filePath= self._filePath)
            return result


class ConfigFileManager:
    def __init__(self, filePath: str) -> None:
        if filePath[-5:] != '.toml':
            filePath += '.toml'
        if path.isfile(filePath):
            self._filePath: str = filePath
        else:
            raise FileExistsError(f'{filePath} is not a config file')

    @property
    def _data(self) -> dict:
        try:
            with open(self._filePath, 'rb') as f:
                data: dict = tomli.load(f)
        except tomli.TOMLDecodeError:
            raise tomli.TOMLDecodeError(f'{self._filePath} is not a valid .toml file')
        return data

    def __str__(self) -> str:
        return str(self._data)

    def __getattr__(self, name: str) -> Any:
        try:
            return self.__dict__[str(name)]
        except KeyError:
            result: Any = self._data[str(name)]
            if isinstance(result, dict):
                result = ConfigDict(result,
                                    route= [str(name)],
                                    filePath= self._filePath)
            return result


cfg = ConfigFileManager(path.join(CONFIGPATH, 'config.toml'))
