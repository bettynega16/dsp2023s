1. There is 3 types of version control system. These are local vcs, centralized vcs, and distributed vcs. Local version contral system is the simplest one it keeps track of files withing the local system. centalized vcs alwalss more then one computer to check out files from the central vcs server. Distributed vcs allows a server to have complete clone of the repository, an example of this is Git.
2. git software belongs to Distributed vcs.
3. The answer is ```git add --all```
4. The answer is ```git commit```
5. The git command that lists all Git commands for you is ```git help -a```
6. The git command that lists all git branchs is ```git branch```
7. ```git checkout -b "dev"``` creates and checks out a new branch named dev.
8. 8a. betty@DESKTOP-VBCCV16 MINGW64 ~/DSP_Newfolder/dsp2023s/quiz1pr.8 (main)
9. 8b.  betty@DESKTOP-VBCCV16 MINGW64 ~/DSP_Newfolder/dsp2023s/quiz1pr.8 (main)
$ git add --all
warning: in the working copy of 'homework/homework1/README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'quiz1pr.8/README.md', LF will be replaced by CRLF the next time Git touches it

8c. betty@DESKTOP-VBCCV16 MINGW64 ~/DSP_Newfolder/dsp2023s/quiz1pr.8 (dev)
$ git branch
  b1
  b2
* dev
  main

8d.betty@DESKTOP-VBCCV16 MINGW64 ~/DSP_Newfolder/dsp2023s/quiz1pr.8 (main)
$ git merge dev
Already up to date.

8d.betty@DESKTOP-VBCCV16 MINGW64 ~/DSP_Newfolder/dsp2023s/quiz1pr.8 (main)
$ git push origin --delete dev
To github.com:bettynega16/dsp2023s.git
 - [deleted]         dev

8e. betty@DESKTOP-VBCCV16 MINGW64 ~/DSP_Newfolder/dsp2023s/quiz1pr.8 (main|MERGING)
$ git branch
  b1
  b2
  dev
* main

betty@DESKTOP-VBCCV16 MINGW64 ~/DSP_Newfolder/dsp2023s/quiz1pr.8 (main|MERGING)
$ git branch -d dev
Deleted branch dev (was 827b1ef).

9. ```git rev-lsit``` will list all the commits made to the project.
