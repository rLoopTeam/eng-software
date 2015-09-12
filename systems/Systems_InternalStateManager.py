#----------------------------#
# File: Systems_InternalStateManager.py
# Description: Tracks and reports the internal state of the virtual systems
# Author: Tom Rader
# Date: 2015-09-11
#----------------------------#
#
# Change Log:
# Document created  2015-09-11  Created the initial file
#---------------------------#
import random
class InternalStateManager:

    def __init__(self):
        self.currentState = 0
        self.stateHistory =[] # This is to simulate data logging

    def ISM_GenerateNewState(self):
        self.stateHistory.append(self.currentState) 
        # print "Generating a new state"
        
        random.seed()
        newState= random.randint(1,99)

        self.currentState = newState

    def ISM_GetCurrentState(self):
        oldState = self.currentState
        self.ISM_GenerateNewState()
        return oldState

    def ISM_GetStateHistory(self):
        return self.stateHistory

# Test class for InternalStateManager
# Initializes an instance of InternalStateManager, has it generate a 10 new states
# and then checks it's list against InternalStateManagers to test that the data logging
# works.
class InternalStateManager_TEST:

    my_ISM = InternalStateManager()
    def __init__(self):
        print "Begining InternalStateManager_TEST:",
        my_ISM = InternalStateManager()
        my_ISM_stateHistory = []
        for i in range(0,10):
            my_ISM_stateHistory.append(my_ISM.ISM_GetCurrentState())

        # Test if both stateHistories match
        if my_ISM_stateHistory == my_ISM.ISM_GetStateHistory():
            print 'Pass'
        else:
            print 'Fail'
            print my_ISM_stateHistory
            print my_ISM.ISM_GetStateHistory()

my_ISM_TEST = InternalStateManager_TEST()
'Done'
