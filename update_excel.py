import openpyxl
from github import Github
import os

github_token = os.environ['GITHUB_TOKEN']

repo_owner = 'Deepthidsd'
repo_name = 'commit_update'

excel_file_path = 'path/to/your/excel/file.xlsx'

g = Github(github_token)

repo = g.get_repo(f'{repo_owner}/{repo_name}')

latest_commit = repo.get_commits()[0]

commit_sha = latest_commit.sha
commit_message = latest_commit.commit.message
commit_author = latest_commit.commit.author.name
commit_date = latest_commit.commit.author.date

wb = openpyxl.load_workbook(excel_file_path)
sheet = wb.active

new_row = [commit_sha, commit_message, commit_author, commit_date]
sheet.append(new_row)

wb.save(excel_file_path)
