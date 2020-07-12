# class Union_Find:
#     def __init__(self,N):
#         self.parent=[-1]*N
#
#     def find(self,a):
#         while self.parent[a]>=0:
#             a=self.parent[a]
#         return a
#
#     def union(self,a,b):
#         root_a=self.find(a)
#         root_b=self.find(b)
#         if(root_a==root_b):
#             return
#         size_a=-self.parent[root_a]
#         size_b=-self.parent[root_b]
#         if(size_a<size_b):
#             self.parent[root_a]=root_b
#             self.parent[root_b]=-(size_a+size_b)
#         else:
#             self.parent[root_b] = root_a
#             self.parent[root_a] = -(size_a + size_b)
#
# if __name__ == '__main__':
#     uf=Union_Find(8)
#     uf.union(4,5)
#
#     uf.union(6,7)
#     uf.union(5,7)
#     uf.union(3,7)
#     print(uf.parent)
#     # print(uf.parent)
print(1333*6)
