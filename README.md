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

After install Snips NLU
```
$ pip install snips-nlu==[NLU_VERSION_USED_IN_DATASET]
```