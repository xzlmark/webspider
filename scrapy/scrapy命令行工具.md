# scrapy命令行工具

1、scrapy -h

​	查看所有可用命令

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  check         Check spider contracts
  crawl         Run a spider
  edit          Edit spider
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  list          List available spiders
  parse         Parse URL (using its spider) and print the results
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

2、scrapy <command> -h

​	查看所执行命令的用法

注意：scrapy共有两种类型的命令，一种是全局命令，一种是项目用的命令

​	全局命令：

​	startproject  :创建项目,格式： scrapy startproject 项目名

​	genspider:

​			![1560590061775](.\image\genspider.png)

​	settins:

​			![1560591399620](.\image\settings.png)

​	runspider:

​		![1560591477942](.\image\runspider.png)

​	shell:

​			![1560591208369](.\image\shell.png)

​	fetch:

​	![1560590831617](.\image\fetch.png)

​	view:

​		![1560591062567](.\image\view.png)

​	version

​	项目用的命令

​	crawl:

​				![1560590254263](.\image\crawl.png)

​	check:

​				![1560590377241](.\image\check.png)

​	list:

​		![1560590506395](.\image\list.png)

​	edit:

​			![1560590665125](.\image\edit.png)

​	parse:

​				![1560591312356](.\image\parse.png)

​	bench

