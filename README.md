# Back To Coding Python



# Python on MacOS

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