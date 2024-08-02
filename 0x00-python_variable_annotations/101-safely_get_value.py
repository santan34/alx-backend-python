#!/usr/bin/env python3
from typing import Mapping, Any, Union
def safely_get_value(dct: Mapping[Any,Any], key:Any, default:Union[] = None):
    if key in dct:
        return dct[key]
    else:
        return default