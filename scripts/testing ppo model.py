from stable_baselines3 import PPO
import sumo_rl
import supersuit as ss
from stable_baselines3.common.vec_env import VecMonitor
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common.vec_env import VecTransposeImage
from stable_baselines3.common.vec_env import VecNormalize
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
import gym
import os
import numpy as np
import argparse
import torch

PATH = os.path.dirname(sumo_rl.__file__)

env = sumo_rl.parallel_env(net_file= "data/nets/map/grid4x4.net.xml" , 
route_file= "" , # change it
out_csv_name="outputs/testing outputs/",
use_gui=True, 
num_seconds=48000,render_mode="human",
)
env.delta_time = 10

env.render_mode = "human"
env.unwrapped.render_mode = "human"

env = ss.pad_action_space_v0(env)  
env = ss.pad_observations_v0(env)
env = ss.pettingzoo_env_to_vec_env_v1(env)
env = ss.concat_vec_envs_v1(env, 1, num_cpus=1, base_class="stable_baselines3")
env = VecMonitor(env)

model = PPO.load("ppo_model_test_version", env=env) #model name 

episode_rewards, episode_lengths = evaluate_policy(model, env, n_eval_episodes=10, return_episode_rewards= True)
mean_reward = np.mean(episode_rewards)
std_reward = np.std(episode_rewards)
print(f"Episode Rewards: {episode_rewards}, Episode Length: {episode_lengths}")
print(f"Mean Rewards:{mean_reward}, Standard Deviation Rewards:{std_reward}")

