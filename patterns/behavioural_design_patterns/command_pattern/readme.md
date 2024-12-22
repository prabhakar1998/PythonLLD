# Command design pattern

Command design pattern provides abstraction to the client and allows to not worry about the implementation.
It also provides ability to undo the operation or command by keeping the history of commands.

# Key Components

Command Interface:
    declares and executable method

Concrete command:
    implements the Command interface executable method, binding the receiver and the action

Receiver:
    The object that actually performs the work, when the command execute method is called.

Invoker:
    Keeps the reference of the commands and triggers the execution of the command

Client:
    Creates and configures the command and their receiver



# Problem and solution implemented

Assume a system that has different commands, these commands can be invoked via file or via command line.
Implement the solution for the same.
Check the parking lot example for this command pattern implementation.