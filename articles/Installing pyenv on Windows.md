# Installing pyenv on Windows

The original pyenv is designed for Unix-based systems, but there's a Windows alternative called pyenv-win. Here's how to install it:

```
pip install pyenv-win --target $HOME\.pyenv
```



## After Installation

After installing, you'll need to set up environment variables:

Add these to your PATH:

- `%USERPROFILE%\.pyenv\pyenv-win\bin`
- `%USERPROFILE%\.pyenv\pyenv-win\shims`

Set these environment variables:

- `PYENV` = `%USERPROFILE%\.pyenv\pyenv-win\`
- `PYENV_HOME` = `%USERPROFILE%\.pyenv\pyenv-win\`



We can use PowerShell commands:

```powershell
[System.Environment]::SetEnvironmentVariable('PYENV', $env:USERPROFILE + "\.pyenv\pyenv-win\", 'User')
[System.Environment]::SetEnvironmentVariable('PYENV_HOME', $env:USERPROFILE + "\.pyenv\pyenv-win\", 'User')
[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', 'User'), 'User')
```

