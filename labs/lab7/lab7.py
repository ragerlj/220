def weighted_average(in_file_name, out_file_name):
    weighted_averages_list = []
    infile = open(in_file_name, 'r')
    for line in infile:
        all_values = line.split()
        grades = []
        weights = []
        weighted_average = 0
        for i in range(2, len(all_values), 2):
            num_weight = eval(all_values[i])
            weights.append(num_weight)
        for i in range(3, len(all_values), 2):
            num_grade = eval(all_values[i])
            grades.append(num_grade)
        for i in range(len(grades)):
            weighted_average = ((weights[i]) * (grades[i])) + weighted_average
        final_weight_average = weighted_average / 100
        weighted_averages_list.append(final_weight_average)


    total_average_weighted = (sum(weighted_averages_list) / len(weighted_averages_list))
    print(total_average_weighted, file=out_file_name)


    infile.close()


def main():
    grades = "grades.txt"
    avg = "avg.txt"
    weighted_average(grades, avg)