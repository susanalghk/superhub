# SuperHub

SuperHub is a Python-based tool that automates and schedules regular system tasks on Windows using a cron-like scheduling system. It allows you to define tasks that need to be executed at specific times and will handle running these tasks for you in the background.

## Features

- Schedule tasks to run at specific times.
- Automate system commands or scripts.
- Runs in the background with minimal resource usage.
- Simple to set up and configure.

## Requirements

- Python 3.x
- `pywin32` module (for setting system time)

## Installation

1. Clone the repository or download the script:

```bash
git clone https://github.com/yourusername/superhub.git
```

2. Navigate to the project directory:

```bash
cd superhub
```

3. Install the required dependencies:

```bash
pip install pywin32
```

## Usage

1. Open the `superhub.py` file and add your tasks using the `add_task` method. Specify the task name, schedule time (`HH:MM` format), and the command to execute.

2. Run the script:

```bash
python superhub.py
```

3. The scheduler will start running in the background, executing tasks at their scheduled times.

## Example

To schedule a task that echoes a message at 14:30:

```python
superhub.add_task("Example Task", "14:30", "echo Hello, this is a scheduled task!")
```

## Stopping the Scheduler

To stop the scheduler, simply press `Ctrl + C` in the terminal where the script is running.

## Note

- Ensure the system time is set correctly on your Windows machine for accurate scheduling.
- The script is designed to run continuously. Ensure it's running in an environment where it won't be terminated unexpectedly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.