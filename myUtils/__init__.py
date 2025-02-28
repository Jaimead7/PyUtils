from .src.config import (APPLICATIONPATH, CONFIGPATH, DISTPATH,
                         ConfigFileManager, cfg)
from .src.debug import Styles, debug
from .src.Immutable import Immutable
from .src.noInstantiable import NoInstantiable
from .src.validation import ValidationClass

debug(f'Package loaded: myUtils', Styles.OKGREEN)
