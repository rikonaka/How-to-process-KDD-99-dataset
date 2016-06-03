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
re_list = ['re0', 're1', 're2']
la_list = ['la0', 'la1', 'la2']
gg_list = ['gg0', 'gg1', 'gg2']

def get_lines_count(num):
	fp = la_list[num]
	get_op = open(str(fp), "r")
	return int(len(get_op.readlines()))
	get_op.close()

def return_re_first(lines_num, fp):
	re = open(fp, "r")
	local_num = 1
	for i in re.readlines():
		if (lines_num == local_num):
			shit = i.split(",")
			return shit[0]
		else:
			local_num += 1
	re.close()

def return_la_first(lines_num, fp):
	la = open(fp, "r")
	local_num = 1
	for i in la.readlines():
		if (lines_num == local_num):
			return i
		else:
			local_num += 1
	la.close()
	
def insert_into_gg(list_num):
	filename_1 = gg[list_num]
	gg = open(str(filename_1), "a")
	
	fp_re = re_list[list_num]
	fp_la = la_list[list_num]
	
	get_l = get_lines_count(list_num)
	for i in range(1, get_l + 1):
		print i,'/', get_l, ' ', filename_1
		re_string = str(return_re_first(i, str(fp_re)))
		la_string = str(return_la_first(i, str(fp_la)))
		insert_string = re_string + "," + la_string
		gg.writelines(insert_string)
	gg.close()

def main():
	for list_num in xrange(0, 3):
		insert_into_gg(list_num)

if __name__ == "__main__":
	main()
