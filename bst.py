
import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)


BSTree : TypeAlias = Union[None, "BSTNode"]

class BSTNode:
    val =  int 
    left : BSTree
    right : BSTree
