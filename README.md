# PsychoPy plugin for LSL

Explore ways to send messages from a PsychoPy experiment over [Lab Streaming Layer (LSL)](https://labstreaminglayer.org/) and have them included in the shared data file.

> [!WARNING]
> This project is in the planning stage.
> The LSL messaging function described here is not implemented, so there is not yet a plugin you can install and use for this purpose.

## What we hope to make possible

When running an experiment, researchers may want to mark important events, e.g., when a stimulus appears or a participant responds, so those events can be considered alongside other recorded data.

The first goal is to explore how PsychoPy can send such messages over LSL and have them appear in the shared data file.

The broader hope is to make useful LSL functions easier to use from PsychoPy's Builder.
What those functions should be, and how they should work, remains open for discussion.

## Using the project

There is not yet an LSL function to install or use.
The example components and other code currently in the repository came from the [PsychoPy plugin template](https://github.com/psychopy/psychopy-plugin-template); they are examples for plugin development, not working LSL features.

If you are interested in trying or shaping the idea, please start a discussion or issue in the project repository.
Opinions about what would be useful in an experiment are especially welcome.

## Project status and development

The project is at an early stage.
No particular design or interface has been decided, and this repository should not yet be used as part of an experiment.

Researchers, PsychoPy users, and developers are welcome to contribute ideas, questions, and eventually code.
See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance, and the [development and setup guide](docs_src/development.rst) for information about the starter code and working with the repository.

## Authors

- Johannes Keyser <johannes.keyser@uni-hamburg.de>

## License

Project code is licensed under the [European Union Public Licence (EUPL-1.2)](LICENSE.txt).
