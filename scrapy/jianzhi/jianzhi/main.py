from scrapy.cmdline import execute
from datetime import datetime
import sys
import os

if __name__ == "__main__":
    cur_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dir_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(dir_path)
    os.chdir(dir_path)
    execute(
        [
            "scrapy",
            "crawl",
            "spider_1",
            "-o",
            "result/result_{}_{}.json:json".format('current_missions', cur_datetime),
            
        ]
    )
    # execute(
    #     [
    #         "scrapy",
    #         "crawl",
    #         "spider_2",
    #         "-o",
    #         "result/result_{}_{}.json:json".format('future-missions', cur_datetime),
            
    #     ]
    # )
    # execute(
    #     [
    #         "scrapy",
    #         "crawl",
    #         "spider_3",
    #         "-o",
    #         "result/result_{}_{}.json:json".format('concept-missions', cur_datetime),
            
    #     ]
    # )
    # execute(
    #     [
    #         "scrapy",
    #         "crawl",
    #         "spider_4",
    #         "-o",
    #         "result/result_{}_{}.json:json".format('past-missions', cur_datetime),
            
    #     ]
    # )