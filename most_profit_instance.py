import sys
import re

# Empty list to store the data
most_proftable = []


def make_all_the_calculation():
    with open(sys.argv[1]) as input_1:
        for line in input_1:
            hvm = re.findall(r'HVM', line)
            if hvm:
                instance = line.split(',')[0]
                vcpu = line.split(',')[1]
                with open(sys.argv[2]) as input_2:
                    for lines in input_2:
                        if instance in lines:
                            memory = lines.split(',')[1]
                            cost = lines.split(',')[2]
                            #cost_benefit = (((MEMORY / m) + VCPU)/COST)
                            m = (3.75*float(cost))
                            cost_benefit = (((float(memory)/float(m))+float(vcpu))/float(cost))
                            most_proftable.append([cost_benefit,instance])

def most_proftable_list():
    for line in sorted(most_proftable,reverse=True):
        print(line[1])

if __name__ == "__main__":
    make_all_the_calculation()
    most_proftable_list()
