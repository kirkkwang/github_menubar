# Have notifications of approved PRs
# Show in the menubar icon how many open PRs by me
# Show in menubar how many PRs i have assigned
# Get notified when I get assigned

import rumps
from github3 import login
from pprint import pprint as pp

TIMER = 5

# add creds file to root directory and put your token on the first line
with open("creds", 'r') as fd:
    token = fd.readline().strip()

gh = login(token=token)
username = gh.me().login

# following queries are all for `is:open`
# for pull requests
pr_created_query = f"is:open is:pr author:{username}"
pr_assigned_query = f"is:open is:pr assignee:{username} archived:false"
pr_mentioned_query = f"is:open is:pr mentions:{username} archived:false"
pr_review_requests_query = f"is:open is:pr review-requested:{username} archived:false"

# for issues
issues_created_query = f"is:open is:issue author:{username} archived:false"
issues_assigned_query = f"is:open is:issue assignee:{username} archived:false"
issues_mentioned_query = f"is:open is:issue mentions:{username} archived:false"

created_prs = [pr.title for pr in gh.search_issues(pr_created_query)]
assigned_issues = [issue.title for issue in gh.search_issues(issues_assigned_query)]

# breakpoint()

pp(created_prs)
pp(assigned_issues)

# TODO integrate into rumps
# class GitHubMenuBar(rumps.App):
#     @rumps.timer(TIMER)
#     def GetData(self, _):
#         "something"

# if __name__ == "__main__":
#     "something"
