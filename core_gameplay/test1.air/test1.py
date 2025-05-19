# -*- encoding=utf8 -*-
__author__ = "Administrator"
import os
from airtest.core.api import *

auto_setup(__file__)
import os
print("当前工作目录:", os.getcwd())
print("图片目录内容:", os.listdir(ST.IMAGE_DIR))