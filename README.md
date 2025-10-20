# Green Lab project - NNDEV
**An Empirical Study on the Energy Usage and Performance of
Python code using Python Energy Efficiency Guidelines**

This repository contains source code, data analysis script and results of this experiment.

## Experiment goal
This experiment is intended to evaluate energy consumption and performance benefits when using [Python Energy Efficiency Guidelines](https://github.com/S2-group/icse-2026-llm-ee-rep-pkg/blob/main/3.2%20Green%20guidelines%20elicitation/Guidelines.pdf) collected by [S2 research group](https://github.com/S2-group). Main focus is two guideline families: Code Optimization and Function Calls.

Key metrics for this experiment are Energy Usage (in Joule), Memory Usage (in Bytes), CPU Usage (in percentage) and execution time (in second).


## Guidelines

| Family          | Guideline | Description |
|-----------------|-----------|-------------|
| Code Optimization | G1  | When there are multiple occurrences of the same expression, assign it to a variable and use the variable. |
|                 | G2  | Avoid redundant operations in sorting already sorted or semi-sorted collections. |
|                 | G3  | Use loop optimization techniques (e.g., loop unrolling, loop unswitching, early termination) to improve performance, such as storing the loop end condition in a variable. |
|                 | G4  | Use short-circuit versions of logical operators where the second argument of a logical expression is evaluated only if the first argument is insufficient to determine the value of the expression. |
|                 | G5  | When high-precision computation is not needed, use approximate computations. |
|                 | G6  | Avoid storing or saving data that has already been computed, saved, or is unnecessary. For example, don't recompute data that is available in a local variable, or avoid having variables only for debugging purposes. |
| Function Calls  | G18 | Use memoization to avoid repeated execution of expensive pure functions. |
|                 | G19 | Reduce function calls to minimize overhead; use static methods and inline code to avoid lookup delays. |

## Repository structure
```
green-lab-project-nndev/
│
├── benchmarks/
│   ├── benchmarks_complexity/  # Benchmark complexity records
│   ├── experiments             # Contain result logs and run table
│   └── G<x>/                   # Guideline x
│        ├── C<y>/              # Code y
│        │   ├── guideline.py    # Guideline-applied version of the code
│        │   └── no_guideline.py # No-guideline-applied version of the code
│        └── config.py          # Arguments of all code in this guideline
│
├── data-analysis/
│   ├── ... 
│   ├── figures                 # visualization results are saved here
│   └── main.Rmd                # Main data analysis script
│
├── experiment-runner/          # Containing experiment runner implementation
│   ├── ...
│   └── requirements.txt        # required packages for experiment runner
│
├── lizard/                     # Code complexity analyzer
├── .gitignore
└── README.md

```

## Run Code

### Installation
- Install EnergiBridge from the instructions [here](https://github.com/tdurieux/EnergiBridge).
- Verify installation by running `energibridge -h`
- Python version 3.11
- Create and activate Python virtual environment:
```
python3 -m venv <your-environment-name>
source ./<your-environment-name>/bin/activate
```
- Install packages: `pip3 install -r experiment-runner/requirements.txt`

### Run experiment
- Experiment Runner configuration file for this experiment is located in `benchmarks/RunnerConfig_EB.py`
- Change factors according to use
```
factor1 = FactorModel("guideline", ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G18', 'G19'])
factor2 = FactorModel("code", [f'C{i}' for i in range(1, 11)])
factor3 = FactorModel("treatment", ['guideline', 'no_guideline'])
factor4 = FactorModel("run_number", [f'r{i}' for i in range(1, 21)])
```
- Adjust table model with `factors, repetition, exclude_combinations, data_columns, shuffle` to select factors, repetition, combinations want to excule, data columns in table model and shuffle option.
```
self.run_table_model = RunTableModel(
    factors=[factor1, factor2, factor3, factor4],
    repetitions = 1,
    exclude_combinations=[
        {factor1: ['G1']},                   # all runs of G1 will be excluded
        {factor1: ['G2'], factor2: ['C2']},  # all runs of G2/C2 will be excluded
    ],
    data_columns=['execution_time', 'cpu_usage', 'memory_usage', 'average_power (Watts)', 'energy_usage'],
    shuffle = False,
)
```
- Update path and name of folder to save results:
```
name:                       str             = <your-folder-name>
results_output_path:        Path            = <your-parent-folder-name>
```
- Update time between run
```
time_between_runs_in_ms:    int             = 2000
```
- Run command from base directory
```
python3 experiment-runner/ benchmarks/RunnerConfig_EB.py
```
After all runs are finished, results can be found in the folder that you indicated.

### Troubleshoot
There might be cases when you need to use administrator right to execute the experiment.
```
sudo python3 experiment-runner benchmarks/RunnerConfig_EB.py
```
After the experiments are finished, you need to grant your current users right to access the result directory.
```
sudo chown -R <your-current-username> benchmarks/<your-parent-folder-name>
```

## Run data analysis
### Installation
- R
- Positron
### Run analysis
- Run block by block in the `.Rmd` file to see the result, all graphs are saved in `data-analysis/figures`.