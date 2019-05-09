import csv
import pandas as pd
import matplotlib.pyplot as plot

with open('CO_Algo_input_SawTooth_auto.csv','w') as file:
    input_csv_descriptor = csv.writer(file)
    input_csv_descriptor.writerow(['date[]','clock_time[]','elapsed_time[sec]','ts_dark[V]','ts_means[V]','ts_adj[V]','ts_percent_obs[per_ft]','ts_dbm[per_m]','ts_offset[V]','ts_adj_tc[V]','ts_dbm_tc[per_m]','s_temperature[C]','smoke_obs_per_ft[per_ft]','tsl_dark[V]','tsl_means[V]','tsl_adj[V]','tg_dark[V]','tg_means[V]','tg_adj[V]','tg_percent_obs[per_ft]','tg_dbm[per_m]','tg_offset[V]','tg_adj_tc[V]','tg_dbm_tc[per_m]','tg_temperature[C]','tgl_dark[V]','tgl_means[V]','tgl_adj[V]','ionization[dBm]','ref_obs[per_ft]','ref_dbm[per_m]','ref_scatter[per_m]','ref_mic[pA]','ref_beam[uA]','extract','main_door','main_door_lock','cal_relay','motor_rpm[RPM]','smoke_alarm_activated[]','tsh_dark[V]','tsh_means[V]','tsh_adj[V]','tsh_percent_obs[per_ft]','tsh_dbm[per_m]','tt1[C]','tt2[C]','sht20_temp[C]','sht20_hum[%RH]','ref_temp[C]','ref_hum[%RH]','tc_mv[mV]','tc_na[nA]','tc_co_ppm[ppm]','tc_co_ppm_temp_corrected[ppm]','co_filt[ppm]','ref_co_target[ppm]','ref_co_actual[ppm]','ref_co_meter[ppm]','ref_co_temperature[C]','ref_co_pressure[psi]','mfc_1_mass_flow_rate[]','mfc_2_set_point[]','mfc_2_mass_flow_rate[]','als_raw[]','ref_lux[lux]','gpib_cmd','gpib_read','comment'])

    for i in range(1,69):
        input_csv_descriptor.writerow([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,1,2,3,4,5,6,7,8])
        # add date in the csv
        # add logic of mean value
        # add logic of 
        # print(i)
