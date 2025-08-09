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

my_logger = MyLogger(__name__, logging.DEBUG)

my_logger.debug('Test debug')
my_logger.info('Test info')
my_logger.warning('Test warning')
my_logger.error('Test error')
my_logger.critical('Test critical')

my_logger.set_logging_level(logging.CRITICAL)

my_logger.debug('Test new debug', style= Styles.PURPLE)
my_logger.info('Test new info', style= Styles.PURPLE)
my_logger.warning('Test new warning', style= Styles.PURPLE)
my_logger.error('Test new error', style= Styles.PURPLE)
my_logger.critical('Test new critical', style= Styles.PURPLE)
```  
```
>> DEBUG[Logg.Name] -----> 01/03/2025 13:55:42: Test debug1
>> WARNING[Logg.Name] ---> 01/03/2025 13:55:42: Test warning
>> ERROR[Logg.Name] -----> 01/03/2025 13:55:42: Test error
>> CRITICAL[Logg.Name] --> 01/03/2025 13:55:42: Test critical
>> CRITICAL[Logg.Name] --> 01/03/2025 13:55:42: Test new critical
```