# DEProjectScrapySpider 
### Knowledged
* Spark (PySpark)
* Scrapy
* Pandas
* SQL (DDL & DML)

### Newegg Data

* Mô tả | collect và thống kê các thông tin tại danh mục trên website bán hàng sản phẩm card đồ họa từ [source](https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48)
* Flowchart describe the crawl data process
![image](https://github.com/QuocAnh171/DEProjectScrapySpider/assets/74640069/643bc6c9-56a4-43e4-842c-dfa84f0284e2)


* Scrapy | crawl data from the website yêu cầu ([newegg](https://github.com/QuocAnh171/DEProjectScrapySpider/tree/master/newegg))
* Data output (.csv) | ./newegg/data.csv
* Pandas | build to DataFrame
* PySpark & Databricks | [xử lý data và load lên database được tạo sẵn bằng AWS RDS](https://github.com/QuocAnh171/DEProjectScrapySpider/blob/master/newegg_data/newegg_data_ETL.ipynb)

* Thông tin AWS RDS để kiểm tra dữ liệu:

  host = 'database-2.cmfq2wbb1ceg.ap-southeast-1.rds.amazonaws.com'
  
  post = '5432'
  
  user = 'postgres'
  
  password = 'quocanh1711'

  table_1 = 'ahmad_schema_pyspark.newegg_data'
  
  table_2 = 'ahmad_schema_pyspark.Brand_Count'
