# snap-game
A command line application for a game of snap in Python.

- To play, please install all the dependencies and run main.py.
- Instructions and steps are displayed in the console thorughout the game.
- Time delays have been added throughout to ensure output is easier to read. 
- Random time delays have been added when playing and calling snap to attempt to simulate more realistic playing.
- Number of players are restricted to 2 in this game.
- Game is customisable using user input for the following options: number of decks to use, number of rounds to play, game ending condition and different snap conditions.
- After game setup, in the playing stage, use ESC key to terminate script in terminal. Normal terminal keyboard commands are blocked due to the use of keyboard listeners.

Note Mac Users:
- If using a Mac with touchbar, beware when pressing the ESC key. 
- Pressing the blank area just left of the ESC key in Touchbar generates multiple TAB inputs
- Multiple TABs create an observed behaviour in terminal "Display all 2536 possibilities? (y or n)"
- To stop this from executing many times, press ESC and then enter 'n' into the terminal.

Update:
- Missing some unit tests