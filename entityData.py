
import csv
from com.relation import utility as ut

# input output file

input_file = "/opt/shazPyProjects/M2M_DataGen/input/input.properties"
out_file = "/opt/shazPyProjects/M2M_DataGen/output/entity"
mpid_out_file = out_file + "_mpid.csv"
rel_mpid_out_file = out_file + "_rel_mpid.csv"
wcc_out_file = out_file + "_wcc.csv"
rel_wcc_out_file = out_file + "_rel_wcc.csv"

input_prop_list = ut.readproperty(input_file)

# writing mpid
print("writing mpid out file.....")

with open(mpid_out_file, 'w', newline='') as csvfile:
    point_id = int(input_prop_list['start_mpid'])
    my_writer = csv.writer(csvfile, delimiter=',')
    for i in range(int(input_prop_list['entity_row_count'])):
        temp_id = input_prop_list['prefix_mpid'] + str(point_id)
        temp_row = [temp_id, input_prop_list['mpid_type']]
        my_writer.writerow(temp_row)
        point_id = point_id + 1


# writing rel_mpid
print("writing rel mpid out file.....")

with open(rel_mpid_out_file, 'w', newline='') as csvfile:
    point_id = int(input_prop_list['start_rel_mpid'])
    my_writer = csv.writer(csvfile, delimiter=',')
    for i in range(int(input_prop_list['entity_row_count'])*2):
        temp_id = input_prop_list['prefix_mpid'] + str(point_id)
        temp_row = [temp_id, input_prop_list['mpid_type']]
        my_writer.writerow(temp_row)
        point_id = point_id + 1


# writing wccid
print("writing wccid out file.....")

with open(wcc_out_file, 'w', newline='') as csvfile:
    point_id = int(input_prop_list['start_wccid'])
    my_writer = csv.writer(csvfile, delimiter=',')
    for i in range(int(input_prop_list['entity_row_count'])):
        temp_row = [str(point_id), input_prop_list['wcc_type']]
        my_writer.writerow(temp_row)
        point_id = point_id + 1


# writing rel_mpid
print("writing rel wccid out file.....")

with open(rel_wcc_out_file, 'w', newline='') as csvfile:
    point_id = int(input_prop_list['start_rel_wccid'])
    my_writer = csv.writer(csvfile, delimiter=',')
    for i in range(int(input_prop_list['entity_row_count'])*2):
        temp_row = [str(point_id), input_prop_list['wcc_type']]
        my_writer.writerow(temp_row)
        point_id = point_id + 1

