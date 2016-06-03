#
# 
# Copyright 2016 isinstance <super_big_hero@sina.com>/*
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

import pandas as pd
import os

gg_list = ['gg0', 'gg1', 'gg2']

def list_way():
	col_names = ['label']
	while True:
		if os.path.exists("%d.txt" % i):
			data = pd.read_csv("%d.txt" % i, header=None, names = col_names)
			print 'Cluster ', i
			print data['label'].value_counts()
			print ''
			i += 1
		else:
			break

def split_all_part(num):
	
	gg_name = gg_list[num]
	g = open(str(gg_name), 'r')
	for i in g.readlines():
		print 'gg%d worked' % num
		i_1 = i.split(",")
		fp_save = open("%d.txt" % int(i_1[0]), "a")
		fp_save.writelines(i_1[1])
		fp_save.close()
		

def remove_txt():
	while True:
		filename = "%d.txt" % h
		if os.path.exists(filename):
			os.remove(filename)
			h += 1
		else:
			break

def main():
	for i in xrange(0, 3):
		split_all_part(i)
	list_way()
	remove_txt()

if __name__ == "__main__":
	main()
