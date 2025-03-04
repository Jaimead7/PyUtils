from pathlib import Path

from pytest import fixture, warns

from ..src.config import *


def getCfgContent() -> str:
    return '[app]\n\tname = "MyPyUtils"\n\tloggingLevel = "Debug"\n\t[app.author]\n\t\tname = "Jaimead7"\n\t\turl = "https://github.com/Jaimead7"'

@fixture(autouse= True)
def configureTestFolder(tmp_path: Path) -> None:
    dist: Path = tmp_path / 'dist'
    dist.mkdir()
    config: Path = tmp_path / 'dist' / 'config'
    config.mkdir()
    configFile: Path = tmp_path / 'dist' / 'config' / 'config.toml'
    configFile.write_text(getCfgContent())

@fixture
def prjTestDict(tmp_path: Path) -> ProjectPathsDict:
    prjTestDict = ProjectPathsDict()
    prjTestDict.setAppPath(tmp_path)
    return prjTestDict

@fixture
def cfgManager(prjTestDict: ProjectPathsDict) -> ConfigFileManager:
    return ConfigFileManager(prjTestDict[ProjectPathsDict.CONFIG_FILE_PATH])


class TestProjectPaths:
    def test_defaultPaths(self, prjTestDict: ProjectPathsDict, tmp_path: Path) -> None:
        assert prjTestDict[ProjectPathsDict.APP_PATH] == tmp_path
        assert prjTestDict[ProjectPathsDict.DIST_PATH] == tmp_path / 'dist'
        assert prjTestDict[ProjectPathsDict.CONFIG_PATH] == tmp_path / 'dist' / 'config'
        assert prjTestDict[ProjectPathsDict.CONFIG_FILE_PATH] == tmp_path / 'dist' / 'config' / 'config.toml'

    def test_errors(self, prjTestDict: ProjectPathsDict) -> None:
        with warns(UserWarning):
            prjTestDict['ERROR_PATH'] = 'noPath'
        assert prjTestDict['ERROR_PATH'] == None


class TestConfigFileManager:
    def test_access(self, cfgManager: ConfigFileManager) -> None:
        assert cfgManager.app.name == 'MyPyUtils'
        assert type(cfgManager.app.author) == ConfigDict
        assert cfgManager.app.author == {'name': 'Jaimead7', 'url': 'https://github.com/Jaimead7'}
        assert cfgManager.app.author.name == 'Jaimead7'

    def test_routes(self, cfgManager: ConfigFileManager) -> None:
        assert cfgManager.app.author.route == ['app', 'author']

    def test_filePath(self, cfgManager: ConfigFileManager, prjTestDict: ProjectPathsDict) -> None:
        assert cfgManager.app.author.filePath == prjTestDict[ProjectPathsDict.CONFIG_FILE_PATH]
