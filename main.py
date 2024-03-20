import os
import fire
from git import Repo


def git_add_all(repo_path=os.getcwd()):
    repo = Repo(repo_path)
    repo.git.add('-A')
    repo.index.commit("Update")
    repo.remotes.origin.push(repo.head.ref)


if __name__ == "__main__":
    fire.Fire(git_add_all)
