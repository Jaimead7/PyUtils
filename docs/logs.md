# Logs
- [Basic usage](#basic-usage)
- [Logs files](#logs-files)
- [Package module loggers](#package-module-loggers)

<br>

## Basic usage
### ```test.py```
```python
from dotenv import load_dotenv

load_dotenv()

import logging
from pyUtils import (MyLogger, config_logger, save_pyutils_logs,
                     set_pyutils_logs_path, Styles)

my_logger = MyLogger(
    logger_name= __name__,
    logging_level= logging.DEBUG,
    file_path= 'Log.log',
    save_logs= False
)

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

my_logger.save_logs = True

my_logger.debug('This will be saved')

my_logger.save_logs = False

my_logger.debug('This will NOT be saved')

my_logger.save_logs = True

my_logger.debug('This will be saved too')

my_logger.logs_file_path = 'NewLog.log'

my_logger.debug('This will be saved in the new log file')
```

### ```console output```
```
>> DEBUG[Logg.Name] -----> 01/03/2025 13:55:42: Test debug1
>> WARNING[Logg.Name] ---> 01/03/2025 13:55:42: Test warning
>> ERROR[Logg.Name] -----> 01/03/2025 13:55:42: Test error
>> CRITICAL[Logg.Name] --> 01/03/2025 13:55:42: Test critical
>> CRITICAL[Logg.Name] --> 01/03/2025 13:55:42: Test new critical
```

### ```Log.log```
```log
DEBUG[Logg.Name] -----> 01/03/2025 13:55:42: This will be saved
DEBUG[Logg.Name] -----> 01/03/2025 13:55:42: This will be saved too
```

### ```NewLog.log```
```log
DEBUG[Logg.Name] -----> 01/03/2025 13:55:42: This will be saved in the new log file
```

<br>

## Logs files
The logs are saved by default in the temporal directory of the system.  
- Windows: `TEMP` or `TMP` environment variable. `C:\Users\UserName\AppData\Local\Temp`.
- Linux: `/tmp`.  

The default path can be changed by environment variable `LOGS_PATH`.

### ```.env```
```env
LOGS_PATH="/Absolute/Custom/Path"
```

### ```test.py```
```python
from dotenv import load_dotenv

from pyUtils import *


default_logger = MyLogger(
    __name__,
    file_path= Path('default_logger.log'),
    save_logs= True
)

load_dotenv()

relative_logger = MyLogger(
    __name__,
    file_path= Path('relative_logger.log'),
    save_logs= True
)
new_relative_logger = MyLogger(
    __name__,
    file_path= Path('./other/new_relative_logger.log'),
    save_logs= True
)
absolute_logger = MyLogger(
    __name__,
    file_path= Path('/Other/Path/absolute_logger.log'),
    save_logs= True
)

default_logger.debug('This is default')
relative_logger.debug('This is relative')
new_relative_logger.debug('This is relative too')
absolute_logger.debug('This is absolute')
```

### ```/tmp/default_logger.log```
```log
DEBUG[Logg.Name] -----> 01/03/2025 13:55:42: This is default
```

### ```/Absolute/Custom/Path/relative_logger.log```
```log
DEBUG[Logg.Name] -----> 01/03/2025 13:55:42: This is relative
```

### ```/Absolute/Custom/Path/other/new_relative_logger.log```
```log
DEBUG[Logg.Name] -----> 01/03/2025 13:55:42: This is relative too
```
### ```/Other/Path/absolute_logger.log```
```log
DEBUG[Logg.Name] -----> 01/03/2025 13:55:42: This is absolute
```

<br>

## Package module loggers
Loggers for the modules of the package can be access by:
- `loggers`
- `config_logger`,
- `no_instantiable_logger`
- `timing_logger`
- `validation_logger`

`loggers` is a list of all the other loggers.  
`set_pyutils_logging_level`, `set_pyutils_logs_path` and `save_pyutils_logs` can be use to change the configuration of all of the package loggers.
By default, all loggers save the messages on a `PyUtils.log` file.