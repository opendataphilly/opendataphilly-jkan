---
name: Rebase to upstream
about: Describe this issue template's purpose here.
title: Rebase to upstream YY-MM
labels: ''
assignees: ''

---

### Setup
- [ ] git clone git@github.com:azavea/opendataphilly-jkan.git
- [ ] git remote add upstream https://github.com/timwis/jkan.git

### 
- [ ] git fetch upstream main:upstream
- [ ] git checkout -b main_rebase_unique_branch_name
- [ ] git rebase upstream - may have some conflicts - go through and resolve them
- [ ] git rebase main - - may have some conflicts - go through and resolve them
- [ ] git push -u origin HEAD
- [ ] Go the PR on GitHub, review changes, ask for another review.
- [ ] This process should allow you to do a rebase to commit the changes.
