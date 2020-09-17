
# these import everything from the module "module_converters"
import modules_converters
import modules_converters as mc

# these only import specific parts of the module "module_converters"
from modules_converters import pounds_to_kb
from modules_converters import kg_to_pounds as k

import modules_utils as utils
from modules_utils import maximum, foo

print(modules_converters.kg_to_pounds(80))
print(mc.kg_to_pounds(30))

print(utils.maximum([3, 0, -1, 999, 3, 2, 100]))