#!/usr/bin/env python
# -*- Coding: UTF-8 -*-
# Author: Jakob Friedl
# Created on: Thur, 14. Dec 2023
# Description: NoPowerShell.exe port to Havoc C2. Execute powershell cmdlets in memory.

from havoc import Demon, RegisterCommand 

nps_binary = "NoPowerShell.exe"

def nps_parse_params( demon, params ):
    args : str = ""
    for p in params:
        args = args + " " + p
    return args

def nps( demonID, *params ):
    TaskID : str = None 
    demon : Demon = None
    demon = Demon(demonID)
    
    args = nps_parse_params(demon, params)

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Executing NoPowerShell.exe")
    demon.DotnetInlineExecute(TaskID, nps_binary, args)

    return TaskID

RegisterCommand( nps, "", "nps", "Use NoPowerShell.exe to run PowerShell cmdlets in memory.", 0, "command arguments", "Get-ADUser -Filter *" )
