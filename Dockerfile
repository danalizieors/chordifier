from jupyter/scipy-notebook

run jupyter labextension install jupyterlab_bokeh

run pip install pipenv

cmd ["start-notebook.sh", "--notebook-dir=/home/jovyan/work", "--NotebookApp.token=''"]

copy Pipfile Pipfile.lock ./
run pipenv install --system --deploy --ignore-pipfile --sequential
