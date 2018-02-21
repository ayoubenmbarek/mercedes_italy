#!/bin/bash

cd /home/databiz41/scrapy_projects/mercedes/mercedes/
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl mercedes_italy15_02_new -o /home/databiz41/scrapy_projects/mercedes/mercedes/nnv333.csv
