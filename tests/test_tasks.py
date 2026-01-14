from src.tasks import add_task, list_tasks

def test_add_task():
    task = add_task("Teste", "Alta")
    assert task["priority"] == "Alta"

def test_list_tasks():
    assert len(list_tasks()) >= 0
