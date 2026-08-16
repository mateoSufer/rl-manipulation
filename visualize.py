import gymnasium as gym
import gymnasium_robotics
from stable_baselines3 import SAC


gymnasium_robotics.register_robotics_envs()
env = gym.make("HandManipulateBlockRotateZDense-v1", render_mode="human")
model = SAC.load("hand_manipulation_model", env=env)

observation, info = env.reset()

for _ in range(5000):
    action, _ = model.predict(observation)
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()

env.close()