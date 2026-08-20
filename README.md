# Hand Manipulation RL Agent

## Description
This project trains a robotic hand (Shadow Hand) to rotate a block 
to a target orientation using deep reinforcement learning. The main 
challenges are the high-dimensional action space (20 joints) and 
sparse rewards — the agent rarely achieves the goal by random 
exploration. SAC with HER addresses both problems efficiently.

## Algorithm
We use SAC because it improves training by reusing past experience 
stored in a replay buffer — different from PPO used in my previous 
project. Since reaching the goal is much harder here, reusing 
information from many past episodes makes learning more efficient. 
HER is also used to improve learning by making the agent believe it 
reached the goal even when it didn't, generating useful training 
signal from failed episodes.

## Reward Design
The default HandManipulateBlock environment uses sparse rewards — 0 at 
every step and only a positive reward when the block reaches the exact 
target orientation. This makes learning almost impossible since the agent 
rarely achieves the goal by random exploration. I switched to the Dense 
variant which provides continuous reward proportional to how close the 
block is to the target orientation, making learning significantly faster.

## Results
- Algorithm: SAC + HER
- Environment: HandManipulateBlockRotateZDense-v1
- Training steps: 1,000,000
- Training time: ~7 hours on CPU
- Best success rate: 43% (episode ~9880)
- Final success rate: ~28%

The agent learned to rotate the block toward the target orientation but 
movements are unnatural — joints move in ways that would be impossible 
or damaging on a real robot.

## Sim-to-Real Connection
The main limitation of this project is the reality gap. The agent learned 
effective strategies in simulation but with unrealistic movements — joints 
move too fast and in unnatural ways because the simulation does not model 
real physical constraints like motor limits, joint friction, or inertia.
