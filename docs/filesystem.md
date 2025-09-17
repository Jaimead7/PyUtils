# TODO


## Example
```python
from pyUtils import *


class DataYamlFile(YamlFileValidator):
    NAME_PATTERN = r'^data.yaml$'


class MetadataYamlFile(YamlFileValidator):
    NAME_PATTERN = r'^metadata.yaml$'


class ImageDir(MyDirValidator):
    NAME_PATTERN = r'^images$'
    ALLOWED_FILES: list[type[MyFileValidator]] = [
        ImageFileValidator
    ]


class LabelsDir(MyDirValidator):
    NAME_PATTERN = r'^labels$'
    ALLOWED_FILES: list[type[MyFileValidator]] = [
        TxtFileValidator
    ]


class TestDir(MyDirValidator):
    NAME_PATTERN = r'^test$'
    REQUIRED_DIRS: list[type[MyDirValidator]] = [
        ImageDir,
        LabelsDir
    ]


class TrainDir(MyDirValidator):
    NAME_PATTERN = r'^train$'
    REQUIRED_DIRS: list[type[MyDirValidator]] = [
        ImageDir,
        LabelsDir
    ]


class ValidationDir(MyDirValidator):
    NAME_PATTERN = r'^validation$'
    REQUIRED_DIRS: list[type[MyDirValidator]] = [
        ImageDir,
        LabelsDir
    ]


class TrainingDir(MyDirValidator):
    REQUIRED_FILES: list[type[MyFileValidator]] = [
        DataYamlFile
    ]
    ALLOWED_FILES: list[type[MyFileValidator]] = [
        TomlFileValidator
    ]
    REQUIRED_DIRS: list[type[MyDirValidator]] = [
        TestDir,
        TrainDir,
        ValidationDir
    ]
TrainingDir.add_required_file(MetadataYamlFile)

dir = TrainingDir('/tmp/test')

dir.validate()
```