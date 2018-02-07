import re
[l.strip() for l in open('/home/databiz41/scrapy_projects/mercedes/mercedes/save_all_cars_info.csv').readlines()]
re.search(r"detail(.*?)/'", l).group(1)

#f1 = open('/home/databiz41/scrapy_projects/mercedes/mercedes/save_all_cars_info.csv', 'r')
#f2 = open('/home/databiz41/scrapy_projects/mercedes/mercedes/save_all_cars_info_sorted.csv', 'w')
#for line in f1:
#        f2.write(line.replace("sisli", "sisliiii"))
#        f1.close()
#        f2.close()
