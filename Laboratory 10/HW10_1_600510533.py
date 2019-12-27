#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# HW 10
# Problem 1
# 204113 Sec 02A

class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self,v):
        vset = set(self.neighbors)
        if v not in vset:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = dict()

    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key+str(self.vertices[key].neighbors))

def bfs(graph, start):
    
    queue = []
    queue.append(start) # แอดตัวแรกเข้าไป
    while len(queue) != 0: # ถ้าคิว ไม่ว่างให้ทำต่อไป
        front_data = queue[0] # ตัวแรก
        queue.pop(0) # ไม่มีใครเชื่อมก็ดูตัวก่อนหน้า

        for i in range(len(graph.vertices[front_data].neighbors)): # วนตามจำนวนที่อยู่ในกราฟ (A, B, C, D, ...)
            queue.append(graph.vertices[front_data].neighbors[i])

        print(front_data, end = ' ')
    print()

def main():
    
    g = Graph()
    edges = ["1A 11B 12C 13D 111E 131F 132G 1321H"]
    edges = edges[0].split(" ")
    dict_ = {} # สร้าง dict ว่างๆ
    dict_["1"] = edges[0][1] # สร้าง dict โดยให้เลข 1 = A
    for i in range(1,len(edges)): # วนตั้งแต่ตัวที่ 2 เป็นต้นไปไป
        parent = dict_[edges[i][:-2]] # เอาตั้งแต่ตัวแรกถึงก่อนก่อนตัวอักษร (46846B = เอาแค่ 4684)
        son  = edges[i][-1] # เอาตัวอักษร
        g.add_vertex(Vertex(parent)) # เพิ่มลงไปในกราฟ
        g.add_vertex(Vertex(son)) # เพิ่มลงไปในกราฟ
        g.add_edge(parent,son) # เชื่อมจุดทั้งสอง
        dict_[edges[i][0:-1]] = edges[i][-1] # ให้มันอัพค่าปทนกันต่อๆไป
        
    bfs(g, edges[0][1])

if __name__ == '__main__':
    main()