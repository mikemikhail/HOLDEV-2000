'''
mamikhai@cisco.com
20200111
starting constants for monitor.py
'''

from datetime import datetime

# name of database in Influxdb, production probably mdt_db, replay data is mdt_db-210321
target_db = 'mdt_db_210321'
db_user = 'telegraf'
db_pass = 'password'

model_directory = './model' # delete or rename folder to have a fresh model, or if you change layers, optimizer, etc.

# demo or replay variables. If 'is_replay' is set, 'time_shift' will be calculated based on mdt_db-nnnnnn timeframe
is_replay = True
time_shift = ' - 0d '
start_time = datetime(2021, 3, 10, 16) # replay start time y, m, d, h
time_accelerator = 5.0 # in replay mode, 1 is normal time speed, 5 is playing 10 minutes in 2 minutes

x_periods = 0

feature_mean = 0.0
feature_std = 0.0
feature_max = 0.0

fig_color = '#ffffd4'   # figures background color = eggshell

tunnel_ifs = ['tunnel-te11200', 'tunnel-te11201', 'tunnel-te13501', 'tunnel-te13502', 'tunnel-te13703', 'tunnel-te13704', 'tunnel-te17801', 'tunnel-te17802', 'tunnel-te12400', 'tunnel-te12401', 'tunnel-te12402', 'tunnel-te12403', 'tunnel-te12404', 'tunnel-te12500', 'tunnel-te12501', 'tunnel-te12502', 'tunnel-te12503', 'tunnel-te12504']

# physical_ifs = ['GigabitEthernet0/0/0/0.1224', 'GigabitEthernet0/0/0/0.1424', 'GigabitEthernet0/0/0/0.1225', 'GigabitEthernet0/0/0/0.1525']
physical_ifs = []

interval = 600 # wait time between prediction cycles, seconds
hidden_units = [72, 36, 18]     # 36, 36 is an overkill!

