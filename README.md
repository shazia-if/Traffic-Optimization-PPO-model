# Traffic-Optimization-PPO-model
Training a PPO model for Traffic Optimization and Testing its performance across various traffic datasets using the sumo-rl library and sumo gui.

**Using the sumo-rl Library and SUMO GUI**

This project investigates the application of Proximal Policy Optimization (PPO) for adaptive traffic signal control in a simulated traffic environment. The model is trained using the sumo-rl library and evaluated in the SUMO GUI across various traffic conditions including high, medium, and low congestion, with both biased and unbiased traffic flows.

Through reinforcement learning, the system aims to minimize average vehicle waiting times and reduce congestion. The PPO model is tested against a fixed-action policy, and performance is assessed using custom metrics including queue length, mean speed, total waiting time, and an optimization score.

**Explanatory Report**

Read online: 

Download PDF:

**Case Study Report**

Read online: 

Download PDF: 

This report presents an in-depth comparison of the PPO model against a fixed policy. It discusses model setup, traffic simulation strategies, reward mechanisms, performance metrics, and highlights the PPO model's adaptability under dynamic traffic conditions.

### Project Directory Overview

```
Traffic-Optimization-PPO-model/
├── README.md                  
├── requirements.txt           
│
├── model/                     
│   └── ppo_model_test_version.zip
│
├── scripts/                   
│   ├── training ppo model.py
│   ├── testing ppo model.py
│   ├── baseline_code.py
│   ├── optimization_score.py
│   ├── my_plot.py
│   ├── random_routes.py
│   └── significance testing.py
│
├── data/                      
│   ├── results rewards.csv
│   ├── randomTrips.py
│   ├── outputs/
│   │   ├── training_outputs/
│   │   └── testing_outputs/
│   └── nets/
│       ├── maps/
│       └── scenario route files/
│
├── future_work/               #Ongoing
│   └── application/
│
└── references/                
    └── 
```

The visuals below provide a comprehensive overview of the project, illustrating the model architecture, training workflow, and key performance outcomes
![1](https://github.com/user-attachments/assets/273fdfc1-3f7a-4823-8fd5-69d7eb2d5378)
![2](https://github.com/user-attachments/assets/1a88cb3e-4ab6-454c-8936-3e5eb13b032d)
![3](https://github.com/user-attachments/assets/83cccdc8-1782-4064-aea0-af35e651d5d6)





