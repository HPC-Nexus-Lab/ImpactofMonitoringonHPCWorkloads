site_configuration = {
    "systems": [
        {
            'name': "hpcnexus_gpu",
            'descr': "HPC Nexus GPU node",
            'hostnames': [ 'admin' ],
            'partitions': [
                {
                    'name': 'default',
                    'scheduler': 'squeue',
                    'launcher': 'srun',
                    'environs': ['builtin'],
                    'resources': [
                        {
                            'name': 'l40s_gpu',
                            'options': ['--gres=gpu:nvidia_l40s:{num_gpus_per_node}']
                        }
                    ]
                }
            ]
        },
        {
            'name': "ichn_slurm",
            'descr': "Intercontenental Home Network - Slurm",
            'hostnames': [ 'slurm-login-slinky-.*' ],
            'partitions': [
                {
                    'name': 'default',
                    'scheduler': 'squeue',
                    'launcher': 'srun',
                    'environs': ['builtin'],
                    'resources': [
                        # {
                        #     'name': 'l40s_gpu',
                        #     'options': ['--gres=gpu:nvidia_l40s:{num_gpus_per_node}']
                        # }
                    ]
                }
            ]
        },
        {
            'name': "phd_slurm",
            'descr': "PhD server slurm",
            'hostnames': [ 'slurm-admin' ],
            'partitions': [
                {
                    'name': 'default',
                    'scheduler': 'squeue',
                    'launcher': 'srun',
                    'environs': ['builtin'],
                    'resources': [
                    ]
                }
            ],
            "modules_system": "envmod",
            "modules": [ "mpi/openmpi-x86_64", "mpi/mpich-x86_64" ]
        },
        # {
        #     'name': "psst_server",
        #     'descr': "Ex-PSST Server",
        #     'hostnames': [ 'vancelle' ],
        #     'partitions': [
        #         {
        #             'name': 'default',
        #             'scheduler': 'ssh',
        #             'launcher': 'ssh',
        #             'environs': ['builtin'],
        #             'sched_options': {
        #                 'ssh_hosts': [ "10.0.2.167" ],
        #             },
        #             'access': [  '10.0.2.167' ]
        #         }
        #     ]
        # },
        {
            'name': "local",
            'descr': "local",
            'hostnames': [ 'server', 'vancelle' ],
            'partitions': [
                {
                    'name': 'default',
                    'scheduler': 'local',
                    'launcher': 'mpirun',
                    'environs': ['builtin'],
                    'sched_options': {
                    },
                }
            ]
        }
    ],
    "storage": [
        {
            "enable": True,
            "sqlite_db_file": "reframe/.results/results.db",
        },
    ],
    "general": [
        {
            "report_file": "reframe/.results/run-report-{sessionid}.json",
            "topology_prefix": "reframe/.results/topology"
        }
    ],
    "environments": [
        {
            'name': 'builtin',
            'cc': 'cc',
            'cxx': '',
            'ftn': ''
        },
    ],
    'logging': [
        {
            'handlers$': [
                {
                    'type': 'stream',
                    'name': 'stdout',
                    'level': 'info',
                    'format': '%(message)s'
                },
            ],
            'handlers': [
                {
                    'type': 'file',
                    'level': 'debug2',
                    'format': '[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s',   # noqa: E501
                    'append': False
                }
            ],
            'handlers_perflog': [
                {
                    'type': 'filelog',
                    'prefix': '%(check_system)s/%(check_partition)s',
                    'level': 'info',
                    'format': ('%(check_result)s|'
                               '%(check_job_completion_time)s|%(check_#ALL)s'),
                    'ignore_keys': [
                        'check_build_locally',
                        'check_build_time_limit',
                        'check_display_name',
                        'check_executable',
                        'check_executable_opts',
                        'check_hashcode',
                        'check_keep_files',
                        'check_local',
                        'check_maintainers',
                        'check_max_pending_time',
                        'check_outputdir',
                        'check_prebuild_cmds',
                        'check_prefix',
                        'check_prerun_cmds',
                        'check_postbuild_cmds',
                        'check_postrun_cmds',
                        'check_readonly_files',
                        'check_sourcepath',
                        'check_sourcesdir',
                        'check_stagedir',
                        'check_strict_check',
                        'check_tags',
                        'check_time_limit',
                        'check_valid_prog_environs',
                        'check_valid_systems',
                        'check_variables'
                    ],
                    'format_perfvars': (
                        '%(check_perf_value)s|%(check_perf_unit)s|'
                        '%(check_perf_ref)s|%(check_perf_lower_thres)s|'
                        '%(check_perf_upper_thres)s|'
                    ),
                    'append': True
                }
            ]
        }
    ]   # end of logging
}