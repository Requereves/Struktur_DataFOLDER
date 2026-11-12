# Materi: Node
# Menjalankan: python3 01_node.py

class Node:
    def __init__(self, data):
        self.info = data
        self.next = None
        self.prev = None


if __name__ == "__main__":
    P = Node(10)

    print("Data node :", P.info)
    print("P.prev    :", P.prev)
    print("P.next    :", P.next)
