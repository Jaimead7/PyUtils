### Logs
<code>loggingLevel</code> can be defined in the <code>config.toml</code> file under the <code>[app]</code> section.  
If it is not defined, the default value is <code>Debug</code>.  
```toml
[app]
    loggingLevel = "Debug"  #[Debug, Info, Warning, Error, Critical]
    ...
```
```python
from MyPyUtils.logs import Styles, criticalLog, debugLog, errorLog, infoLog, setLoggingLevel, warningLog

debugLog('Test debug')
infoLog('Test info')
warningLog('Test warning')
errorLog('Test error')
criticalLog('Test critical')

setLoggingLevel(logging.CRITICAL)

debugLog('Test new debug', style= Styles.PURPLE)
infoLog('Test new info', style= Styles.PURPLE)
warningLog('Test new warning', style= Styles.PURPLE)
errorLog('Test new error', style= Styles.PURPLE)
criticalLog('Test new critical', style= Styles.PURPLE)
```  
```
>> DEBUG -----> 01/03/2025 13:55:42: Test debug1
>> WARNING ---> 01/03/2025 13:55:42: Test warning
>> ERROR -----> 01/03/2025 13:55:42: Test error
>> CRITICAL --> 01/03/2025 13:55:42: Test critical
>> CRITICAL --> 01/03/2025 13:55:42: Test new critical
```