preorders = []
postorders = []
class Node :
    def __init__ (self,data,left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    if node == None:
        return
    preorders.append(node.data[0])
    preorder(node.left)
    preorder(node.right)

def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    postorders.append(node.data[0])
    
def solution(nodeinfo):
    table = []
    for idx, (x,y) in enumerate(nodeinfo,start = 1):
        table.append([idx,x,y])
    table.sort(key = lambda x:(-x[2],x[1]))
    root = Node(table.pop(0))
    for idx,x,y in table:
        cur_node = root
        ## 왼쪽
        while(True):
            if cur_node.data[1] > x:
                ## 이미 누가 있으면
                if cur_node.left:
                    cur_node = cur_node.left
                    continue
                else:
                    cur_node.left = Node([idx,x,y])
                    break
            ## 오른쪽
            elif cur_node.data[1] < x:
                ## 이미 누가 있으면
                if cur_node.right:
                    cur_node = cur_node.right
                    continue
                else:
                    cur_node.right = Node([idx,x,y])
                    break
    preorder(root)
    postorder(root)
    return [preorders,postorders]

    
        
        



solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]],)
    
