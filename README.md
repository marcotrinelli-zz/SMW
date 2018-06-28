# SMW
Retrieve remotely intents and slots using the Snips NLU engine
# Installation

## Prerequisites
First install RUST
### Windows
https://www.rust-lang.org/en-US/install.html
Note: Once installed you need to restart your computer
### Linux
```
curl https://sh.rustup.rs -sSf | sh
```

Then, install setuptools_rust library
```
$ pip install setuptools_rust
```

After install Snips NLU, using the version found in the _trained_assistant.json_ file downloaded from the Snips Console.
The version to look up is in the entry "training_package_version": [NLU_VERSION]

```
$ pip install snips-nlu==[NLU_VERSION]
```

Install the Snips NLU english language resources
```
$ snips-nlu download en
```