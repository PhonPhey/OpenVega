#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   ____               __      __                         _____ _____
#  / __ \              \ \    / /                   /\   |  __ \_   _|
# | |  | |_ __   ___ _ _\ \  / /__  __ _  __ _     /  \  | |__) || |
# | |  | | '_ \ / _ \ '_ \ \/ / _ \/ _` |/ _` |   / /\ \ |  ___/ | |
# | |__| | |_) |  __/ | | \  /  __/ (_| | (_| |  / ____ \| |    _| |_
#  \____/| .__/ \___|_| |_|\/ \___|\__, |\__,_| /_/    \_\_|   |_____|
#        | |                        __/ |
#        |_|                       |___/

from abc import ABC, abstractmethod
import arduino


class initModule():

    def __init__(self, port):
        self.port = port
