# Configuration file for ipcluster.

c.IPClusterEngines.engine_launcher_class = 'ipyparallel.apps.launcher.SlurmEngineSetLauncher'
c.SlurmLauncher.qos = 'janus'
c.SlurmLauncher.timelimit = '4:00:00'
# c.SlurmLauncher.account = ''
# c.SlurmLauncher.machines = ''
# c.SlurmLauncher.mem = ''
# c.SlurmLauncher.resources = ''

c.SlurmEngineSetLauncher.batch_template = """#!/bin/bash

#SBATCH --qos {qos}
#SBATCH --job-name ipengine
#SBATCH --nodes {n}
#SBATCH --ntasks {n}
#SBATCH --cpus-per-task 12
#SBATCH --time {timelimit}
#SBATCH --output {profile_dir}/log/slurm.out

mpiexec ipengine --profile-dir="{profile_dir}" --cluster-id="{cluster_id}"
"""
