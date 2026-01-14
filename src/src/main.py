from task import Task
from kanban import Kanban


def main():
    board = Kanban()
    task1 = Task("Criar estrutura do projeto")
    board.add_task(task1)

    print(board.columns)


if __name__ == "__main__":
    main()
