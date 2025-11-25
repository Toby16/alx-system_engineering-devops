# 🔐 SHELL, PERMISSIONS 👥
`DevOps` `Shell` `Bash` 
<br /> <br />
<img src="https://github.com/Toby16/system_engineering-devops/blob/181652ebfcd5ee689f0f62bca8dd9bff1f064f64/assets/0x01-shell_permissions.jpg" alt="0x01-shell_permissions" width="500"/>
<br /><br />

## :book: INSTRUCTIONS
* Ensure to go through every `.md` markdown file carefully.
* Run the scripts using `bash <script>.sh` command! `script` is the name of the bash file/script.
<br />or run `chmod u+x <script>.sh && ./<script>.sh` command!
* All your scripts should be exactly two lines long.
<br /> `$ wc -l <file>` should print 2.
* The first line of all your files should be exactly `#!/bin/bash`.
<br /> `$ head -n 1 <file>` must print #!/bin/bash.<br />
* Run the [check_file.sh]() script to perform an auto-check for you.
  ```
  ~/alx-system_engineering-devops/0x01-shell_permissions$ ./check_file.sh <file>
  number_of_lines <file>
  first line of <file>
  ~/alx-system_engineering-devops/0x01-shell_permissions$ ./check_file.sh 0-iam_betty 
  2 0-iam_betty
  #!/bin/bash
  ```
* You are not allowed to use `backticks` `&&` `||` or `;`.
* All your scripts must be executable.
<br /> To make your file executable, use the `chmod` command: `$ chmod u+x <file>`.
<br />

## 📚 RESOURCES
* [Permissions](https://linuxcommand.org/lc3_lts0090.php).
* Man (manual) Pages of `chmod` `sudo` `su` `chown` `chgrp` `id` `groups` `whoami` `adduser` `useradd` `addgroup`.
<br />
