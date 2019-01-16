#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:53:54 2017

@author: Rong
"""

#graph = {'1':{'2':10,'3':3},'2':{'3':1,'4':2,'5':2},'3':{'2':4,'4':8,'5':2},'4':{'5':7},'5':{'2':10,'4':9}}


def dijkestra(graph,start,end,demend):
    graph2 = graph.copy()
    shortest_dist = {} #開一個空的dictionary存最短距離
    parent = {} #記錄各個點在最短路徑上的父親是誰
    unseenNodes = graph2 #還沒拜訪過的node們
    inf = 999999 #將還沒拜訪過的distance先設無限大
    path = [] #存放未來最短路徑的path
    
    for i in unseenNodes:
        shortest_dist[i] = inf
    shortest_dist[start] = 0 #將start的最短路徑先設成0
    
    while unseenNodes: #loop一直到unseenNodes裡面每個node都拜訪過才跳出迴圈
        minNode = None
        for i in unseenNodes: #要挑出有最小的distance來當我第一個要走的node
            if minNode == None: #best case
                minNode = i 
            elif shortest_dist[i] < shortest_dist[minNode]: #如果有出現distance更小的則switch
                minNode = i
    
       #選好minNode之後更新shortest_dist
        for neighbor,weight in graph[minNode].items(): 
            
            if weight + shortest_dist[minNode] < shortest_dist[neighbor] and weight >= demend:
                shortest_dist[neighbor] = weight + shortest_dist[minNode]
                parent[neighbor] = minNode
                if weight < demend: #如果weight(link capacity)小於 demend 這條就不能走
                    del parent[neighbor] #就把這個neighbor node 紀錄刪掉
                    parent[neighbor] = minNode
                    shortest_dist[neighbor] = shortest_dist[neighbor] - weight 
        #print(parent) #可以知道目前所有node的parent是誰
            
        unseenNodes.pop(minNode) #把已經跑完的minNode從unseenNode裡面pop掉   
    
    current = end #將currentnode 設成 end    
    while current != start:
        
        current_check = current in parent.keys() #檢查current node有沒有在parent key裡面
        start_check = start in parent.values() #檢查start node有沒有在parent value裡面
        if current_check == False or start_check == False: #如果其中有一個不符合表示沒有路可以走了
            print('no path to route') 
            break
        
        
        path.insert(0,current) #把目前最短路徑insert進去path (會加在path最前面)
        current = parent[current]
        #print(current)
      
    path.insert(0,start)
    if shortest_dist[end] != inf:
        print("Shortest Distance: " + str(shortest_dist[end]))
        print("Shortest Path: " + str(path))
        print("All paths: ",Findallpath(graph,start,end))
        #print("Paths numbers: ",len(Findallpath(graph,start,end)))
        print("Satisfaction index: ", 1 / len(Findallpath(graph,start,end)))   
    
    
def Findallpath(graph,start,end,path=[]): #找到start到destination的所有路徑
    path = path + [start] #把起點加到path裡面
    if start == end: 
        return [path]
    if start not in graph: #如果start不再graph裡面
            return [] #回傳空的list
    paths = []
    for i in graph[start]: #graph dictionary裡面的第一個value{'2':10,'3':3}
        if i not in path: #i是graph第一排裡面的key
            newpath = Findallpath(graph,i,end,path) 
            for j in newpath:
                paths.append(j)
    return paths
    

#dijkestra(graph,'1','5',2)

"""
routers = int(input("router numbers(please input 1 ~ 5): "))

graph = {}
for i in range(routers):
    value = {}
    num = int(input('how many neighbors does the node %d have: ' %(i+1)))
    for j in range(num):       
        neighbor = input('Please enter the neighbor of node %d : ' %(i+1))
        link_cost = int(input('Please enter the link cost: '))
        value.update({neighbor:link_cost})
    tmp = str(i + 1)
    graph[tmp] = value
"""
    
#print(Findallpath(graph,start,end,path=[]))
# router 只能走出去不能走回來（例如：起點 1 終點 4,但不能起點 4 終點 1）
str_tmp = input('Router Request:'  ) #請老師跟助教打 source destination 跟 demend 用空白鍵隔開～～
x = str_tmp.split() #將 user的input分割成：
start = x[0] #source router
end = x[1]  #destination router
demend = int(x[2]) #capacity demand
dijkestra(graph,start,end,demend)


while start != '0':     
    str_tmp = input('Router Request:'  ) #老師你如果輸入0 X X就會跳出迴圈                           
    x = str_tmp.split()
    start = x[0] #第二次的start
    end = x[1]
    demend = int(x[2])
    dijkestra(graph,start,end,demend)
    #print("All paths:",Findallpath(graph,start,end))
