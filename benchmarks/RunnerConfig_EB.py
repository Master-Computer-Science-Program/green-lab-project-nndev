from datetime import datetime
from EventManager.Models.RunnerEvents import RunnerEvents
from EventManager.EventSubscriptionController import EventSubscriptionController
from ConfigValidator.Config.Models.RunTableModel import RunTableModel
from ConfigValidator.Config.Models.FactorModel import FactorModel
from ConfigValidator.Config.Models.RunnerContext import RunnerContext
from ConfigValidator.Config.Models.OperationType import OperationType
from ProgressManager.Output.OutputProcedure import OutputProcedure as output
from Plugins.Profilers.EnergiBridge import EnergiBridge

from typing import Dict, Any, Optional
from pathlib import Path
from os.path import dirname, realpath
import statistics, math


class RunnerConfig:
    ROOT_DIR = Path(dirname(realpath(__file__)))
    timestamp_start  = None
    timestamp_end  = None

    # ================================ USER SPECIFIC CONFIG ================================
    """The name of the experiment."""
    name:                       str             = f"python_guidelines_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    """The path in which Experiment Runner will create a folder with the name `self.name`, in order to store the
    results from this experiment. (Path does not need to exist - it will be created if necessary.)
    Output path defaults to the config file's path, inside the folder 'experiments'"""
    results_output_path:        Path             = ROOT_DIR / 'experiments'

    """Experiment operation type. Unless you manually want to initiate each run, use `OperationType.AUTO`."""
    operation_type:             OperationType   = OperationType.AUTO

    """The time Experiment Runner will wait after a run completes.
    This can be essential to accommodate for cooldown periods on some systems."""
    time_between_runs_in_ms:    int             = 10000

    # Dynamic configurations can be one-time satisfied here before the program takes the config as-is
    # e.g. Setting some variable based on some criteria
    def __init__(self):
        """Executes immediately after program start, on config load"""

        EventSubscriptionController.subscribe_to_multiple_events([
            (RunnerEvents.BEFORE_EXPERIMENT, self.before_experiment),
            (RunnerEvents.BEFORE_RUN       , self.before_run       ),
            (RunnerEvents.START_RUN        , self.start_run        ),
            (RunnerEvents.START_MEASUREMENT, self.start_measurement),
            (RunnerEvents.INTERACT         , self.interact         ),
            (RunnerEvents.STOP_MEASUREMENT , self.stop_measurement ),
            (RunnerEvents.STOP_RUN         , self.stop_run         ),
            (RunnerEvents.POPULATE_RUN_DATA, self.populate_run_data),
            (RunnerEvents.AFTER_EXPERIMENT , self.after_experiment )
        ])
        self.run_table_model = None  # Initialized later

        output.console_log("Custom config loaded")

    def create_run_table_model(self) -> RunTableModel:
        """Create and return the run_table model here. A run_table is a List (rows) of tuples (columns),
        representing each run performed"""
        factor1 = FactorModel("guideline", ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G18', 'G19'])
        factor2 = FactorModel("code", [f'C{i}' for i in range(1, 11)])
        factor3 = FactorModel("treatment", ['guideline', 'no_guideline'])
        factor4 = FactorModel("run_number", [f'r{i}' for i in range(1, 21)])
        self.run_table_model = RunTableModel(
            factors=[factor1, factor2, factor3, factor4],
            repetitions = 1,
            data_columns=['execution_time', 'cpu_usage', 'memory_usage', 'average_power (Watts)', 'energy_usage'],
            shuffle = True,
        )
        return self.run_table_model

    def before_experiment(self) -> None:
        """Perform any activity required before starting the experiment here
        Invoked only once during the lifetime of the program."""
        pass

    def before_run(self) -> None:
        """Perform any activity required before starting a run.
        No context is available here as the run is not yet active (BEFORE RUN)"""
        self.timestamp_start = datetime.now()

    def start_run(self, context: RunnerContext) -> None:
        """Perform any activity required for starting the run here.
        For example, starting the target system to measure.
        Activities after starting the run should also be performed here."""
        pass       

    def start_measurement(self, context: RunnerContext) -> None:
        """Perform any activity required for starting measurements."""
        guideline = context.execute_run["guideline"]
        code = context.execute_run["code"]
        treatment = context.execute_run["treatment"]
        print(f"Starting measurement for {guideline}, {code}, {treatment}")
        
        self.profiler = EnergiBridge(target_program=f"python3 benchmarks/{guideline}/{code}/{treatment}.py",
                                     out_file=context.run_dir / f"{guideline}_{code}_{treatment}_energibridge.csv")

        self.profiler.start()

    def interact(self, context: RunnerContext) -> None:
        """Perform any interaction with the running target system here, or block here until the target finishes."""
        pass

    def stop_measurement(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping measurements."""
        _ = self.profiler.stop(wait=True)

    def stop_run(self, context: RunnerContext) -> None:
        """Perform any activity here required for stopping the run.
        Activities after stopping the run should also be performed here."""
        self.timestamp_end = datetime.now()

    def populate_run_data(self, context: RunnerContext) -> Optional[Dict[str, Any]]:
        """Parse and process any measurement data here.
        You can also store the raw measurement data under `context.run_dir`
        Returns a dictionary with keys `self.run_table_model.data_columns` and their values populated"""
        
        eb_log, _ = self.profiler.parse_log(self.profiler.logfile, 
                                                     self.profiler.summary_logfile)

        cpu_usage = [statistics.mean(filter(lambda x: not math.isnan(x), eb_log[f"CPU_USAGE_{i}"].values())) for i in range(1, 8)]
        execution_time = (self.timestamp_end - self.timestamp_start).total_seconds()
        avarage_power = statistics.mean(list(eb_log["SYSTEM_POWER (Watts)"].values()))
        energy_usage = avarage_power * execution_time
        return {
            "execution_time": execution_time,
            "cpu_usage": statistics.mean(cpu_usage),
            "memory_usage": max(eb_log["USED_MEMORY"].values()),
            "average_power (Watts)": avarage_power,
            "energy_usage": energy_usage
        }

    def after_experiment(self) -> None:
        """Perform any activity required after stopping the experiment here
        Invoked only once during the lifetime of the program."""
        pass

    # ================================ DO NOT ALTER BELOW THIS LINE ================================
    experiment_path:            Path             = None
