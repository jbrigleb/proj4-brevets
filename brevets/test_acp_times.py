"""
Nose tests for acp_times.py
"""

import acp_times
import nose
import arrow


def test_zero():
    """
    test that a controle distance of 0 returns start time
    """
    #print('2018-01-01T00:00:00+00:00')
    #print(acp_times.open_time(0, 200, '2018-01-01T00:00:00+00:00'))
    
    assert (acp_times.open_time(0, 200, '2018-01-01T00:00:00+00:00') == '2018-01-01T00:00:00+00:00') and (acp_times.close_time(0, 200, '2018-01-01T00:00:00+00:00') == '2018-01-01T00:00:00+00:00')
    
def test_negative():
    """
    test that a negative controle distance returns start time
    """
    
    assert (acp_times.open_time(-50, 200, '2018-01-01T00:00:00+00:00') == '2018-01-01T00:00:00+00:00') and (acp_times.close_time(-50, 200, '2018-01-01T00:00:00+00:00') == '2018-01-01T00:00:00+00:00')
    
def test_brevet_edge():
    """
    tests whether a controle at exactly the brevet distance returns the correct valuation
    """
    #print(acp_times.open_time(200, 200, '2018-01-01T00:00:00+00:00'))
    #print(acp_times.close_time(200, 200, '2018-01-01T00:00:00+00:00'))
    assert (acp_times.open_time(200, 200, '2018-01-01T00:00:00+00:00') == '2018-01-01T05:53:00+00:00') and (acp_times.close_time(200, 200, '2018-01-01T00:00:00+00:00') == '2018-01-01T13:30:00+00:00')
    
    
def test_over_under():
    """
    test whether a controle placed over the brevet distance, but under 1.2 X the distance returns correct value
    (correct value being the same as if the controle distance was the brevet distance)
    """
    assert (acp_times.open_time(230, 200, '2018-01-01T00:00:00+00:00') == '2018-01-01T05:53:00+00:00') and (acp_times.close_time(230, 200, '2018-01-01T00:00:00+00:00') == '2018-01-01T13:30:00+00:00')
    
def test_over_1_2():
    """
    tests whether an err flag is returned when controle is > 1.2 X brevet
    """
    assert acp_times.open_time(250, 200, '2018-01-01T00:00:00+00:00') == 'err'
