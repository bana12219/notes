#Firstly, check if a remote repository is defined:

Erik@local:~/myProject$ git remote

#If it's not, define the remote repository named origin:

Erik@local:~/myProject$ git remote add origin http://github.com/myRepoAddress.git

# Now, push the changes using the following command:

Erik@local:~/myProject$ git push -u origin master

#remove
git rm --cached MyFileName.txt
#remove del repo
git rm --cached MyFileName.txt
#git ignore
#If you want to ignore all files having p or l at the end of its name, use the following regex:

*.[pl]

#If you want to ignore all temporary files (finishing by ~), use the following regex:

*~
git diff master test
#merge three-way merge hace merge de dos commit que no vienen del mismo branch
git merge --no-ff

#With the -s parameter, you can specify some merge strategies. There are two kinds of strategies; ours and theirs:

Erik@local:~/webproject$ git merge -s ours test
Erik@local:~/webproject$ git merge -s theirs test

The result of an ours strategy is that everything from the merged branch will be ignored. The theirs strategy will do the exact opposite.
# para ocaciones donde 2 archivos estan en cnflicto pero sabes que la tuya es la version buena, ignoras la de ella
# o bien sabesque lasuya es la versio buena 

There is one strategy left; this is the recursive strategy. It allows you to specify the –x parameter to prefer your local/remote changes if there are conflicts from the two merged branches:

Erik@local:~/webproject$ git merge -s recursive -x ours test
Erik@local:~/webproject$ git merge -s recursive -x theirs test


The --interactive option will stop after each commit to change messages, add files, or perform whatever else you want to.

There are some options for this command:

    Pick: This means that the commit is included
    Reword: This is similar to pick, and will let you alter the commit message
    Edit: This one will let you amend the commit
    Squash: This combines several commits into one
    Fixup: This is similar to Squash, without the possibility to change the commit message
    Exec: This lets you run the shell commands on a commit

Jim@local:~/webproject$ git cherry-pick --abort

However, if you want to roll back a cherry-pick, you have two ways to do it:

    If it's in a private branch, you can use the git rebase command
    If it's already in a public branch, use the git revert command


Jim@local:~/webproject$ git tag 1.0.0
#Annotated tag contains a small description
Jim@local:~/webproject$ git tag 1.0.0 -m 'Release 1.0.0'
#Use a commit
Jim@local:~/webproject$ git tag 1.0.0 -m 'Release 1.0.0' commit_hash

Jim@local:~/webproject$ git tag -d 1.0.0
#Push it remotely
Jim@local:~/webproject$ git push origin tag 1.0.0

#searching
rik@server:~$ git grep "Something to find"
Erik@server:~$ git grep -n body
Master:Website.Index.html:4:        <body>
Master:Website.Index.html:12:       </body>

#You can also specify the commit references that grep will use to search the keyword:

Erik@server:~$ git grep -n body d32lf56 p88e03d HEAD~3
Master:Website.Index.html:4:        <body>
Master:Website.Index.html:12:       </body>

Erik@server:~$ git grep -e [A-Z] --and -e [0-9] HEAD
Master:Website.Test.html:6:        TEST01

git log --all 

git log --author=Erik --before "2014-07-20" --after "2014-07-18"
Commit xxxxxxxxxxx
Author: Erik <erik@mail.com>
Date: Sat Jul 19 07:06:14 2014 -0300
Add the crop feature on website backend


git log --author=Jim --stat 
Commit xxxxxxxxxxx
Author: Jim <jim@mail.com>
Date: Sun Jul 20 15:10:12 2014 -0300
Fix front bugs on banner

index.php | 1 +
      1 file changed, 1 insertion(+)


 git diff and git show.




 git stash.

This is really helpful when you have to develop an urgent fix. 
After this, you can restore the stashed changes and continue with your development.

Erik@server:~$ git stash
#Do your fix and then unstash edit
Erik@server:~$ git stash pop


Erik@server:~$ git stash
#See the list of available stashes
Erik@server:~$ git stash list
#Apply the second stash
Erik@server:~$ git stash apply stash@"1}
#Delete a stash
Erik@server:~$ git stash drop stash@"1}
#Or delete all stashes
Erik@server:~$ git stash clear

Let's start this section with how to remove untracked files:

Erik@server:~$ git clean -n

The –n option will make a dry-run (it's always important to see what will happen before you regret it).

If you want to also remove directories and hidden files, use this one:

Erik@server:~$ git clean -fdx


rik@server:~$ rm myfile.txt
Erik@server:~$ git checkout HEAD myfile.txt






