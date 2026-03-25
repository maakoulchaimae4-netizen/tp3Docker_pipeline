import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"../app"))
def test_addd_task():
    add_task("Learn Docker")
    assert "Learn Docker" in get_tasks()
def test_multiple_tasks():
    add_task("Learn CI")
    add_task("Learn DevOps")
    tasks=get_tasks()
    assert "Learn CI" in tasks
    assert "Learn DevOps" in tasks
