# Desafio Tunts

## Depedencies
### First create a virtual environment (venv) using one of this following commands:
>"python -m venv venv_name" // **Example:** "python -m venv Desafio_Tunts"  
>"python3 -m venv venv_name" // **Example:** "python3 -m venv Desafio_Tunts"

&nbsp;

### Then activate it with the following command: 
>**Windows**  
>**PowerShell**: "path_to_venv\Scripts\activate.ps1" // **Example:** "E:\Venvs\Desafio_Tunts\Scripts\activate.ps1"
>If any "Execution Policies" erros happen open PowerShell with admin mode and using the following command: **"Set-ExecutionPolicy -ExecutionPolicy RemoteSigned"**  
>**CMD**: "path_to_venv\Scripts\activate" // **Example:** "E:\Venvs\Desafio_Tunts\Scripts\activate"

&nbsp;

> **Linux or MacOs**  
> "source path_to_venv/bin/activate" // **Example:** "source E:/Venvs/Desafio_Tunts/bin/activate"

&nbsp;

### After avoiding venv, we will need to download all project dependencies, for that we use pip, which is a Python package management system, it comes in the default python installation. The command is very simple, first you need to be inside the main folder where the file "requirements.txt" is located. After that just run: 
>"pip install -r requirements.txt"

&nbsp;

### After everything is ready just run the code with one of this following python commands:
>"python -u path_to_files/main.py" // **Example:** "python -u E:\Projetos\Desafio_Tunts\main.py"  
>"python3 -u path_to_files/main.py" // **Example:** "python3 -u E:\Projetos\Desafio_Tunts\main.py"

_Observation: in **Windows** we use the backslash (" \\ ") to identify the file_path diferently from **Linux** or **MacOs** where we use the normal bar (" / ")._

&nbsp;

## Bonus Features
>* Support for add or remove students from spreadsheet;
>* Exception treatments;
>* Log 100% functional and interactive;