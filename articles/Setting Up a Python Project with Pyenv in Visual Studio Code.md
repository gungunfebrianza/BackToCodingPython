# Setting Up a Python Project with Pyenv in Visual Studio Code

Here's a step-by-step guide to create a new Python project using pyenv on your Mac, and execute the vector code in Visual Studio Code:

## Step 1: Create a new project directory

1. Open Terminal in Visual Studio Code (press `Ctrl+` `` or go to Terminal → New Terminal)

2. Create and navigate to your project directory, here is an example:

   ```bash
   mkdir vector_math_project
   cd vector_math_project
   ```

   

## Step 2: Set up a Python version with pyenv

1. List available Python versions:

   ```
   pyenv install --list
   ```

2. Install a specific Python version (if not already installed):

   ```
   pyenv install 3.10.0
   ```

3. Set the local Python version for this project:

   ```bash
   pyenv local 3.10.0
   ```

This creates a `.python-version` file in your project directory, ensuring this Python version is used when you're in this directory.



## Step 3: Create a virtual environment

1. If you haven't already installed the pyenv-virtualenv plugin:

   ```bash
   brew install pyenv-virtualenv
   ```

   And add this to your shell configuration (if not already there):

   ```bash
   echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc  # For zsh
   # OR
   echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile  # For bash
   ```

   Restart your terminal or source your shell configuration:

   ```bash
   source ~/.zshrc  # For zsh
   # OR
   source ~/.bash_profile  # For bash
   ```

2. Create a virtual environment with pyenv-virtualenv using the Python version you selected:

   ```bash
   pyenv virtualenv 3.10.0 vector-math-env
   ```

3. Activate it manually whenever needed:

   ```bash
   pyenv activate vector-math-env
   ```

4. Or set it as the local virtual environment for the project directory:

   ```
   pyenv local vector-math-env
   ```

   This approach automatically activates the environment when you enter the directory. 

5. Verify that you're using the correct Python version and environment:

   ```bash
   python --version
   which python
   pip --version
   ```

   

## Step 4: Install required packages

Install NumPy for vector operations:

```bash
pip install numpy
```



## Step 5: Create a Python file for vector operations

1. Create a new file:

   ```bash
   touch vector_operations.py
   ```

2. Open the file in VS Code:

   ```bash
   code vector_operations.py
   ```

3. Paste the vector code into the file:

   ```python
   import numpy as np
   
   # Create vectors
   row_vec = np.array([3, -2, 5])
   col_vec = np.array([[3], [-2], [5]])
   
   # Display the vectors
   print("Row vector:\n", row_vec)
   print("Column vector:\n", col_vec)
   
   # Transpose operations
   print("Transposed row vector (column vector):\n", row_vec.reshape(-1, 1))
   print("Transposed column vector (row vector):\n", col_vec.T)
   
   # Vector operations
   # Dot product
   dot_product = np.dot(row_vec, col_vec.flatten())
   print("Dot product:", dot_product)
   
   # Vector scaling
   scaled_vector = 2 * row_vec
   print("Scaled vector:", scaled_vector)
   
   # Vector addition
   sum_vectors = row_vec + np.array([1, 1, 1])
   print("Vector addition:", sum_vectors)
   
   # Vector magnitude (norm)
   magnitude = np.linalg.norm(row_vec)
   print("Vector magnitude:", magnitude)
   ```

   

## Step 6: Configure VS Code for your Python environment

1. Select the Python interpreter in VS Code:
   - Press `Cmd+Shift+P` to open the command palette
   - Type "Python: Select Interpreter" and select it
   - Choose the interpreter from your virtual environment (it should include 'venv' in the name)
2. Optionally, set up a launch configuration:
   - Press `Cmd+Shift+P` again
   - Type "Python: Create Debug Configuration" and select it
   - Choose "Python File" as the debug configuration



## Step 7: Run your code

You have several options to run the code:

1. Using the terminal:

   ```
   python vector_operations.py
   ```

2. Using VS Code's Run button:

   - Click the "Run" (play) button in the top-right corner of the editor
   - Or press `F5` to run with debugging

   Using the VS Code Python extension:

   - Click the "Run Python File" button (green triangle) in the top-right corner of the editor



## Step 8: Create additional examples (optional)

Create more files to explore different vector operations:

```bash
touch advanced_vectors.py
```

Then add more advanced examples to this file, such as:

```python
import numpy as np
import matplotlib.pyplot as plt

# More vector examples
# Vector cross product (only in 3D)
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
cross_product = np.cross(v1, v2)
print("Cross product:", cross_product)

# Simple vector visualization
plt.figure(figsize=(10, 6))
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2')
plt.xlim(-1, 6)
plt.ylim(-1, 6)
plt.grid()
plt.legend()
plt.title('Vector Visualization')
plt.savefig('vector_plot.png')  # Save the plot
plt.show()  # Display the plot
```

To run this, you'll need matplotlib:

```bash
pip install matplotlib
```



## Step 9: Deactivate the virtual environment when done

When you're finished working on your project:

```
deactivate
```

This returns your terminal to the global Python environment.



## Additional Notes

- To save your dependencies for future reference:

  ```bash
  pip freeze > requirements.txt
  ```

- To install from requirements.txt in the future:

  ```bash
  pip install -r requirements.txt
  ```

- You can create a `.gitignore` file to exclude the virtual environment from version control:

  ```bash
  echo "venv/" > .gitignore
  ```





----





----



# Debugging

In Visual Studio Code, there are two primary ways to debug Python code: the "Debug Module" and "Debug Python File" options. Here's how they differ:

## Debug Python File

This option runs and debugs the currently active Python file directly. When you select "Debug Python File":

1. VSCode executes the specific file you're currently editing
2. The file is run as a standalone script (using `python filename.py`)
3. The debugger attaches to this process
4. The execution starts from the top-level code in that file

This is best for debugging single scripts or when you want to test one specific file in isolation.

## Debug Module

This option uses Python's `-m` flag to run a Python module as a script. When you select "Debug Module":

1. VSCode executes the module using `python -m module_name`
2. The module is imported and executed as if you ran it from the command line as a module
3. Python searches for the module in the current directory and then in the Python path
4. This approach respects package structures and relative imports

The "Debug Module" option is particularly useful when:

- Working with packages that have complex import relationships
- Debugging code that relies on relative imports
- Working with modules that are part of a larger package structure

## Key Practical Differences

- **Import Resolution**: Debug Module handles relative imports better within packages
- **Working Directory**: Debug Module uses the project root as the working directory, while Debug File uses the file's directory
- **Module Search Path**: Debug Module includes the project root in the module search path

If you're running into import errors when debugging your Python code, switching between these two options often resolves the issue.
