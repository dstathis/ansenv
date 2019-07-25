import os
from pathlib import Path

class AnsenvError(Exception):
    pass


def setup_ansenv(dest):
    path = Path(dest).resolve()
    try:
        path.mkdir(parents=True)
    except FileExistsError:
        raise AnsenvError(f'Destination {path} already exists')
    (path / 'bin').mkdir()
    (path / 'roles').mkdir()
    with (path / 'bin/activate').open('w') as f:
        f.write('export PS1="(ansenv) ${PS1}"\n')
        f.write(f'alias ansible-playbook="ANSIBLE_ROLES_PATH={path}/roles ansible-playbook"\n')
