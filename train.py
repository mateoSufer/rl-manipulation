import gymnasium as gym
import gymnasium_robotics
from stable_baselines3 import SAC
from stable_baselines3.her.her_replay_buffer import HerReplayBuffer

gymnasium_robotics.register_robotics_envs()
env = gym.make("HandManipulateBlockRotateZDense-v1")

model = SAC(
    policy="MultiInputPolicy",
    env=env,
    replay_buffer_class=HerReplayBuffer,
    buffer_size=200000,
    verbose=1
)

model.learn(total_timesteps=1000000)

model.save("hand_manipulation_model")