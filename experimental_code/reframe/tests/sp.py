import reframe as rfm
import reframe.utility.sanity as sn
from reframe.core.builtins import sanity_function, performance_function, run_before, variable
from reframe.core.launchers.mpi import SrunLauncher


@rfm.simple_test
class sp_test(rfm.RegressionTest):
    problem_size = variable(str, value='A')
    valid_systems = ['*']
    valid_prog_environs = ['*']
    parallel_launcher = 'mpirun'
    r_num_tasks = variable(int, value=49)
    num_cpus_per_task = 1

    # Build info
    build_system = 'Make'
    sourcesdir='npb/NPB3.4-MPI'
    
    @run_before('compile')
    def set_class(self):
        self.build_system.options = [ "sp", f"CLASS={self.problem_size}" ]
        # self.build_system.srcdir = 'npb/NPB3.4-MPI'

    @sanity_function
    def validate(self):
        return sn.assert_found(r'Verification\s+=\s+SUCCESSFUL', self.stdout)

    @performance_function('Mop/s')
    def mops_total(self):
        return sn.extractsingle(r'Mop/s total\s+=\s+(\S+)', self.stdout, 1, float)

    @performance_function('Mop/s')
    def mops_process(self):
        return sn.extractsingle(r'Mop/s/process\s+=\s+(\S+)', self.stdout, 1, float)
    
    @performance_function('runtime')
    def runtime(self):
        return sn.avg(sn.extractall(r'Time in seconds\s+=\s+(\S+)', self.stdout, 1, float))
    
    @run_before('run')
    def set_cpu_binding(self):
        if isinstance(self.job.launcher, SrunLauncher):
            self.job.launcher.options = ['--mpi=pmix']

    @run_before('run')
    def set_executable(self):
        self.executable = f"bin/sp.{self.problem_size}.x"
        self.num_tasks = self.r_num_tasks