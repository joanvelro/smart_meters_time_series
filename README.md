## Project structure       

```
├── README.md                          # this file
├── LICENSE                            # license document
├── MAKEFILE                           # to automate Python projects
├── requirements.txt                   # library requisites  `pip freeze > requirements.txt`
├── environment.yml                    # virtual environment `conda env create -f environment.yml`
├── config.ini                         # default configuration `config = iniFile(config.ini)`
│
│
├── build                # file to generate containers, images or automatization of the deployment
├── data                 # data for unitary test and user example             
├── docs                 # documentation generated [Sphinx Tool])          
├── libs                 # code of the building block use (models included)
├── notebooks            # examples and how-to-use guide/tutorial
├── references           # bibliografy and used examples (not upload to repo)
├── venv                 # virtual environment (not upload to repo)
├── logs                 # where log.txt is sotred with the execution details
│
├── src                  # specific code of the project
│   ├── __init__.py      # for submodules importation
```


