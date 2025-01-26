# Back To Coding Python

Written by Gun Gun Febrianza



# Python on MacOS

**Development Environment Consistency** 

macOS is Unix-based, similar to Linux, which means it provides a native Unix-like environment. This is crucial because most production servers run on Linux, making the development-to-deployment process smoother. When Anisa develops on macOS, her code behaves almost identically to how it will run on the production server. Windows, on the other hand, uses a different path system and environment, which can lead to unexpected issues when deploying code. Other benefits include better docker performance & native support for many development tools.

**Package Management and Installation** 

On macOS, package management is more straightforward. With Homebrew, installing Python and related tools is as simple as `brew install python`. The package manager handles dependencies and updates seamlessly. Windows users often face more complicated installation processes, potential path issues, and may need to manually download installers or use multiple package managers like Chocolatey and pip.

Common Real-world Example:

```python
# On Windows
file_path = "C:\\Users\\Username\\Documents\\project\\file.txt"

# On macOS
file_path = "/Users/username/Documents/project/file.txt"
# or simply
file_path = "~/Documents/project/file.txt"
```

**Terminal and Command Line Tools** 

macOS comes with a powerful Terminal application that supports bash/zsh shells natively. These shells are industry-standard and make it easier to run Python scripts, manage virtual environments, and use command-line tools. While Windows has PowerShell and WSL (Windows Subsystem for Linux), they can add extra layers of complexity and potential compatibility issues.

**Built-in Python Tools** 

Many Python development tools and libraries work "out of the box" on macOS. For example:

- Data science libraries like numpy and scipy often install more smoothly
- Web development tools have better native support
- Graphics libraries like pygame tend to have fewer dependency issues
- System automation scripts are easier to integrate with the OS

**System Resource Management** 

macOS generally provides better memory management and process handling for Python applications. The Unix-based system makes it easier to:

- Monitor running Python processes
- Handle background tasks
- Manage system resources
- Debug performance issues

**Developer Community**

**More open-source tools target Unix-like systems first**

The developer community's preference for Unix-like systems, including macOS, has deep historical roots in software development culture. When developers create open-source tools, they typically develop them first on Unix-like systems because of the robust command-line interface, built-in development tools, and the similarity to production server environments. This means macOS users often get access to new tools and features first, while Windows users might have to wait for ports or face compatibility issues. For example, when Docker first launched, it was exclusively available for Linux and macOS, with Windows support coming much later, and many cutting-edge AI development tools and machine learning frameworks are initially tested and optimized for Unix-based systems.

**Stack Overflow solutions usually Unix-based**

When developers run into problems and search for solutions on Stack Overflow or other technical forums, they'll find that most answers are written with Unix-like systems in mind. The commands, file paths, and environment configurations are typically shown in Unix format. While a Windows user might need to mentally translate these solutions to their environment (changing forward slashes to backslashes, translating bash commands to PowerShell, or figuring out environment variable differences), a macOS user can often copy and paste solutions directly into their terminal. This immediate applicability saves considerable time and reduces the friction in problem-solving, especially for newer developers who are still learning to navigate technical documentation.

**Easier to follow most programming tutorials**

Following programming tutorials becomes significantly more straightforward on macOS due to its Unix foundations. Most tutorial authors use either Linux or macOS when creating their content, so their instructions align perfectly with what a macOS user sees on their screen. For instance, when a Python tutorial discusses installing packages, setting up virtual environments, or configuring development tools, the commands and processes shown will work seamlessly on macOS. This consistency extends to more advanced topics like web development, where tools like Node.js, Ruby on Rails, or Django have smoother installation and configuration processes on macOS. Beginners especially benefit from this alignment, as they can focus on learning programming concepts rather than struggling with platform-specific setup issues or command translations.

However, Windows has improved significantly with:

**Windows Subsystem for Linux (WSL)**

