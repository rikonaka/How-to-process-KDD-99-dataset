#
# 
# Copyright 2016 rikonaka
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
# 
# 
#

#!/usr/bin/env python
# coding=utf-8

from numpy import *
import time
import sqlite3
import threading
import os
import sys

## step 1: load data

def delete_file(path, word):
	for filename in os.listdir(path):
		fp = os.path.join(path, filename)
		if os.path.isfile(fp) and word in filename:
			os.remove(fp)

def average_distribution(n):
	h = 1
	average_open = open('db_t_%d' % n, 'r')
	for average_lines in average_open.readlines():
		insert_open = open('db_t_%d' % h, 'a')
		insert_open.writelines(average_lines)
		insert_open.close()
		h += 1
	print 'Average distribution over'
	path = os.getcwd()
	delete_file(path, 'db_t_%d' % n)

def count_the_file(filename):
	count_file = 1
	file_count = open('%s' % filename, 'r')
	for line in file_count.readlines():
		count_file += 1
	return count_file

def split_the_file_part(filename, count_file_split):
	o = 1
	p = 1
	
	#There have a variable named core
	core = 16 #I sugest you take notice of here
	
	n = core + 1
	count_for_0 = 0
	count_for_1 = count_file_split / n
	count_for_ma = {'count_for_0': '0'} #init the dict for first use
	ctl_ma = {'ctl_0': '1'}
	count_for_ma['count_for_1'] = int(count_for_1)
	
	for n_n in range(2, n, 1):
		count_for_ma['count_for_%d' % n_n] = int(count_for_1 * n_n)
		
	count_for_ma['count_for_%d' % n] = count_file_split
	print "Init split file"
	
	for n_b in range(1, n + 1):
		ctl_ma['ctl_%d' % n_b] = 1
	print "Init the ctl_numbuer"
	
	try:
		file_split = open('%s' % filename, 'r')
	except Exception, eq:
		print 'Can not open the file'
	for n_m in range(1, n + 1):
		try:
			file_name_1 = 'file_split_save_%d' % n_m
			file_name_1 = open('db_t_%d' % n_m, 'a')
		except Exception, ew:
			print 'Can not open the save file'
	
	for read_file in file_split.readlines():
		if (o >= int(count_for_ma['count_for_%d' % (p - 1)]) and o < int(count_for_ma['count_for_%d' % p])):
			ctl_name = 'ctl_%d' % p
			if (ctl_ma[ctl_name]):
				print 'split to the db_t_%d' % p
				j = open('db_t_%d' % p, 'a')
				ctl_ma[ctl_name] = 0
			j.writelines(read_file)
			o += 1
		elif (o == int(count_for_ma['count_for_%d' % p])):
			j.close()
			p += 1
			o += 1
	average_distribution(n)
	return core


def load_data_and_insert_into_database(filename, count_for_whole, i):
	count_for_insert = 1
	#print "step 1: load data..."
	try:
		file_input = open('%s' % filename, 'r')
	except Exception, e:
		print 'Can not open the file'
	
	path_load = os.getcwd()
	data_file = 'DataBase'
	data_name = '%d.db' % i
	for filename in os.listdir(path_load):
		fp = os.path.join(path_load, filename)
		if os.path.isdir(fp) and data_file in filename:
			path_fp = os.path.join(fp, data_name)
			db = sqlite3.connect(path_fp)
			db.execute("create table test (duration integer, protocol_type text, service text, flag text, src_bytes integer, dst_bytes integer, land integer, wrong_fragment integer, urgent integer, host integer, num_failed_logins integer, logged_in integer, num_compromised integer, root_shell integer, su_attempted integer, num_root integer, num_file_creations integer, num_shells integer, num_access_files integer, num_outbound_cmds integer, is_host_login integer, is_guest_login integer, count integer, srv_count integer, serror_rate integer, srv_serror_rate integer, rerror_rate integer, srv_rerror_rate integer, same_srv_rate integer, diff_srv_rate integer, srv_diff_host_rate integer, dst_host_count integer, dst_host_srv_count integer, dst_host_same_srv_rate integer, dst_host_diff_srv_rate integer, dst_host_same_src_port_rate integer, dst_host_srv_diff_host_rate integer, dst_host_serror_rate integer, dst_host_srv_serror_rate integer, dst_host_rerror_rate integer, dst_host_srv_rerror_rate integer, label text)")
			
			for line_db in file_input.readlines():
				#print 'now to insert the database'
				one_line_data = line_db.strip().split(',') #split the sentence and delete the Blank symbol
				if len(one_line_data) == 42:
					dev = (float(count_for_insert) / float(count_for_whole)) / float(i)
					print '%d/%d is done' % (count_for_insert, (float(count_for_whole) / float(i))), '%.3f' % (dev * 100) + '%'
					db.execute("insert into test values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", one_line_data)
					db.commit()
					count_for_insert += 1
				else:
					print 'Incorrect number of bindings supplied. The current statement uses 42, and there are not 42 supplied'
		

def main():
	filename = raw_input('Enter the file name: ')
	
	#step 1
	count_lines_of_file = count_the_file(filename)
	
	#step 2
	core = split_the_file_part(filename, count_lines_of_file)
	
	for y in range(1, core + 1):
		t_n = threading.Thread(target = load_data_and_insert_into_database, args=('db_t_%d' % y, count_lines_of_file, y))
		t_n.start()

if __name__ == "__main__":
	main()
