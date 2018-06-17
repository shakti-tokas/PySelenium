
import csv
# Methods used


def getproperty(prop_file, prop_name):
    with open(prop_file, "rt") as p_file:
        for line in p_file:
            l = line.strip()
            if l.startswith(prop_name):
                my_value = l.split("=")[1]
                break
            else:
                continue
    return my_value


def readproperty(prop_file):
    my_prop_list = {}
    with open(prop_file, "rt") as p_file:
        for line in p_file:
            l = line.strip().split("=")
            my_prop_list[l[0]] = l[1]
    return my_prop_list


def mycsvreader(read_file):
    return csv.reader(open(read_file, newline=''), delimiter=',')


def mycsvwriter(write_file):
    return csv.writer(open(write_file, 'w', newline=''), delimiter=',')
