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

import os
import pandas as pd

col_name = ['label']

def list_way():
    
    """ Notice about above number"""
    
    for i in range(1, 11):
        if os.path.isfile("temp/%d.txt" % i):
            data = pd.read_csv("temp/%d.txt" % i, names = col_name)
            print 'Cluster ', i
            print data['label'].value_counts()
            print ''
        else:
            print 'Cluster %d is Null' % i

def split_all_part(fp):
    
    fp_fp = open(fp, 'r')
    for i in fp_fp.readlines():
        i_1 = i.split(",")
        fp_0 = open("temp/%d.txt" % int(i_1[0]), "a")
        fp_0.writelines(i_1[1])
        fp_0.close()

def get_lines_count(filename):
    get_op = open(filename, "r")
    return int(len(get_op.readlines()))
    get_op.close()
	
def insert_into_gg(num):
    file_save_name = 'gg%d' % num
    gg = open(file_save_name, "a")
    
    fp_re = 're%d' % num
    fp_la = 'la%d' % num
    
    get_number = get_lines_count(fp_re)
    re = open(fp_re, "r")
    la = open(fp_la, "r")
    for i in range(1, get_number + 1):
        print i,'/', get_number
        re_string = re.readline().split(',')[0]
        la_string = la.readline()
        insert_string = re_string + "," + la_string
        gg.writelines(insert_string)
    gg.close()
    la.close()
    re.close()

def then_all():
    IOP = True
    l = 0
    while IOP:
        fp = 're%d' % l
        if os.path.exists(fp):
            insert_into_gg(l)
            l += 1
        else:
            IOP = False
            
    DEF = True
    k = 0
    if os.path.isdir('temp'):
        os.rmdir('temp')
        os.mkdir('temp')
    else:
        os.mkdir('temp')
    while DEF:
        fp = 'gg%d' % k
        if os.path.exists(fp):
            print 'Now use', fp
            split_all_part(fp)
            k += 1
        else:
            DEF = False
    list_way()


def main():
    then_all()

if __name__ == "__main__":
    main()
