def modifyList(task, list):
    if task.startswith('insert'):
        list.insert(int(task.split(" ")[1]), int(task.split(" ")[2]))
    elif task.startswith('print'):
        print list
    elif task.startswith('remove'):
        list.remove(int(task.split(" ")[1]))
    elif task.startswith('append'):
        list.append(int(task.split(" ")[1]))
    elif task.startswith('sort'):
        list.sort()
    elif task.startswith('pop'):
        list.pop()
    elif task.startswith('reverse'):
        list.reverse()

if __name__ == '__main__':
    N = int(raw_input())
    outputList = []
    for i in range(0,N):
        s = str(raw_input())
        modifyList(s, outputList)