
from com.relation import utility as ut
# input file

input_file = "/opt/shazPyProjects/M2M_DataGen/input/input.properties"
in_file = "/opt/shazPyProjects/M2M_DataGen/output/entity"
mpid_out_file = in_file + "_mpid.csv"
rel_mpid_out_file = in_file + "_rel_mpid.csv"
wcc_out_file = in_file + "_wcc.csv"
rel_wcc_out_file = in_file + "_rel_wcc.csv"

out_file = "/opt/shazPyProjects/M2M_DataGen/output/relation"
mpid_rel_file = out_file + "_mpid.csv"
wccid_rel_file = out_file + "_wccid.csv"

# mpid rel file

my_mpid_reader = ut.mycsvreader(mpid_out_file)
my_rel_mpid_reader = ut.mycsvreader(rel_mpid_out_file)

mpid_rel_writer = ut.mycsvwriter(mpid_rel_file)

input_prop_list = ut.readproperty(input_file)

'''
for mp_row in my_mpid_reader:
        print(mp_row[0])


for rel_mp_row in my_rel_mpid_reader:
        print(rel_mp_row[0])
'''

# print(my_mpid_reader.__next__()[0])
# print(my_mpid_reader.line_num)

for i in range(int(int(input_prop_list['entity_row_count'])/3)):
    for j in range(1, 4):
        main_id = next(my_mpid_reader)[0]
        for k in range(1, j+1):
            temp_row = [main_id, next(my_rel_mpid_reader)[0]]
            mpid_rel_writer.writerow(temp_row)
            temp_row = []

