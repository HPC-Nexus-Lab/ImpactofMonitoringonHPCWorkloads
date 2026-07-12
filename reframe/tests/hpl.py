import reframe as rfm
import reframe.utility.sanity as sn
from reframe.core.builtins import sanity_function, performance_function, run_before, variable
from reframe.core.launchers.mpi import SrunLauncher


@rfm.simple_test
class hpl_test(rfm.RunOnlyRegressionTest):
    valid_systems = ['*']
    valid_prog_environs = ['*']
    parallel_launcher = 'mpirun'
    r_num_tasks = variable(int, value=56)
    num_cpus_per_task = 1
    arch = variable(str, value='Linux_Intel64')
    sourcesdir = '/home/steven/Slurm/hpl/bin/Linux_Intel64'
    time_limit = '40m'

    @sanity_function
    def validate(self):
        #return sn.assert_found(r'Verification.*=.*SUCCESSFUL', self.stdout)
        return sn.all([
            sn.assert_found('End of Tests.', self.stdout),
            sn.assert_found('0 tests completed and failed residual checks', self.stdout),
            sn.assert_found('0 tests skipped because of illegal input values.', self.stdout)
        ])

    @performance_function('Gflops')
    def gflops(self):
        return \
            sn.avg(
                [ a * pow(10,b) for a,b in zip(\
                    sn.extractall(r'^W[R|C]\S+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d[\d.]+\s+([\d\.]+)e[+-][\d]+', self.stdout, 1, float), \
                    sn.extractall(r'^W[R|C]\S+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d[\d.]+\s+[\d\.]+e([+-][\d]+)', self.stdout, 1, float)
                )]
            )

    @performance_function('runtime')
    def runtime(self):
        return sn.sum(sn.extractall(r'^W[R|C]\S+\s+\d+\s+\d+\s+\d+\s+\d+\s+(\d[\d.]+)\s+\d[\d.eE+]+', self.stdout, 1, float))
    
    @run_before('run')
    def set_cpu_binding(self):
        if isinstance(self.job.launcher, SrunLauncher):
            self.job.launcher.options = ['--mpi=pmi2']

    @run_before('run')
    def set_executable(self):
        self.executable = f"/usr/bin/time /home/steven/Slurm/hpl/bin/{self.arch}/xhpl"
        self.num_tasks = self.r_num_tasks