import os
import gym
from gym.wrappers import Monitor
import matplotlib.pyplot as plt

env_type={'Discrete':['PPO','A2C', 'DQN'],'Box':['PPO', 'A2C', 'DDPG', 'SAC', 'TD3'],'MultiDiscrete':['PPO','A2C'],'Multibinary':['PPO','A2C']}
def get_applicable_algos(action_type):
	'''
	We are going to get all the algorithms that are applicable for the given action_state space. All algos can work independently of the state space type.
	link: https://stable-baselines3.readthedocs.io/en/master/modules/a2c.html
	Algo	Space			Action	Observation
	PPO		Discrete		Yes		Yes
	PPO		Box				Yes		Yes
	PPO		MultiDiscrete	Yes		Yes
	PPO		MultiBinary		Yes		Yes
	PPO		Dict			No		Yes
				
	A2C		Discrete		Yes		Yes
	A2C		Box				Yes		Yes
	A2C		MultiDiscrete	Yes		Yes
	A2C		MultiBinary		Yes		Yes
	A2C		Dict			No		Yes
				
	DDPG	Discrete		No		Yes
	DDPG	Box				Yes		Yes
	DDPG	MultiDiscrete	No		Yes
	DDPG	MultiBinary		No		Yes
	DDPG	Dict			No		Yes
				
	DQN		Discrete		Yes		Yes
	DQN		Box				No		Yes
	DQN		MultiDiscrete	No		Yes
	DQN		MultiBinary		No		Yes
	DQN		Dict			No		Yes
				
	SAC		Discrete		No		Yes
	SAC		Box				Yes		Yes
	SAC		MultiDiscrete	No		Yes
	SAC		MultiBinary		No		Yes
	SAC		Dict			No		Yes
				
	TD3		Discrete		No		Yes
	TD3		Box				Yes		Yes
	TD3		MultiDiscrete	No		Yes
	TD3		MultiBinary		No		Yes
	TD3		Dict			No		Yes
	'''
	return env_type[action_type]
	
def run_env(env, episodes, random=True, model=""):
    total_rewards=[]
    if random:
        for _ in range(episodes):
            ep_rewards=0
            env.reset()
            while True:
                action=env.action_space.sample()
                next_state, reward,done, info=env.step(action)
                ep_rewards+=reward
                if done:
                    total_rewards.append(ep_rewards)
                    break
    else:
        if model=="":
            print('Please enter the agent model')
            
        else:
            for _ in range(episodes):
                ep_rewards=0
                state=env.reset()
                while True:
                    action,_=model.predict(state)
                    next_state, reward,done, info=env.step(action)
                    ep_rewards+=reward
                    state=next_state
                    if done:
                        total_rewards.append(ep_rewards)
                        break
        return total_rewards
        
def run_experiment(env_name,env,render_path,random=True, episodes=5, model=""):
    env=Monitor(gym.make(env_name),render_path,force=True)
    if random:
        total_rewards=run_env(env, 5)
    else:
        total_rewards=run_env(env,episodes=episodes, random=False,model=model)
    return env, total_rewards

def create_paths(algo_name,env_name,n_steps):
    log_path=os.path.join(env_name, algo_name+"_"+str(n_steps),"logs")
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    render_path=os.path.join(env_name, algo_name+"_"+str(n_steps),"render")
    if not os.path.exists(render_path):
        os.makedirs(render_path)
    model_path=os.path.join(env_name, algo_name+"_"+str(n_steps),"models")
    if not os.path.exists(model_path):
        os.makedirs(model_path)
    return(log_path, render_path, model_path)

def call_paths(algo_name,env_name,n_steps):
    log_path=os.path.join(env_name, algo_name+"_"+str(n_steps),"logs")
    render_path=os.path.join(env_name, algo_name+"_"+str(n_steps),"render")
    model_path=os.path.join(env_name, algo_name+"_"+str(n_steps),"models")
    return(log_path, render_path, model_path)

def get_action_type_name(env):
    action_space_type=str(type(env.action_space)).split('.')[3].split("'")[0] #Parsing the action_space variable to get the exact type - Discrete, Box, etc.
    return action_space_type
    
def get_all_algos(env):
    action_space_type=get_action_type_name(env)
    algo_list=get_applicable_algos(action_space_type)
    return algo_list

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i]+0.5,round(y[i],2))
    
def plot_mean(rewards,y_title):
    x=list(rewards.keys())
    y=list(rewards.values())
    plt.bar(range(len(x)),y,tick_label=x)
    plt.xlabel("Algorithm")
    plt.ylabel(y_title)
    addlabels(x,y)