import printing_functions as pf

unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

"""可以使用如下方式调用：
方式一：
# import 模块名
import printing_functions

# 调用函数： 模块名.函数()
printing_functions.print_models()
printing_functions.show_completed_models()

方式二：
# from 模块名 import 函数名
from printing_functions import print_models
from printing_functions import show_completed_models 

# 调用函数： 函数()
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

方式三：
# from 模块名 import 函数名 as 函数别名
from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm

# 调用函数： 函数别名()
pm(unprinted_designs, completed_models)
scm(completed_models)

方式四：
# import 模块名 as 模块别名
import printing_functions as pf

# 函数调用： 模块别名. 函数()
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

方式五：
# from 模块名 import *
from printing_functions import *

# 使用时不需要加模块名前缀
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
"""

