# 🤖 SHELL BASICS 🚀
`DevOps` `Shell` `Bash` 
<br /> <br />
<img src="https://github.com/Toby16/system_engineering-devops/blob/ca7ef3ba84b713f6e780f5a95e80ff7007229b4a/assets/0x00-shell_basics.webp" alt="0x00-shell_basics" width="500"/>
<br /><br />

## :book: INSTRUCTIONS
* Ensure to go through every `.md` markdown file carefully.
* Run the scripts using `bash <script>.sh` command! `script` is the name of the bash file/script.
<br />or run `chmod u+x <script>.sh && ./<script>.sh` command!
* All your scripts should be exactly two lines long.
<br /> `$ wc -l <file>` should print 2.
* The first line of all your files should be exactly `#!/bin/bash`.
<br /> `$ head -n 1 <file>` must print #!/bin/bash.<br />
* Run the [check_file.sh](https://github.com/Toby16/alx-system_engineering-devops/blob/02cd306ef18f09cd950bb8f501e59ad7ed4fec95/0x00-shell_basics/check_file.sh) script to perform an auto-check for you.
  ```
  ~/alx-system_engineering-devops/0x00-shell_basics$ ./check_file.sh <file>
  number_of_lines <file>
  first line of <file>
  ~/alx-system_engineering-devops/0x00-shell_basics$ ./check_file.sh 0-current_working_directory 
  2 0-current_working_directory
  #!/bin/bash
  ```
* You are not allowed to use `backticks` `&&` `||` or `;`.
* All your scripts must be executable.
<br /> To make your file executable, use the `chmod` command: `$ chmod u+x <file>`.
<br />
