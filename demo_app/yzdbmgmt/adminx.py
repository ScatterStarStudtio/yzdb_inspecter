import xadmin
import inspect, sys

from .models import TSchool, TClass, TTeacher, TStudent, TUserpaperattribute, TUserscore, TExaminfo, TExamcard, TTestquestions, \
    TTestproblem
from re import split

def get_columns(cls):
    columns_raw = str(cls.__doc__)
    columns_raw = split('([a-zA-Z_0-9]+)(?:,|\))', columns_raw)
    return tuple(columns_raw[1::2])

operation_clses = [m[1] for m in inspect.getmembers(sys.modules["yzdbmgmt.models"], inspect.isclass) if m[0].startswith('T')]

# operation_clses = [
#     TSchool, TClass, TTeacher, TStudent, TUserpaperattribute, TUserscore, TExaminfo, TExamcard, TTestquestions,
#     TTestproblem
# ]

for cls in operation_clses:
    xadmin.site.register(
        cls,
        type(
            cls.__name__ + "Admin", (object,),
            {'list_display': get_columns(cls), 'list_filter': get_columns(cls), 'search_fields': get_columns(cls)}
        )
    )