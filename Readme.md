# Breakout
## Description:
Another famous Atari game. The dynamics are similar to pong: You move a paddle and hit the ball in a brick wall at the top of the screen. Your goal is to destroy the brick wall. You can try to break through the wall and let the ball wreak havoc on the other side, all on its own! You have five lives. Detailed documentation can be found on the AtariAge page.

## Training steps:
1. Inital exploration across algorithms - 200K
2. Final training for PPO and RecurrentPPO - 5M

## Results:
### Randomly acting agent:
![Initial](random.gif)

### Modelled agent
![Trained model](modelled.gif)
