# Back To Coding Python



# Python on MacOS



## Install Homebrew

Homebrew is a popular package manager for macOS (and Linux). Here's how to install it:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After installation, you'll need to add Homebrew to your PATH. For Apple Silicon Macs, run:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
source ~/.zshrc
```

Once installed, verify it's working with:

```
brew --version
```



----



## Install Python via Homebrew

If you want to install the specific Python version using Homebrew:

```bash
brew install python@3.12
```

Then you can make it your default Python:

```bash
echo 'alias python=/opt/homebrew/bin/python3' >> ~/.zshrc
source ~/.zshrc
```

Let me break down this code line by line:

1. `echo` prints the text that follows it
2. `alias python=/opt/homebrew/bin/python3` creates a shortcut: whenever you type `python`, it will use `/opt/homebrew/bin/python3` instead
3. `>>` appends the text to a file (rather than overwriting it)
4. `~/.zshrc` is your Zsh shell configuration file (~ means your home directory)
5. `source` reloads the configuration file to apply changes immediately
6. Without this command, you'd need to restart your terminal to see the changes

Alternative ways to write this:

```bash
# Or edit .zshrc directly using a text editor:
nano ~/.zshrc   # Add the alias line manually
source ~/.zshrc
```



---



## Check Python Installation

Having multiple Python installations isn't necessarily a problem, but it's important to understand what you're working with:

`/usr/bin/python3` is typically the system Python that comes pre-installed with macOS

`/opt/homebrew/bin/python3` is the Python version installed via Homebrew package manager

The key things to know are:

1. When you run `python3` in the terminal, your system uses the first Python it finds in your PATH environment variable
2. You can check which Python you're currently using with:

```bash
which python3
```

To avoid confusion, I recommend using virtual environments for your projects to isolate dependencies



---



## Pip3

For consistency with your Python 3 installation, you should use `pip3`. Here's why:

1. `pip3` is specifically tied to Python 3
2. Just `pip` might point to Python 2's package manager on some systems (though this is less common now)

To make sure you're using the correct pip, you can:

1. Check which pip you're using:

   ```bash
   which pip3
   ```

2. Or verify the Python version it's associated with:

   ```
   pip3 --version
   ```

**Note : **

**If you're using virtual environments (recommended), you can just use `pip` inside the activated environment as it will automatically use the correct version.**

**Pro tip:** 

**You can also install packages using Python directly to ensure you're using the right version:**

```
python3 -m pip install package_name
```

This method is the most explicit and safest way to ensure you're installing packages for the correct Python version.