import re
#[l.strip() for l in open('/home/databiz41/scrapy_projects/mercedes/mercedes/save_all_cars_info.csv').readlines()]
[l.strip() for l in open('/home/databiz41/scrapy_projects/mercedes/mercedes/all_cars_details.csv').readlines()]
#for l in open('/home/databiz41/scrapy_projects/mercedes/mercedes/all_cars_details.csv').readlines():
 #   l.strip()
cc = re.search(r"detail': u'(.*?)/'", l).group(1)
print cc

#f1 = open('/home/databiz41/scrapy_projects/mercedes/mercedes/all_cars_details.csv', 'r')
#f2 = open('/home/databiz41/scrapy_projects/mercedes/mercedes/save_all_cars_info_sorted.csv', 'w')
#for line in f1:
#         #print line
#         cc = re.search(r"detail': u'(.*?)/'", line).group(1)
 #        f2.write(c)#.replace("sisli", "sisliiii"))
 #        f1.close()
 #        f2.close()
