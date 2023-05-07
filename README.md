# mlab-to-extxyz

#### Converts ML AB files to the extended XYZ (extxyz) file format.

This tool can be used in three different ways that are covered in the following secctions. 
- Import as a package to your existing python script.
- Call the the .py script directly through CLI while providing the needed arguments
- Call the executable tool anywhere from CLI (requires installation of the tool)
> **NOTE:** The third option works for unix systems only.    

---

## Use cases

## 1. Package import

<pre>
```python
# my_script.py

from ml_ab_parser import convert

input_file = 'ML_AB'
output_file = 'output.extxyz'

convert(input_file, output_file)
```
</pre>


This code will read data from ```ML_AB```, convert it and save into ```output.extxyz```.

## 2. Python script
> **NOTE:** make sure that you are in the directory, where ```mlab-to-extxyz.py``` is located. 
#### Without specifying output file name 
- Run ```mlab-to-extxyz.py path/to/ML_AB/file``` this will generate a output.extxyz file.

#### With specifying output file name (optional)
- Run ```mlab-to-extxyz.py path/to/ML_AB/file my_out_put.extxyz``` this will generate a output.extxyz file.

## 3. CLI
> **NOTE:** To use the tool from the CLI, you have to install it first. Take a look at the [installation guide](#installation-guide) below.

#### Without specifying output file name 
- Run ```mlab-to-extxyz path/to/ML_AB/file``` this will generate a output.extxyz file.

#### With specifying output file name (optional)
- Run ```mlab-to-extxyz path/to/ML_AB/file my_out_put.extxyz``` this will generate a output.extxyz file.

---

## Installation guide <a id="installation-guide"></a>
> **NOTE:** Unix systems only
- First add execution permission to the install script. ```chmod +x install```
- Run the install script. ```sudo ./install```
- Restart your terminal.
- Ready to go.

---

## Uninstall (Before updates) 
> **NOTE:** Unix systems only

> **_NOTE:_** If you want to update the source code, run first the uninstall script, update your repository, then run the install script again.

#### Uninstall steps
- First add execution permission to the uninstall script. ```chmod +x uninstall```
- Run the uninstall script. ```sudo ./uninstall```

---

## Have a problem?
In case of any problem, don't hesitate to talk to any of the authors. We will try to solve it asap! :)

- Joshua Feld mail@joshuafeld.com
- Anastasiia Dolgova anastasiiadolgova55@gmail.com
- Azer Benelhedi benelhedi.azer@gmail.com