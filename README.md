# Composite Wrapper
Wrapper for ASF's Local Resolution Weighted Composite python tool.
Accomplishes collecting granules for use, processing collected granules with rtc-gamma, downloading the resulting products and running the composite tool on them. Includes optional cleanup of extraneous rtc-gamma files.
## Sections
  1. Dependencies
  2. Setup
  3. Usage
  4. Jupyter Notebook Setup
  5. Jupyter Notebook Usage
  6. Potential Improvements

### Dependencies
  - conda
  - python 3.9.1

### Setup
  1. Run install.sh.
  2. Edit run.sh to include your valid earthdata credentials. Using the --password flag without it being followed by your password will result in entering your password at runtime in a secure fashion.

### Usage
  1. Activate the conda environment with:   
    `conda activate composite_wrapper_env`

  2. With conda environment activated run:  
    `python run.py -h`  
  This will show all command line arguments available and instruct on further command line usage.

  3. With or without environment activated one can also run:  
    `source run.sh`  
    run.sh should be taken as a template for building shell scripts using this wrapper.

### Jupyter Notebook Setup
  1. Complete initial setup process
  2. Run `python -m ipykernel install --user --name=composite_wrapper_env`
  3. Launch jupyter notebook and open composite_wrapper.ipynb
  4. On the top bar select 'Kernel' and then 'Change Kernel'
  5. Select 'composite_wrapper_env'
  6. Run each cell containing function or class definitions

### Jupyter Notebook Usage
  At the bottom of the notebook, functions managing each step of the process are collected into one cell. This can be run for a full demonstration of the script. Throughout the notebook these functions will be in cells immediately following the function definitions they require. These cells can be run one by one to go through each step at a controlled pace.

### Potential Improvements
  1. Integrate cleanup.py functionality into jupyter notebook
  2. HyP3 SDK's 'Batch' class does not begin downloading products until all are finished processing. This could be changed in the SDK or in how the SDK is used (i.e using the lower level 'Job' class and iteratively check each, beginning a download when one is available.)
  3. Jupyter notebook could likely use refactor, particularly by someone more familiar with writing them.
  4. Modifying the cleanup process to leave behind a list of granules used to make composites in the form of a text file. 
