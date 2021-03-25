##########

User GUIDE commit :

git status (voir l'état des fichiers)

git add 'dossierx' /fichier

git status (passage vert)

git commit -m'message' (nom de la modif)

git push (envoyer serveur)

##########


##########

User GUIDE rebase :

git fetch (chope le remote)

git rebase origin/'branche' (branche à recuperer) (origin = remote)

##########




https://git-scm.com/book/fr/v1/Démarrage-rapide-Paramétrage-à-la-première-utilisation-de-Git

Si vous voulez faire du css / de la mise en page créer une branch git n'éditez pas dans la branch master faut pas l'abimer

lien pour creer branch https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches

dans le cas ou la branch master a été modifier:

La branch master est à utiliser pour déposer le ppe qui est fonctionnel et sans bug

https://help.github.com/en/articles/adding-a-remote https://www.freecodecamp.org/forum/t/push-a-new-local-branch-to-a-remote-git-repository-and-track-it-too/13222

git pull // pour merger et recupperer les fichiers modifier et la c'est bon on a la possibilité de git add / git add * (pour tous les fichiers/dossiers) git commit -m "msg_config" git status / git diff // pour voir les fichier a push ou les modification faite git push -u origin master (--force) // origin est le nom du remote ajouté et master la branch dans laquelle ont l'envoie

git commit -a -m "commit msg" : add + commit with message

git checkout SHAduCommit: Revenir à un commit précédent

git checkout branchName: aller au commit le plus récent

git revert SHAduCommit: créer l'inverse du commit (revenir en arrière)

git commit --amend -m "message": change le msg du dernier commit

git reset --hard: annuler les derniers changements qui ne sont pas encore commités

git status: get status de l'actuel branch

git fetch: fetch content from remote server

git rebase origin/dev: se rebaser sur le contenu de la branch dev

git tag nomTag SHA: labéliser un commit

git tag -d nomTag: supprimer un tag

git log: get all commits

git log --graph: get all commits sous forme de graph

git push origin master: push local commits to remote branch (master)

git push --tags origin master: push the tags too

git pull origin master: pull changes from remote branch

git branch: get all branches

git branch nameOfBranch: creer une nouvelle branch

git checkout nameOfBranch: se placer sur la branch nameOfBranch

git checkout -b nameOfBranch: creer et se placer sur nameOfBranch

git checkout branchA + git merge branchB: merge branchB dans branchA

git diff HEAD: show changes between current state and HEAD

git blame nomDuFichier: voir qui a modifié nomDuFichier

git show SHA: voir détail du commit SHA

git stash save "message": sauvegarder l'état actuel avec le nom "message"

git stash list: voir tous les stash

git stash pop id: appliquer le travail sauvegarder dans le stash et le supprimer de la liste

git stash apply id: appliquer le travail sauvegarder dans le stash sans le supprimer de la liste

git merge-base branchA master: show base commit of branchA starting from master branch

git submodule foreach "(git checkout dev || git checkout master) && git pull": update all repos

git clean -df: clean unresolved files and directories

git commit --amend --date="Wed Feb 20 10:26:03 2019 +0100"

git push -o ci.skip: skip CI Pipeline

git mv -f OldFileNameCase newfilenamecase

Tools:

opendiff kdiff3 tkdiff xxdiff meld kompare gvimdiff diffuse diffmerge ecmerge p4merge araxis bc codecompare emerge vimdiff