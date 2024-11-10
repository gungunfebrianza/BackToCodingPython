# Back To Coding Python



# Python on MacOS



## Homebrew

Meet Anisa R., a dedicated software developer who used to spend countless hours battling with software installations on her Mac. Before discovering Homebrew, she would juggle multiple terminal windows, manually download packages from various websites, and often run into version conflicts that would break her projects. 

Then one day, her mentor introduced her to Homebrew, and it changed her development life forever. Now, instead of the usual installation headaches, Anisa R. simply types "brew install" followed by whatever tool she needs - whether it's Python for her data analysis, Node.js for her web projects, or PostgreSQL for her databases. 

She loves how Homebrew keeps all her development tools neatly organized in one place (/opt/homebrew), away from her system files, making updates as easy as typing "brew upgrade". What used to take her hours of troubleshooting now takes just minutes, and she can focus on what she really loves: writing code and building amazing applications. 

Thanks to Homebrew, Anisa R.'s Mac stays clean and organized, and she often tells new developers, "Homebrew is like having a super-efficient personal assistant who keeps your developer tools perfectly organized!"

So learn from above story homebrew is:

1. A package manager for macOS (and Linux)
2. Think of it as an "app store" for command-line tools and software
3. Uses the command `brew` to install, update, and manage software



---



## Benefit of Homebrew

Benefits of installing Python via Homebrew:

1. Separation from System Python

   - macOS comes with a system Python that Apple uses
   - Installing via Homebrew keeps your Python separate from the system version
   - Prevents conflicts with system operations
   - Safer to modify and update

2. Easy Management

   ```bash
   # Update Python
   brew upgrade python
   
   # Switch versions
   brew install python@3.11
   brew install python@3.12
   
   # Uninstall cleanly
   brew uninstall python
   ```

3. Dependency Management

   - Automatically handles required dependencies
   - Manages PATH and environment variables
   - Installs pip (Python package manager) automatically

4. Clean Environment

   - Installs in isolated directory (/opt/homebrew)
   - Easy to remove without affecting system
   - No need for sudo permissions

5. Regular Updates

   - Easy to get the latest Python versions
   - Security updates are readily available
   - Simple update process: `brew update && brew upgrade`



---



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

Key Learnings:

1. System Python (/usr/bin/python) is for macOS use
2. Homebrew Python (/opt/homebrew/bin/python3) is for developer use
3. They never interfere with each other
4. System updates remain safe
5. No sudo permissions needed for Python packages

This is why the clean environment provided by Homebrew is so valuable - it prevents these kinds of system-level conflicts that can be time-consuming and difficult to debug.

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

**Note** : 

**If you're using virtual environments (recommended), you can just use `pip` inside the activated environment as it will automatically use the correct version.**

**Pro tip:** 

**You can also install packages using Python directly to ensure you're using the right version:**

```
python3 -m pip install package_name
```

This method is the most explicit and safest way to ensure you're installing packages for the correct Python version.