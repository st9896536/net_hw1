# net_homework1
Goal:Routing with adaptive lick cost assignment

## 使用的程式語言：python

## inputs:
- Network topology
	- 請輸入全部共有幾個nodes（routers）
	- 再輸入每個nodes有幾個鄰居
	- node 1 到 node 5 的鄰居是誰？ weight是多少？（ weight=link cost ）
	- user全部輸入完 graph 就畫出來了！
- Router Requests
	- 請輸入一開始要走的node跟結束的node還有capacity demand（請直接一行就輸入所有參數 用空白鍵隔開）
	- user可以一直輸入Router Request 直到以下情形發生的時候：
		- 注意：如果Router Request的第一個參數 輸入0 X X(X表示其他非0的參數) 則就會跳出迴圈

## outputs:
- Discovered path of each route request
	- Shortest Path會印出一條最短路徑（程式以dijkestra跑）
	- Shortest Distance 會印出最短的路徑長度
	- All paths會印出所有可以走的路徑
	- Satisfaction index：印出最短的一條 / 所有可能路徑
	- 如果user輸入的demend，graph裡面的weight(link capacity)小於demand，那條路就不能走了
		- 如果起點start走不到end，則會顯示 No path to route
	