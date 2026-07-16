import gymnasium_robotics
import gymnasium as gym

gymnasium_robotics.register_robotics_envs()

env = gym.make("HandManipulateBlock-v1", render_mode = "human")
obserbation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()
    
print("Claves del estado:", observation.keys())
for key, value in observation.items():
    print(f"  {key}: {value.shape}")
print("Acciones:", env.action_space.shape)

env.close()