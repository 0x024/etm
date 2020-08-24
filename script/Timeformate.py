import datetime
import time



def order_time_formate(o_time):
	str(o_time)
	n_time=datetime.datetime.strptime(o_time,"%Y%m%d")	
	return n_time
	print (n_time)
def train_time_formate(o_time):
	n_time=datetime.datetime.strptime(o_time,"%Y%m%d%H:%M")
	return n_time
