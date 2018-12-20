import random
import csv


def process_data(line):
    features = line.split(',')
    for i in range(500):
        for feature in features:
            if '\n' not in feature:
                low, high = feature.split('-')
                value = random.uniform(float(low), float(high))
                with open('datasets.csv', 'a') as dataset:
                    dataset.write(str(round(value, 2)) + ',')
            else:
                with open('datasets.csv', 'a') as dataset:
                    dataset.write(feature)


def read_data():
    with open('test.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            process_data(line)


def main():
    read_data()


if __name__ == '__main__':
    main()
