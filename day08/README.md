# python爬虫练习
## shell爬虫
```bash
scrapy shell "https://example.com"
```
### 获取网页中各个元素的值
*获取网页标题*
```shell
response.css('title')
```
*在标题中提取文本，这里返回的是一个列表*
```shell
response.css('title::text').getall()
```
*这样写返回第一个结果*
```shell
response.css('title::text').get()
```
*返回第n个结果*
```shell
response.css('title::text')[0].get()
```
