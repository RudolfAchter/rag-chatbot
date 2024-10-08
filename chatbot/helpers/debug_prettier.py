import os
import yaml
import subprocess

from pathlib import Path
from urllib.parse import urljoin

def ignore_unknown_tags(loader, suffix, node):
    return None

yaml.FullLoader.add_multi_constructor('!', ignore_unknown_tags)
yaml.FullLoader.add_multi_constructor('tag:yaml.org,2002:python/name:', ignore_unknown_tags)
yaml.FullLoader.add_multi_constructor('!!python/name:', ignore_unknown_tags)


def get_current_git_branch(source_path):
    result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], 
                            cwd=os.path.dirname(source_path), 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE, 
                            universal_newlines=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return None

"""
get_mkdocs_url: Get the mkdocs url from the source path
it loads the mkdocs.yml file and gets the docs_dir and site_url
then it gets the relative path of the source path from the docs path
and returns the doc_url that leads to the gitlab pages site
"""
def get_mkdocs_url(source_path):
    current_dir = os.path.dirname(source_path)
    while current_dir != '/':
        mkdocs_path = os.path.join(current_dir, 'mkdocs.yml')
        if os.path.exists(mkdocs_path):
            with open(mkdocs_path, 'r') as f:
                mkdocs_data = yaml.load(f, Loader=yaml.FullLoader)
                docs_dir = mkdocs_data.get('docs_dir', 'docs')
                docs_path = os.path.join(current_dir, docs_dir)
                relative_path = os.path.relpath(source_path, docs_path)
                filename = os.path.basename(relative_path)
                if filename == 'README.md':
                    relative_path = os.path.dirname(relative_path)
                else:
                    relative_path = os.path.splitext(relative_path)[0]
                # We need to handle the case where the relative path is '..'
                # then we need to use the repo_url instead of the site_url
                if relative_path.startswith('..'):
                    relative_path = os.path.relpath(source_path, current_dir)
                    git_branch = get_current_git_branch(source_path)
                    if git_branch is not None:
                        doc_url = mkdocs_data.get('repo_url','#') + '/-/blob/' + git_branch + '/' + relative_path
                else:
                    doc_url = urljoin(mkdocs_data.get('site_url','#'), relative_path)
            return {'repo_url': mkdocs_data.get('repo_url','#'), 'site_url': mkdocs_data.get('site_url'), 'doc_url': doc_url}
        current_dir = os.path.dirname(current_dir)
    return {}

# /home/rudi/git/github/fork/rag-chatbot/docs/ansible/src/ansible/basisdienste/terrashell/README.md
# get_mkdocs_url('/home/rudi/git/github/fork/rag-chatbot/docs/chief-of-emergency/terraform/README.md')
get_mkdocs_url('/home/rudi/git/github/fork/rag-chatbot/docs/ansible/src/ansible/basisdienste/terrashell/README.md')