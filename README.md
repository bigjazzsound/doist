# doist

Quickly add and list tasks in todoist from the command line.

Setup:

- Install `todoist-python`:

```bash
pip3 install --user todoist-python
```

- Add your API token to the environment variable 'TODOIST_API_KEY'

- Do work!

```text
usage: doist [-h] [-p PID] [-P {1,2,3,4}] [-l LABELS] [-d DATE]
             {list,add,quick} ...

Add tasks to Todoist

positional arguments:
  {list,add,quick}
  content

optional arguments:
  -h, --help        show this help message and exit
  -p PID            project id
  -P {1,2,3,4}      task priority
  -l LABELS         task label
  -d DATE           date string
```

Example:

```python
doist -p Groceries -P 4 -d 'today at 6pm' -l 'extra strength' add toilet paper
```