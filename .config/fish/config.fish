fish_vi_key_bindings
if not functions -q fundle; eval (curl -sfL https://git.io/fundle-install); end
fundle plugin 'nesl247/fish-theme-dracula'
fundle init
set fish_greeting
set -x FZF_DEFAULT_COMMAND "fdfind --type f"
set -x FZF_CTRL_T_COMMAND "$FZF_DEFAULT_COMMAND"
