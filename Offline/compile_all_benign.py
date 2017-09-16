#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 04:52:22 2017

@author: manaar
"""

import os

chstone_directory = "../CHStone_Program/"
benign_program_directory = "./benign_executables/"
executable_files = ['bf.c', 'dfmul.c', 'sha_driver.c', 'dfdiv.c', 'gsm.c', 'mips.c', 'mpeg2.c', 'main.c', 'dfsin.c', 'dfadd.c', 'aes.c', 'adpcm.c']

def compile_benign():
    if not os.path.exists(benign_program_directory):
        os.makedirs(benign_program_directory)
    list_directory = os.listdir(chstone_directory)
    for directory in list_directory:
        list_files = os.listdir(chstone_directory+directory)
        compile_file = [i for i in list_files if i in executable_files]
        if compile_file[0] == "bf.c":
            object_file = "blowfish"
        elif compile_file[0] == "sha_driver.c":
            object_file = "sha"
        elif compile_file[0] == "mpeg2.c":
            object_file = "motion"
        elif compile_file[0] == "main.c":
            object_file = "jpeg"
        else:
            object_file = compile_file[0].split(".")[0]
        command = ("gcc "+chstone_directory+directory+"/%s -o "+benign_program_directory+"%s") % (compile_file[0], object_file)
        os.system(command)