# 📟  SHELL, I/O REDIRECTIONS, AND FILTERS 🔁
`DevOps` `Shell` `Bash` 
<br /> <br />
<img src="https://github.com/Toby16/system_engineering-devops/blob/1c830c4a551042dfa6185fa1eec500a41121e7ec/assets/0x02-shell_redirections.jpeg" alt="0x02-shell_redirections" width="500"/>
<br /><br />

## :book: INSTRUCTIONS
* Ensure to go through every `.md` markdown file carefully.
* Run the scripts using `bash <script>.sh` command! `script` is the name of the bash file/script.
<br />or run `chmod u+x <script>.sh && ./<script>.sh` command!
* All your scripts should be exactly two lines long.
<br /> `$ wc -l <file>` should print 2.
* The first line of all your files should be exactly `#!/bin/bash`.
<br /> `$ head -n 1 <file>` must print #!/bin/bash.<br />
* Run the [check_file.sh](https://github.com/Toby16/alx-system_engineering-devops/blob/04fadd9a761a3177ede25a4d8902c3b7288a7e67/0x02-shell_redirections/check_file.sh) script to perform an auto-check for you.
  ```
  ~/alx-system_engineering-devops/0x02-shell_redirections$ ./check_file.sh <file>
  number_of_lines <file>
  first line of <file>
  ~/alx-system_engineering-devops/0x02-shell_redirections$ ./check_file.sh 0-hello_world 
  2 0-hello_world
  #!/bin/bash
  ```
* You are not allowed to use `backticks` `&&` `||` or `;`.
* You are not allowed to use `sed` or `awk`.
* All your scripts must be executable.
<br /> To make your file executable, use the `chmod` command: `$ chmod u+x <file>`.
<br />

## 📚 RESOURCES
* [Shell, I/O Redirection](http://linuxcommand.org/lc3_lts0070.php).
* [Special Characters (bash)](https://mywiki.wooledge.org/BashGuide/SpecialCharacters).
* Man (manual) Pages of `echo` `cat` `head` `tail` `find` `wc` `sort` `uniq` `grep` `tr` `rev` `cut` `passwd (5)`.
<br />
