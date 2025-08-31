# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 17:23:17 2021

@author: Matt
"""

from opcua import Client
import py
import pytest
import Tags
import OPC as server
import time

Influent=    ["0:Objects", "2:FactoryTalkLinxGateway", "4:PLC",
                                   "6:Online" ,"17:AI_Influent_Level" , "var"]
Effluent=    ["0:Objects", "2:FactoryTalkLinxGateway", "4:PLC",
                                   "6:Online" ,"11:AI_Effluent_Flow" , "var"]




tag_struct= Tags.MotorTestTags
vpath= Tags.MotorTestpath
delay_time = 1
reset_tag= tag_struct[1]
countdown_time = 1

client= Client("opc.tcp://DESKTOP-RA68AK2.local.:4990/FactoryTalkLinxGateway1")
#client= Client("opc.tcp://DESKTOP-RA68AK2:4840")
def test_init_connect():
    server.OPC_Connect(client)
    print("Client connected!")

def test_PLC_HRT_Auto_test_01():
    objects = server.getvar(client)
    server.write_opc_var(objects, vpath, "PLC_HRT_Program_Auto_Manual", False)
    data = server.read_opc_var(objects, vpath, "PLC_HRT_Program_Auto_Manual")
    countdown_time = server.read_opc_var(objects, vpath, "HRT_Stop_Countdown_SP")
    time.sleep(countdown_time + 5)
    assert data == False
    
    
def test_PLC_HRT_Auto_test_02():    
    ## Influent Level
    objects = server.getvar(client)
    server.write_opc_var(objects, Influent, "EGU", 23)
    data = server.read_opc_var(objects, Influent, "EGU")
    assert data == 23
    
def test_PLC_HRT_Auto_test_03():
    ## Effluent Flow
    objects = server.getvar(client)
    server.write_opc_var(objects, Effluent, "EGU", 24)   
    data = server.read_opc_var(objects, Effluent, "EGU")
    assert data == 24
    
def test_PLC_HRT_Auto_test_04():
    ## HRT Program_Auto_Manual
    objects = server.getvar(client)
    server.write_opc_var(objects, vpath, "PLC_HRT_Program_Auto_Manual", True)
    data = server.read_opc_var(objects, vpath, "PLC_HRT_Program_Auto_Manual")
    assert data == True
    
def test_PLC_HRT_Auto_test_05():
    ## HRT Activate Countdown SP
    objects = server.getvar(client)
    countdown_time = server.read_opc_var(objects, vpath, "HRT_Activate_Countdown_SP")    
    time.sleep(countdown_time+1)
    
    ## HRT Program
    objects = server.getvar(client)
    data = server.read_opc_var(objects, vpath, "Auto_Start_Stop_Treatment")
    assert data == True
    
def test_assert_all_auto_1():
    objects = server.getvar(client)
    data = server.read_opc_var(objects, vpath, "PLC_HRT_System_Enable_Bit")
    assert data == True
    
def test_assert_all_auto_2():
    objects = server.getvar(client)
    data = server.read_opc_var(objects, vpath, "DO_Screen_System_Enable_CMD")
    assert data == True
    
def test_assert_all_auto_3():
    objects = server.getvar(client)
    data = server.read_opc_var(objects, vpath, "Veolia_System_Enable_Flag")
    assert data == True

def test_assert_all_auto_4():
    objects = server.getvar(client)
    data = server.read_opc_var(objects, vpath, "DO_Grit_System_1_Enable_CMD")
    assert data == True
    
def test_assert_all_auto_5():
    objects = server.getvar(client)
    data = server.read_opc_var(objects, vpath, "DO_Grit_System_2_Enable_CMD")
    assert data == True
    
def test_assert_all_auto_6():
    objects = server.getvar(client)
    data = server.read_opc_var(objects, vpath, "DO_MakeUp_Air_Unit_1_Enable_CMD")
    assert data == True
    
def test_assert_all_auto_7():
    objects = server.getvar(client)
    data = server.read_opc_var(objects, vpath, "DO_Makeup_Air_Unit_2_Enable_CMD_IO")
    assert data == True
    
def test_assert_all_auto_8():
    objects = server.getvar(client)
    data = server.read_opc_var(objects, vpath, "DO_Makeup_Air_Unit_3_Enable_CMD_IO")
    assert data == True
    


def test_Conveyor_SG_Auto():
    objects = server.getvar(client)
    time.sleep(delay_time)
    data0 = server.read_opc_var(objects, vpath, "Conveyor_231_Program_Auto_Manual")
    data1 = server.read_opc_var(objects, vpath, "Conveyor_232_Program_Auto_Manual")
    data2 = server.read_opc_var(objects, vpath, "Conveyor_233_Program_Auto_Manual")
    data3 = server.read_opc_var(objects, vpath, "Conveyor_131_Program_Auto_Manual")
    data4 = server.read_opc_var(objects, vpath, "Conveyor_132_Program_Auto_Manual")
    
    assert data0 == True
    assert data1 == True
    assert data1 == True
    assert data2 == True
    assert data3 == True
    assert data4 == True




def test_Grit_Conveyor_test():
    objects = server.getvar(client)
    server.write_opc_var(objects, vpath, "DI_WS_111_Washer_Compactor_Run_Status", 53)
    time.sleep(delay_time)
    data = server.read_opc_var(objects, vpath, "AI_UV_Level_Transmitter_LIT_401_Read")
    assert data == 53



def test_discon():
    server.OPC_Disconnect(client)
    print ("Client disconnected!")
    


#def test_u_00():
    
 #   objects = server.getvar(client)
    
  #  server.write_opc_var(objects, varpath, tag_Struct[0] , True)