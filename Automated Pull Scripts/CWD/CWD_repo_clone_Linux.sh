#!/bin/bash
# Cloning the repository with sparse checkout
git clone --filter=blob:none --sparse https://github.com/skills-cogrammar/C12-Lecture-Backpack.git

# Changing directory to the cloned repository
cd C12-Lecture-Backpack

# Adding the specific folders to sparse checkout
git sparse-checkout add "Full Stack Web Development (WD)"
git sparse-checkout add "StarterPack"
