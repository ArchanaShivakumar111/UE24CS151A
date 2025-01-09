#Display Movies
import csv
def loadm(file_path):
	movies=[]
	with open(file_path,mode='r') as file:
		reader=csv.DictReader(file)
		for row in reader:
			#these conversions are required because it will be taken as string by default
			#convert rating to float
			row['rating']=float(row['rating'])
			#convert year to int
			row['year']=int(row['year'])
			movies.append(row)
	return movies
file_path='BananaTest.csv'
movies=loadm(file_path)
print("value=",movies)