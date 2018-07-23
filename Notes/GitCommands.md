# Start a new git repository
1. Create a directory to contain the project.
2. Go into the new directory.
3. Type git init.
4. Write some code.
5. Type git add to add the files.
6. Type git commit.

# Connect it to github
1. Go to github.
2. Log in to your account.
3. Click the new repository button in the top-right. You’ll have an option there to initialize the repository with a README file, but I don’t.
4. Click the “Create repository” button.
5. Now, follow the second set of instructions, “Push an existing repository…”
$ git remote add origin git@github.com:username/new_repo
$ git push -u origin master

Adding remote to a local repo
 git remote add origin remote (e.g https://github.com/pribala/angular-examples.git)
 Removing remote
  git remote remove remopte-name (origin)
  
  Commiting changes git bash:
  git add .
  git commit -m "message"
  git push
  To push the current branch and set the remote as upstream, use
    git push --set-upstream origin master