Windows Subsystem for Linux (WSL) has revolutionized Windows development by bringing a full Linux kernel to Windows. Developers can now run Ubuntu, Debian, or other Linux distributions directly within Windows, without the overhead of a virtual machine. This means Python developers can use Linux commands, run bash scripts, and work with Linux-first tools while keeping their Windows workflow. For example, a developer can write code in Windows' Visual Studio Code, but run it in a Linux environment through WSL, getting the best of both worlds. WSL2's improved file system performance and full system call compatibility make it nearly indistinguishable from a native Linux machine.

**PowerShell improvements**

PowerShell has evolved from a basic command prompt replacement to a powerful scripting and automation tool. The newer versions offer features like predictive IntelliSense, parallel foreach loops, and cross-platform compatibility. Python developers can now seamlessly integrate PowerShell commands into their Python scripts, making system automation much easier. For instance, you can use PowerShell commands to manage Windows services or Active Directory while processing the results in Python, something that would be much more complicated on macOS or Linux. PowerShell's object-oriented pipeline also makes it easier to work with structured data, complementing Python's data processing capabilities.

**Better package management with winget**

The introduction of winget, Windows' official package manager, has significantly improved the software installation experience. Similar to how Homebrew works on macOS, winget allows developers to install Python and other development tools through simple command-line instructions. Instead of navigating multiple websites and installers, developers can now type `winget install Python.Python.3.12` to get the latest Python version. Package updates are also streamlined with commands like `winget upgrade --all`, making system maintenance much more manageable. This addresses one of the long-standing pain points of Windows development: the fragmented software installation process.

**Visual Studio integration**

Visual Studio's integration with Python has become exceptionally robust, offering features that are hard to match on other platforms. The IDE provides intelligent code completion, real-time linting, integrated debugging, and environment management, all out of the box. The integration goes beyond basic coding support – developers can easily set up virtual environments, manage packages through a graphical interface, and debug Python applications with detailed variable inspection and call stack analysis. For data scientists, the integration with Jupyter notebooks directly in the IDE, along with variable explorers and data viewers, makes Windows a compelling platform for data analysis and machine learning work.

The choice often depends on:

1. Your team's ecosystem
2. Target deployment environment
3. Specific tools you need
4. Personal preference

----



# Homebrew

Meet Anisa R., a dedicated software developer who used to spend countless hours battling with software installations on her Mac. Before discovering Homebrew, she would juggle multiple terminal windows, manually download packages from various websites, and often run into version conflicts that would break her projects. 

Then one day, her mentor introduced her to Homebrew, and it changed her development life forever. Now, instead of the usual installation headaches, Anisa R. simply types "brew install" followed by whatever tool she needs - whether it's Python for her data analysis, Node.js for her web projects, or PostgreSQL for her databases. 

She loves how Homebrew keeps all her development tools neatly organized in one place (/opt/homebrew), away from her system files, making updates as easy as typing "brew upgrade". What used to take her hours of troubleshooting now takes just minutes, and she can focus on what she really loves: writing code and building amazing applications. 

Thanks to Homebrew, her Mac stays clean and organized, and she often tells new developers, "Homebrew is like having a super-efficient personal assistant who keeps your developer tools perfectly organized!"

So learn from above story homebrew is:

1. A package manager for macOS (and Linux)
2. Think of it as an "app store" for command-line tools and software
3. Uses the command `brew` to install, update, and manage software



---



## Benefit of Homebrew

Benefits of installing Python via Homebrew:

1. **Separation from System Python**

   - macOS comes with a system Python that Apple uses
   - Installing via Homebrew keeps your Python separate from the system version
   - Prevents conflicts with system operations
   - Safer to modify and update

2. **Easy Management**

   ```bash
   # Update Python
   brew upgrade python
   
   # Switch versions
   brew install python@3.11
   brew install python@3.12
   
   # Uninstall cleanly
   brew uninstall python
   ```

3. **Dependency Management**

   - Automatically handles required dependencies
   - Manages PATH and environment variables
   - Installs pip (Python package manager) automatically

