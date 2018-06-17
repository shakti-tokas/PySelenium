
import random
from com.relation import utility as ut

patrn_id_list = ['631', '218', '771', '114', '975']
patrn_num_list = ['8T', '0J', 'AT', 'RQ', 'PL']


input_file = "/opt/shazPyProjects/M2M_DataGen/input/input.properties"
out_file = "/opt/shazPyProjects/M2M_DataGen/output/account.csv"

mpid_rel_writer = ut.mycsvwriter(out_file)

input_prop_list = ut.readproperty(input_file)

print("writing account output...")

for i in range(int(input_prop_list['entity_row_count'])*3):
    pre_id = patrn_id_list[random.randint(0, 4)]
    pre_num = patrn_num_list[random.randint(0, 4)]
    temp_id = pre_id + str(int(input_prop_list['ac_id'])+i)
    temp_num = str(random.randint(0, 9)) + pre_num + str(int(input_prop_list['ac_num'])+i)
    temp_row = [temp_id, temp_num]
    mpid_rel_writer.writerow(temp_row)
    temp_row = []
