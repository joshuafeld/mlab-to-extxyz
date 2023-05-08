# mlab-to-extxyz

#### Converts ML AB files to the extended XYZ (extxyz) file format.

This tool can be used in three different ways that are covered in the following section. 
- Import as a package to your existing python script.
- Call the the .py script directly through CLI while providing the needed arguments.
- Call the executable tool anywhere from CLI (requires installation of the tool)
> **NOTE:** The third option works for unix systems only.    

<br>

---

## Use cases
## 1. Package import

```python
# file: my_script.py

from ml_ab_parser import convert

input_file = 'ML_AB'
output_file = 'output.extxyz'

convert(input_file, output_file)
```

This code will read data from ```ML_AB```, convert it, and save it into ```output.extxyz```.

<br>

## 2. Python script
> **NOTE:** Make sure that you are in the directory, where ```mlab-to-extxyz.py``` is located. 
#### Without output file name 
- Run ```mlab-to-extxyz.py path/to/ML_AB/file```. This will generate a ```output.extxyz``` file.

#### With output file name (optional)
- Run ```mlab-to-extxyz.py path/to/ML_AB/file my_output.extxyz```. This will generate a ```my_output.extxyz``` file.

<br>

## 3. CLI
> **NOTE:** To use the tool from the CLI, you have to install it first. Take a look at the **[installation guide](#installation-guide)** below.

#### Without output file name 
- Run ```mlab-to-extxyz path/to/ML_AB/file```. This will generate a ```output.extxyz``` file.

#### With output file name (optional)
- Run ```mlab-to-extxyz path/to/ML_AB/file my_output.extxyz``` this will generate a ```my_output.extxyz``` file.

<br>

---

## Installation guide <a id="installation-guide"></a>
> **NOTE:** Unix systems only
- First add execute permission to the install script: ```chmod +x install```.
- Run the install script: ```sudo ./install```.
- Restart your terminal.
- Ready to go.

<br>

---

## Uninstall (Also before updates) 
> **NOTE:** Unix systems only

> **_NOTE:_** If you want to update the source code, run first the uninstall script, update your repository, then run the install script again.

#### Uninstall steps
- First add execution permission to the uninstall script: ```chmod +x uninstall```.
- Run the uninstall script: ```sudo ./uninstall```.

<br>

---

## Have a problem?
In case of any problem, don't hesitate to talk to any of the authors. We will try to solve it asap! :)

- Joshua Feld mail@joshuafeld.com
- Anastasiia Dolgova anastasiiadolgova55@gmail.com
- Azer Benelhedi benelhedi.azer@gmail.com