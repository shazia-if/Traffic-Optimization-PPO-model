import numpy as np
import os
import random
import sumo_rl
from sumo_rl.environment.env import SumoEnvironment


"""This is a Fixed Policy based code where the agent takes constant actions every step cycle"""
def policy(ts_id, phase_tracker, num_phases):
    # current phase for the given ts_id is given by: 
    current_phase = phase_tracker.get(ts_id, 0)
    # Updating the phase for the next call
    next_phase = (current_phase + 1) % num_phases
    phase_tracker[ts_id] = next_phase
    return current_phase

# routes120kExtraHeavyTraffic_Biased0.rou 
if __name__ == "__main__":
    env = SumoEnvironment(
        net_file="4x4-grid/nets/RESCO/grid4x4/grid4x4.net.xml",
        route_file="routes120kExtraHeavyTraffic_Biased0.rou.xml",
        out_csv_name="outputs/grid4x4/fixed_policy/without_RL_", 
        use_gui=True,  
        num_seconds= 48000,  
        delta_time=10,
    )

    print("Environment created")

    obs = env.reset()
    done = {ts_id: False for ts_id in env.ts_ids}  
    total_reward = 0
    rewards_list = []

    # a phase tracker for each traffic signal
    phase_tracker = {ts_id: 0 for ts_id in env.ts_ids}

    while not all(done.values()):  
        actions = {}
        for ts_id in env.ts_ids:
            
            num_phases = env.action_spaces(ts_id).n
            #print("num phases:", num_phases) # for testing
            actions[ts_id] = policy(ts_id, phase_tracker, num_phases)
            #print("actions[ts_id]", actions[ts_id], "ts_id:", ts_id) # for testing

        obs, rewards, done, info = env.step(actions)
        step_reward = sum(rewards.values())
        total_reward += step_reward  # total_reward += sum(rewards.values())
        rewards_list.append(step_reward)  # Appending the step reward to the list

        # mean and standard deviation of rewards
        mean_reward = np.mean(rewards_list)
        std_reward = np.std(rewards_list)

       
        if env.sim_step >= env.sim_max_time:
            print("Simulation reached maximum time.")
            break

    print(f"Total reward from fixed policy: {total_reward}")
    print(f"Mean reward: {mean_reward}")
    print(f"Standard deviation of reward: {std_reward}")
    #print(rewards_list)

    try:
        env.save_csv(env.out_csv_name, env.episode)
        print(f"CSV output saved to {env.out_csv_name}")
    except Exception as e:
        print(f"Failed to save CSV: {e}")

    env.close()