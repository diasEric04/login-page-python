# mostra as branchs do projeto

## `git branch`

# ================================

# cria uma branch

## `git branch` *nome_da_branch*

### é necessario utilizar `git push` para realmente criar a branch no 
### github, por padrao cria uma copia da branch [master]

# ================================

## trocar de branch

## `git checkout` *nome_da_branch*

# ================================

# remove as alterações pendentes

## `git stash`

# ================================

# mostra qual remote ta ativo

## `git remote -v`

# ================================

# força 'push' em uma branch que tem outras alterações salvas pendentes

## `git push --force origin master`

# ================================

# mostra o log de commits

## `git log`

# ================================

# configura name, email e a branch dafault do projeto, respectivamente:

`git config --global user.name` *nome*
`git config --global user.email` *email*
`git config --global init.defaultBranch` *branch [main]*