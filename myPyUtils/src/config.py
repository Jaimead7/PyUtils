import inspect
import sys
import warnings
from datetime import datetime
from os import path
from pathlib import Path
from typing import Any, Optional

import tomli

warnings.formatwarning = lambda msg, *args, **kwargs: str(msg)

# PATHS
class ProjectPathsDict(dict):
    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError:
            return None

    def __setitem__(self, key, value) -> None:
        if path.exists(value):
            return super().__setitem__(key, value)
        warnings.formatwarning = lambda msg, *args, **kwargs: str(msg)
        warnings.warn(f'\033[93mWARNING ---> {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}:\033[0m {value} is not a valid path\n')
        return super().__setitem__(key, None)

    def setAppPath(self, newAppPath: str) -> None:
        self['APPLICATIONPATH'] = newAppPath
        self['DISTPATH'] = path.join(self['APPLICATIONPATH'], 'dist')
        self['CONFIGPATH'] = path.join(self['APPLICATIONPATH'], 'dist', 'config')
        self['CONFIGFILEPATH'] = path.join(self['APPLICATIONPATH'], 'dist', 'config', 'config.toml')

ppaths = ProjectPathsDict()
if getattr(sys, 'frozen', False):
    ppaths.setAppPath(path.abspath(path.join(path.dirname(sys.executable),'..')))
elif __file__:
    ppaths.setAppPath(path.abspath(str(Path(inspect.stack()[-1].filename).parents[1])))

# CONFIG
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
        filePath = str(filePath)
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


if ppaths['CONFIGPATH'] is not None:
    with open(ppaths['CONFIGFILEPATH'], 'a'):
        ...
    cfg = ConfigFileManager(ppaths['CONFIGFILEPATH'])
else:
    warnings.formatwarning = lambda msg, *args, **kwargs: str(msg)
    warnings.warn(f'\033[93mWARNING ---> {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}:\033[0m There is no default config file\n')
    cfg = None
