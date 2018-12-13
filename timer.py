import time
import csv


class Timer:
	def __init__(self, pathfind_algorithm):
		self.pathfind_algorithm = pathfind_algorithm
		self.start_time = None
		self.total_time = None
		self.start_pathfind_time = None

		self.path_find_times = []
		self.average_pathfind_time = None

	# Ran before every pathfind algorithm
	def start_pathfind(self):
		self.start_pathfind_time = time.time()

	# Ran after every pathfind algo
	def stop_pathfind(self):
		self.path_find_times.append(time.time() - self.start_pathfind_time)

	def start_search(self):
		self.start_time = time.time()

	def stop_search(self):
		self.total_time = time.time() - self.start_time
		self.average_pathfind_time = sum(self.path_find_times) / len(self.path_find_times)
		self.write_to_file()

	def write_to_file(self):
		print(self.pathfind_algorithm)
		print(self.average_pathfind_time)

		# with open('./data/path_find_times.txt', mode='a') as csv_file:
		# 	fieldnames = ['pathfind_algorithm', 'average_path_find_time', 'total_time']
		# 	path_find_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		# 	path_find_writer.writerow([self.pathfind_algorithm, self.total_time, self.average_pathfind_time])


		# with open('./data/path_find_times.txt', mode='a') as csv_file:
		# 	# fieldnames = ['pathfind_algorithm', 'total_time', 'average_path_find_time']
		# 	path_find_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		#
		# 	path_find_writer.writerow([self.pathfind_algorithm, self.average_pathfind_time, self.total_time])

		if self.pathfind_algorithm == 'aStar':
			with open('./data/a_star_times.txt', mode='a') as csv_file:
				# fieldnames = ['pathfind_algorithm', 'total_time', 'average_path_find_time']
				path_find_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

				path_find_writer.writerow([self.average_pathfind_time, self.total_time])

		elif self.pathfind_algorithm == 'breadthFirstSearch':
			with open('./data/bfs_times.txt', mode='a') as csv_file:
				# fieldnames = ['pathfind_algorithm', 'total_time', 'average_path_find_time']
				path_find_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

				path_find_writer.writerow([self.average_pathfind_time, self.total_time])

		elif self.pathfind_algorithm == 'dijkstra':
			with open('./data/dijkstra_times.txt', mode='a') as csv_file:
				# fieldnames = ['pathfind_algorithm', 'total_time', 'average_path_find_time']
				path_find_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

				path_find_writer.writerow([self.average_pathfind_time, self.total_time])

		elif self.pathfind_algorithm == 'dfs':
			with open('./data/dfs_times.txt', mode='a') as csv_file:
				# fieldnames = ['pathfind_algorithm', 'total_time', 'average_path_find_time']
				path_find_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

				path_find_writer.writerow([self.average_pathfind_time, self.total_time])

		elif self.pathfind_algorithm == 'bestFirstSearch':
			with open('./data/best_first_times.txt', mode='a') as csv_file:
				# fieldnames = ['pathfind_algorithm', 'total_time', 'average_path_find_time']
				path_find_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

				path_find_writer.writerow([self.average_pathfind_time, self.total_time])



