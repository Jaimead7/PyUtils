### Config file
#### ProjectPathsDict
Dict with validation for paths. On error <code>path = None</code>.  
<code>ppath</code> is an instance of <code>ProjectPathsDict</code> containing default paths.  
Default <code>APPLICATIONPATH</code> is <code>../\<main>.py</code> when executed <code>py \<main>.py</code>.  
Default <code>DISTPATH</code> is <code>APPLICATIONPATH/dist</code>  
Default <code>CONFIGPATH</code> is <code>APPLICATIONPATH/dist/config</code>  

#### ConfigFileManager
Class to manage <code>.toml</code> files  
<code>cfg</code> is an instance of <code>ConfigFileManager</code> for <code>APPLICATIONPATH/dist/config/config.toml</code>  
On error <code>cfg = None</code>

#### Example
Project structure
```
APPLICATIONPATH
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


print(ppaths['APPLICATIONPATH'])
print(ppaths['DISTPATH'])
print(ppaths['CONFIGPATH'])
print(ppaths['CONFIGFILEPATH'])

print(cfg.app.name)
print(cfg.app.version)

ppaths.setAppPath(ppaths['DISTPATH'])
print(ppaths['APPLICATIONPATH'])
print(ppaths['DISTPATH'])
print(ppaths['CONFIGPATH'])
print(ppaths['CONFIGFILEPATH'])
```
```
>> C:/.../APPLICATIONPATH
>> C:/.../APPLICATIONPATH/dist
>> C:/.../APPLICATIONPATH/dist/config
>> C:/.../APPLICATIONPATH/dist/config/config.toml
>> MyApp
>> 0.0.1
>> C:/.../APPLICATIONPATH/dist
>> None
>> None
>> None
```
