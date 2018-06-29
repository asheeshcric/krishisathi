import random

def create_dataset(crop_name, lower_ph, upper_ph):
	with open('cleaned_dataset.txt', 'a') as file:
		for i in range(20):
			ph = round(random.uniform(lower_ph, upper_ph), 1)
			line = crop_name + '-' + str(ph) + '\n'
			file.write(line)



def process_data(line):
	line = line.strip()
	if '-' in str(line):
		first_part, second_part = line.split('-')
		lower_ph = float(first_part[-3:])
		upper_ph = float(second_part.strip())
		crop_name = first_part[:-3].strip()
		create_dataset(crop_name, lower_ph, upper_ph)
		# print("{}: {}-{}".format(crop_name, lower_ph, upper_ph))


def read_dataset():
	with open('crop_dataset.txt', 'r') as file:
		lines = file.readlines()
		for line in lines:
			process_data(line)



if __name__ == '__main__':
	read_dataset()