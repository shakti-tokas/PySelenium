
import random
from com.relation import utility as ut

group_file = "/opt/shazPyProjects/M2M_DataGen/input/group.csv"
entity_file = "/opt/shazPyProjects/M2M_DataGen/input/entity.csv"

out_file = "/opt/shazPyProjects/M2M_DataGen/output/member.csv"

grp_read = ut.mycsvreader(group_file)
ent_read = ut.mycsvreader(entity_file)

member_writer = ut.mycsvwriter(out_file)

for i, g_row in enumerate(grp_read):
    temp_grp_id = g_row[0]
    temp_ent_row = []
    grp_m = random.randint(2, 5)
    for j in range(1, grp_m):
        temp_ent_row.append(next(ent_read)[0])
        ran_idx = random.randint(0, 2)
        k = 1
        while k <= ran_idx:
            next(ent_read)[0]
            k += 1
    for item in temp_ent_row:
        temp_row = []
        temp_row = [temp_grp_id, item]
        member_writer.writerow(temp_row)

