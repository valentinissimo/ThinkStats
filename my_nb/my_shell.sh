#!/bin/zsh
# Execute with source ./my_shell.sh
autoload -Uz vcs_info
precmd_functions+=(vcs_info)
zstyle ':vcs_info:git:*' formats ' (%b)'
setopt PROMPT_SUBST
PROMPT='%1~${vcs_info_msg_0_} %# '
