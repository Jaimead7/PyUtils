### Config file
#### ProjectPathsDict
Dict with validation for paths. On error ```path = None```.  
Default paths can be setted by a main ```APP_PATH```:  
- ```DIST_PATH``` is ```APP_PATH/dist```  
- ```CONFIG_PATH``` is ```APP_PATH/dist/config```  
- ```CONFIG_FILE_PATH``` is ```APP_PATH/dist/config/config.toml```  

To set the ```APP_PATH``` use ```ProjectPathsDict.set_app_path()```.  
```ProjectPathsDict.get_exec_folder()``` provides the parent of the executed ```script``` or ```exe```.  

#### ConfigFileManager
Class to manage ```.toml``` files.  

#### ConfigDict
Class to access <code>dict</code> objects values with doted notation.  
Used by a [ConfigFileManager](#configfilemanager) to access data.

#### Example
Project structure
```
APP_PATH
├── dist
│   ├── config
│   │   ├── config.toml
│   │   └── ...
│   └── ...
├── src
│   ├── main.py
│   └── ...
└── ...
```
config.toml
```toml
[app]
    name = 'MyApp'
    version = '0.0.1'
    ...
```
main.py
```python
from .src.config import ConfigDict, ConfigFileManager, ProjectPathsDict, cfg

ppaths: ProjectPathsDict = ProjectPathsDict() \
    .set_app_path(ProjectPathsDict.get_exec_folder().parent[2]
cfg = ConfigFileManager(ppaths[ProjectPathsDict.CONFIG_FILE_PATH])

print(ppaths[ProjectPathsDict.APP_PATH])
print(ppaths[ProjectPathsDict.DIST_PATH])
print(ppaths[ProjectPathsDict.CONFIG_PATH])
print(ppaths[ProjectPathsDict.CONFIG_FILE_PATH])

print(cfg.app.name)
print(cfg.app.version)

cfg.app.version = '0.0.2'

print(cfg.app.version)

ppaths.setAppPath(ppaths[ProjectPathsDict.DIST_PATH])
print(ppaths[ProjectPathsDict.APP_PATH])
print(ppaths[ProjectPathsDict.DIST_PATH])
print(ppaths[ProjectPathsDict.CONFIG_PATH])
print(ppaths[ProjectPathsDict.CONFIG_FILE_PATH])
```
```
>> C:/.../APP_PATH
>> C:/.../APP_PATH/dist
>> C:/.../APP_PATH/dist/config
>> C:/.../APP_PATH/dist/config/config.toml
>> MyApp
>> 0.0.1
>> 0.0.2
>> C:/.../APP_PATH/dist
>> None
>> None
>> None
```