4. **Clean Environment**

   - Installs in isolated directory (/opt/homebrew)
   - Easy to remove without affecting system
   - No need for sudo permissions

5. **Regular Updates**

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

**Understanding Each Component:**

- **`echo '...'`**:
  - The `echo` command outputs the string provided within the quotes to the terminal or another output destination.
  - In this case, it's outputting: `eval "$(/opt/homebrew/bin/brew shellenv)"`
- **`>> ~/.zshrc`**:
  - The `>>` operator appends the output from the `echo` command to the end of the file specified.
  - `~/.zshrc` is the **configuration file for the Z shell** (`zsh`), which is **executed every time a new shell session starts.**

**What Does `eval "$(/opt/homebrew/bin/brew shellenv)"` Do?**

- **`/opt/homebrew/bin/brew shellenv`**:
  - This command invokes Homebrew's `shellenv` is a subcommand provided by Homebrew designed to output the necessary environment variables required for Homebrew and its installed packages to function correctly within your shell environment.  
  - Why is `shellenv` Necessary? When you install Homebrew, it places its executables in a specific directory (e.g., `/opt/homebrew/bin`). For your system to recognize and prioritize these executables, the directory must be included in your shell's `PATH` environment variable. Additionally, other variables like `MANPATH` and `INFOPATH` need to be set to ensure that manual pages and info files are accessible.
- **`$(...)`**:
  - This is command substitution. It runs the command inside the parentheses and replaces it with the output of that command.
  - So, `$(/opt/homebrew/bin/brew shellenv)` executes the `brew shellenv` command and captures its output.
- **`eval "..."`**:
  - The `eval` command takes a string as input and executes it as if it were a shell command.
  - By wrapping the `brew shellenv` output in `eval`, the shell interprets and applies the environment variable settings immediately.

#### c. Putting It All Together:

By appending `eval "$(/opt/homebrew/bin/brew shellenv)"` to `~/.zshrc`, you're ensuring that every new Z shell session automatically sets up the necessary environment variables for Homebrew. This makes the `brew` command and any installed packages readily available without needing to set up the environment manually each time.

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

1. `/usr/bin/python3` is typically the system Python that comes pre-installed with macOS
2. `/opt/homebrew/bin/python3` is the Python version installed via Homebrew package manager

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

Anisa R, a passionate developer in her early twenties, discovered the true magic of pip3 during her first hackathon weekend. She used to spend hours manually downloading and installing Python packages, often running into version conflicts and missing dependencies that made her laptop feel like a tangled mess of code. 

One day, while building a machine learning project under a tight deadline, she learned about pip3 - Python's package installer. Her eyes lit up as she typed `pip3 install pandas scikit-learn matplotlib` and watched all the packages she needed, along with their dependencies, install perfectly in seconds. What used to take her hours now took just moments, and when her teammate asked for her project requirements, she simply ran `pip3 freeze > requirements.txt` to share a list of all her project's packages. 

Thanks to pip3, Anisa R went from being stressed about package management to focusing on what she loved most - writing code that could change the world, one project at a time.

For consistency with our Python 3 installation, we should use `pip3`. Here's why:

1. `pip3` is specifically tied to Python 3
2. Just `pip` might point to Python 2's package manager on some systems (though this is less common now)

To make sure we are using the correct pip, we can:

1. Check which pip we are using:

   ```bash
   which pip3
   ```

2. Or verify the Python version it's associated with:

   ```
   pip3 --version
   ```

**Note** : 

**If we are using virtual environments (recommended), we can just use `pip` inside the activated environment as it will automatically use the correct version.**

**Pro tip:** 

**You can also install packages using Python directly to ensure we are using the right version:**

```
python3 -m pip install package_name
```

This method is the most explicit and safest way to ensure we are installing packages for the correct Python version.



# Notes

## Echo

Overview of the `echo` Command

Applications and Use Cases of `echo`

