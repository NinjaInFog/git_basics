mkdir tasks
touch README.md
git add .
git commit -m "task0: created new repo"
mkdir python_course
cd python_course
git init

subtask3
git checkout -b first_branch
nano README.md
git status
git add .
git commit -m "..."

subtask4
git checkout master
nano README.md
git add .
git commit -m "..."
git log --graph --oneline --decorate
