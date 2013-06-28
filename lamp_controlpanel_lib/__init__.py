# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2013 Vibhav Sinha vsinha@webdweb.com
# This file is distributed under the license LGPL version 3 or later
### END LICENSE

### DO NOT EDIT THIS FILE ###

'''facade - makes lamp_controlpanel_lib package easy to refactor

while keeping its api constant'''
from . helpers import set_up_logging
from . Window import Window
from . lamp_controlpanelconfig import get_version
