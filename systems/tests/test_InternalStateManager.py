# pyTest file for Systems_InternalStateManager.py
from ..Systems_InternalStateManager import InternalStateManager
def test_ISM():
    my_ISM = InternalStateManager()
    my_ISM_stateHistory = []
    my_ISM = InternalStateManager()
    my_ISM_stateHistory = []
    for i in range(0,10):
        my_ISM_stateHistory.append(my_ISM.ISM_GetCurrentState())
    
    # Test if both stateHistories match
    if my_ISM_stateHistory == my_ISM.ISM_GetStateHistory():
        assert True
    else:
        assert False 
