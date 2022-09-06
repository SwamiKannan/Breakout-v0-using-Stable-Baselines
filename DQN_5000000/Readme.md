# DQN with 5M steps

## Reference
[Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602)

## Parameters
Default parameters as per [Stable Baselines](https://stable-baselines3.readthedocs.io/en/master/modules/dqn.html)\
buffer_relay parameter set to 39500 instead of 1M to allow for limitations in graphics card memory

## Performance logs
![Trained model](logs/TensorBoard.png)

## Renders
1. Random <br>
![Random agent](render/random.gif)

2. Modelled <br>
![Modelled agent](render/Modelled.gif)
