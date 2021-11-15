#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 06:06:05 2021

@author: alpha
"""

#solving the Gambler's Problem using Value Iteration
#solution based on given lisp script of reference book

# =============================================================================
#Gambler's problem. The gambler has a stake s between 0 and 100. At each play he wagers an integer <= s. He wins that much with prob p, else he loses that much. If he builds his stake to 100 he wins (thus he never wagers more than (- 100 s)); if his stake falls to 0 he loses.
# =============================================================================

#episodic MDP framewrok
#fixed tansition probability (or ignored)
#terminal condition: capital reaches 100


#stake/capital as states, bet size as actions.
#states space: [1,100]  action space: [1, min(state,100-state)]


import numpy as np
import matplotlib.pyplot as plt

states =[i for i in range(1,100)]
state_values=[0 for i in range(1,101)]
state_values[-1]=1

win_prob=0.75
#lmbda = 1  #discount factor sets to 1, hence no need to consider order


def get_action_value(state, action):
    """
    given state and action return action value for next state
    """
    global win_prob
    action_value=win_prob*(state+action)+(1-win_prob)*(state-action)
    return action_value


def value_iteration(max_iteration=100,win_prob=0.75):
    """
    value iteration for given max iteration times
    """
    global states
    global state_values
    for i in range(max_iteration):
        for state in states:
            old_state_value=state_values[state]
            action_space=[i for i in range(1,min(state+1,101-state))]
            #print(action_space)
            action_values=[]
            for action in action_space:
                #print(action)
                #print(state)
                action_value=get_action_value(state,action)
                #print(action_value)
                action_values.append(action_value)
            max_action_value=max(action_values)
            if max_action_value>old_state_value:
                state_values[state]=max_action_value
            else:
                pass
    return state_values



def get_policy(max_iteration=100,win_prob=0.75):
    """
    """
    global states
    global state_values
    policy = [0 for i in range(0,101)]
    for i in range(max_iteration):
        for state in states:
            old_state_value=state_values[state]
            action_space=[i for i in range(1,min(state+1,101-state))]
            #print(action_space)
            action_values=[]
            action_dict={}
            for action in action_space:
                #print(action)
                #print(state)
                action_value=get_action_value(state,action)
                #print(action_value)
                action_values.append(action_value)
                action_dict.update({action:action_value})
            max_action_value=max(action_values)
            if max_action_value>old_state_value:
                state_values[state]=max_action_value
                for keys, values in action_dict.items():
                    if values ==max_action_value:
                        policy[state]=keys
                    else:
                        pass
            else:
                pass
    return policy


policy = get_policy(max_iteration=10, win_prob=0.75)

plt.scatter(states, policy[:99])
plt.xlabel('Capital')
plt.ylabel('Policy(bet size)')
plt.show()



