import inspect
import sys
import warnings
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

import tomli

warnings.formatwarning = lambda msg, *args, **kwargs: f'\033[93mWARNING ---> {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}:\033[0m {msg}'


# PATHS
class ProjectPathsDict(dict):
    APP_PATH = 'APPPATH'
    DIST_PATH = 'DISTPATH'
    CONFIG_PATH = 'CONFIGPATH'
    CONFIG_FILE_PATH = 'CONFIGFILEPATH'
    
    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError:
            return None

    def __setitem__(self, key, value) -> None:
        if Path(value).exists():
            return super().__setitem__(key, Path(value))
        warnings.warn(f'{value} is not a valid path\n')
        return super().__setitem__(key, None)

    def setAppPath(self, newAppPath: str) -> None:
        self[self.APP_PATH] = Path(newAppPath).resolve()
        self[self.DIST_PATH] = self[self.APP_PATH] / 'dist'
        self[self.CONFIG_PATH] = self[self.APP_PATH] / 'dist' / 'config'
        self[self.CONFIG_FILE_PATH] = self[self.APP_PATH] / 'dist' / 'config' / 'config.toml'

ppaths = ProjectPathsDict()
if getattr(sys, 'frozen', False):
    ppaths.setAppPath(Path(sys.executable).parents[1])  #CHECK
    #ppaths.setAppPath(path.abspath(path.join(path.dirname(sys.executable),'..')))
elif __file__:
    ppaths.setAppPath(Path(inspect.stack()[-1].filename).parents[1])  #CHECK


# CONFIG
class ConfigDict(dict):
    def __init__(self,
                 *args,
                 route: Optional[list] = None,
                 filePath: Optional[Path] = None,
                 **kwargs) -> None:
        self._route: Optional[list] = route
        self._filePath: Optional[Path] = filePath
        super().__init__(*args, **kwargs)

    def __getattr__(self, name: str) -> Any:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            try:
                result: Any = self[str(name)]
            except KeyError:
                raise AttributeError(f'"{name}" not found in the route {self._route} of file "{self._filePath}"')
            if isinstance(result, dict):
                newRoute: list | None = self._route
                try:
                    newRoute.append(str(name))
                except AttributeError:
                    newRoute = [str(name)]
                return ConfigDict(result,
                                  route= newRoute,
                                  file_path= self._filePath)
            return result


class ConfigFileManager:
    def __init__(self, filePath: str | Path) -> None:
        pathFile: Path = Path(filePath).with_suffix('.toml')
        if pathFile.is_file():
            self._filePath: Path = pathFile.resolve()
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
                                    filePath= self._filePath,)
            return result


if ppaths[ProjectPathsDict.CONFIG_FILE_PATH] is not None:
    with open(ppaths[ProjectPathsDict.CONFIG_FILE_PATH], 'a'):
        ...
    cfg = ConfigFileManager(ppaths[ProjectPathsDict.CONFIG_FILE_PATH])
else:
    warnings.warn(f'There is no default config file\n')
    cfg = None
