### Config file
#### ProjectPathsDict
Dict with validation for paths. On error <code>path = None</code>.  
<code>ppath</code> is an instance of <code>ProjectPathsDict</code> containing default paths.  
Default <code>APP_PATH</code> is <code>../\<main>.py</code> when executed <code>py \<main>.py</code>. When executed from <code>prg.exe</code> is <code>../\<prg>.exe</code>  
Default <code>DIST_PATH</code> is <code>APP_PATH/dist</code>  
Default <code>CONFIG_PATH</code> is <code>APP_PATH/dist/config</code>  
Default <code>CONFIG_FILE_PATH</code> is <code>APP_PATH/dist/config/config.toml</code>  

#### ConfigFileManager
Class to manage <code>.toml</code> files  
<code>cfg</code> is an instance of <code>ConfigFileManager</code> for <code>APP_PATH/dist/config/config.toml</code>  
On error <code>cfg = None</code>

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
from MyPyUtils.config import ConfigFileManager, ProjectPathsDict, cfg, ppaths


print(ppaths[ProjectPathsDict.APP_PATH])
print(ppaths[ProjectPathsDict.DIST_PATH])
print(ppaths[ProjectPathsDict.CONFIG_PATH])
print(ppaths[ProjectPathsDict.CONFIG_FILE_PATH])

print(cfg.app.name)
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
>> C:/.../APP_PATH/dist
>> None
>> None
>> None
```
