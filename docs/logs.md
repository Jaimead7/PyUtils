### Logs
<code>loggingLevel</code> can be defined in the <code>config.toml</code> file under the <code>[app]</code> section.  
If it is not defined, the default value is <code>Debug</code>.  
```toml
[app]
    loggingLevel = "Debug"  #[Debug, Info, Warning, Error, Critical]
    ...
```
```python
import logging
from pyUtils.logs import Styles, MyLogger

myLogger = MyLogger(__name__, logging.DEBUG)

myLogger.debugLog('Test debug')
myLogger.infoLog('Test info')
myLogger.warningLog('Test warning')
myLogger.errorLog('Test error')
myLogger.criticalLog('Test critical')

myLogger.setLoggingLevel(logging.CRITICAL)

myLogger.debugLog('Test new debug', style= Styles.PURPLE)
myLogger.infoLog('Test new info', style= Styles.PURPLE)
myLogger.warningLog('Test new warning', style= Styles.PURPLE)
myLogger.errorLog('Test new error', style= Styles.PURPLE)
myLogger.criticalLog('Test new critical', style= Styles.PURPLE)
```  
```
>> DEBUG[Logg.Name] -----> 01/03/2025 13:55:42: Test debug1
>> WARNING[Logg.Name] ---> 01/03/2025 13:55:42: Test warning
>> ERROR[Logg.Name] -----> 01/03/2025 13:55:42: Test error
>> CRITICAL[Logg.Name] --> 01/03/2025 13:55:42: Test critical
>> CRITICAL[Logg.Name] --> 01/03/2025 13:55:42: Test new critical
```