from git import Repo


# auto_git_pusher function
# git add -A && git commit -m "Update" && git push origin HEAD
def auto_git_pusher(repo_path=''):
    repo = Repo(repo_path)
    repo.git.add('-A')
    repo.index.commit("Update")
    repo.remotes.origin.push()


# main.py
if __name__ == "__main__":
    from fire import Fire

    Fire(auto_git_pusher)
