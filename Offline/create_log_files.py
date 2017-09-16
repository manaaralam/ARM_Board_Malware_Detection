#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 07:20:27 2017

@author: manaar
"""

import os
import generate_perf_script

if not os.path.exists(generate_perf_script.path_to_benign_log_file):
    os.makedirs(generate_perf_script.path_to_benign_log_file)
    generate_perf_script.generate_benign()
    os.system("./run_all_benign.sh")

if not os.path.exists(generate_perf_script.path_to_malware_log_file):
    os.makedirs(generate_perf_script.path_to_malware_log_file)
    generate_perf_script.generate_malware()
    os.system("./run_all_malware.sh")
