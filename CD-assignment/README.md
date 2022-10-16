# CD assignment
[![Run tests](https://github.com/Remisaurus/CD-assignment/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Remisaurus/CD-assignment/actions/workflows/run-tests.yml)

Please note that this code will remain here for a couple weeks longer, after that it will be moved to another repository as a note for the future. after being moved all functionality will drop.

Most and the best information can be gathered below from the day by day journal.

To dive deeper into what is required by the assignment, here is the part for the report:
"
Finally, write a short, 200/300-word report in which you discuss at least the following:
Name three components of your solution, explain what they are and how they relate to each other. A 'component' can be anthing from GitHub Actions or Bash to Digital Ocean and SSH.
Discuss three problems that you encountered along the way and how you solved them.
(optional) Anything of note that you want to share about the process of solving this assignment.
"

The three components named are: the VPS, the SSH communication it has with github-actions and the github-actions themselves.
First off, the VPS: For someone that has never worked with linux before there is a steep learning curve, but it is not too troublesome to overcome and after the steepness a fairly calm slope enfolds.
The VPS is the rented server which is available 24/7, it can house codes and apps.
secondly the SSH, by far the most troublesome part of programming so far. If it works it is great, but it is really hard to determine where the fault lies if it does not work.
The SSH is the preferred way to log into a VPS and is used to communicate with it.
finally, in the github actions a lot can be done, but it requires a lot of time with it to learn. It could not be learned properly during this assignment.
the github-actions are in effect code you can use when updating your software. It can communicate to the VPS through SSH. (if set-up properly)

The three biggest problems:
1) the workflow. triggering a second workflow after the first one succeeded was not easy (especially with meagre github action programming skills.) In the end I solved it functionally with third party software (peter-evans/repository-dispatch)
2) the SSH connection. It took many days and going through many tutorials before I had it working. The solution was simple though. Where I had thought that the key was everything between the comments --start-- and --end-- the actual comments had to be copied into the secret as key too. 
3) working on the VPS through github actions. because this seems to be a fairly common problem it was not hard finding third party software that could do commands on the VPS. (I used appleboy/ssh-action)


Journal:

 29/09/2022
 The assignment was started.
 Since the previous assignment was also made this day, 
 nothing more has been done than making a file foundation for the rest of the assignment.

 30/09/2022
 The assignment continued with a very minimal flask app now running on the VPS. 
 some trouble was found because the line: 'systemctl enable --now' was not yet executed for the service in charge of starting gunicorn. The problem has been corrected. 
 A SSH key has been created on the VPS and passed into github (with write permissions)
 At first testing with 'on push' and pytest did not work because the app is dependend on flask. the requirements.txt has been updated with a flask entry. (no version number required, just statement:'flask'
 Furthermore, some info was found on how to chain workflows and building .sh files, but work on these subjects has been reserved for another date.

 03-10-2022
 Continuation of the assignment was started.
 There is a possibility to make an if:succes() in github actions. however a point was reached where a second workflow could be triggered at the end of the first. These two methods now are used in conjunction.
 A copy action should ensue after the test results are succesfull.
 The workflow triggering works correctly now, the .github key in use for that function expires in 30 days, at which point I plan to have changed the whole workflow.
 A lot of extra problems arise when trying to replace the content on the VPS with the local repository content. Some secrets have been set-up and the hope is to install the ssh key with: 'shimataro/ssh-key-action@v2'.
 later the SSHD-config file has been opened and changed to accept incoming ssh traffic, also wrestled a bit with the ssh agent. Even later some more options were tried. The only thing that was really learned about this is that it is very user unfriendly, and the huge amount of possibilities are momentarily just an extra wall between where it is and supposed to go. more on another date.

 04-10-2022
 Early today it was decided to go with appleboy's code to work on the VPS from github actions.
 Another couple of hours later, trying to get the github action SSH to work the probable corporate was found. A line has to be added under modern ubuntu systems to allow rsa keys, that line read: " Make sure that your key algorithm of choice is supported. On Ubuntu 20.04 or later you must explicitly allow the use of the ssh-rsa algorithm. Add the following line to your OpenSSH daemon file (which is either /etc/ssh/sshd_config or a drop-in file under /etc/ssh/sshd_config.d/): " It did not quite work after, but soon thereafter the comment was read that the ssh key should include the comments at the start and end. after the last change effects were seen and github-actions actually was able to perform actions on the remote VPS.
 now only the yml file will need some changes so it performs a pull on the VPS and a reset of the gunicorn app.
 The choice of doing a pull was made because it seems to be more elegant than a hard copy to destination. the restart (systemctl restart CD) is there to update the app immediatly and changes can be seen in the browser.
 succes! finally the workflow functions properly. The concoction will be submitted to WINC academy shortly.