import openpyxl
from github import Github
import os
from datetime import datetime

github_token = os.environ['GITHUB_TOKEN']
repo_owner = 'Deepthidsd'
repo_name = 'commit_update'

excel_file_path = 'file.xlsx'

g = Github(github_token)

repo = g.get_repo(f'{repo_owner}/{repo_name}')

latest_commit = repo.get_commits()[0]

wb = openpyxl.load_workbook(excel_file_path)
sheet = wb.active

if sheet.max_row == 1:
    sheet.append(['Commit SHA', 'Commit Message', 'Commit Author', 'Commit Date'])

commit_sha = latest_commit.sha
commit_message = latest_commit.commit.message
commit_author = latest_commit.commit.author.name

commit_date = latest_commit.commit.author.date.replace(tzinfo=None).strftime('%Y-%m-%d %H:%M:%S')

new_row = [commit_sha, commit_message, commit_author, commit_date]
sheet.append(new_row)

wb.save(excel_file_path)
