
# Simple Pendulum Project

This project implements a simple pendulum simulation using the Turtle graphics library in Python. It allows you to visualize the motion of a pendulum and observe its behavior.

## Installation

To run this project, follow these steps:

1. Clone the repository or download the `main.py` and `pendulum.py` files.
2. Make sure you have Python 3.x installed on your system.
3. Install the required libraries by running the following command:
   ```
   pip install turtle
   ```
4. Open a terminal or command prompt and navigate to the directory where the files are located.
5. Run the project by executing the `main.py` file:
   ```
   python main.py
   ```

## Usage

After running the project, a window will open displaying the pendulum simulation. The pendulum consists of a rope and a bob. The bob will swing back and forth under the influence of gravity.

You can customize the pendulum by modifying the parameters in the `Pendulum` class constructor:

```python
p = Pendulum(wn, turtle.Vec2D(0, 200), rope_len=300, angle=math.radians(90))
```

- `wn`: The turtle screen object representing the window.
- `start_pos`: The starting position of the pendulum rope (origin point).
- `bob_radius`: The radius of the bob (circle).
- `rope_len`: The length of the pendulum rope.
- `angle`: The angle the rope makes with the y-axis (in radians).

## Formula

The motion of the pendulum is governed by the following formula:

```
angular_acceleration= -g*sin(theta)/L
angular_velocity -= angular_acceleration
theta -= angular_velocity
bob_position=(origin.x+L*sin(theta), origin.y-L*cos(theta))
```

Where:
- `g`: The acceleration due to gravity.
- `theta`: The angle the pendulum makes with the vertical axis.
- `L`: The length of the pendulum rope.
- `angular_velocity`: The angular velocity of the pendulum.



## License

This project is released under the [MIT License](LICENSE).

## Contributions

Contributions to this project are welcome. If you would like to contribute, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive messages.
- Push your changes to your fork.
- Submit a pull request, explaining the changes you have made.

## Authors

- [Showmen Dey](https://github.com/showmen78/)



