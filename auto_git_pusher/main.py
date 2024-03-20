from git import Repo


def auto_git_pusher(repo_path=''):
    repo = Repo(repo_path)
    repo.git.add('-A')
    repo.index.commit("Update")
    repo.remotes.origin.push()


if __name__ == "__main__":
    from fire import Fire

    Fire(auto_git_pusher)
