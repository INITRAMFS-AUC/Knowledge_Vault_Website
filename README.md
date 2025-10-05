# Knowledge_Vault_Website

Knowledge Vault Website gets updated periodically from InitRamFS' Knowledge Vault.
The link to the website is https://initramfs-auc.github.io/Knowledge_Vault_Website.


>[!warning]
> Any PRs/Issues will be ignored. 
> For your Note to be indexed please pass by [Knowledge_Vault](https://github.com/INITRAMFS-AUC/Knowledge_Vault) repo and drop your Issue/PR there, an it will eventually be indexed.
> The process will be automated soonTM

## Setup & Deployment
This is a simple static website, if new note entries are added, their HTML files are generated using obsidian webpage export plugin, then a new `index.html` is generated using:
```
python3 index_gen.py
```
The python script also injects a header in the HTML files for styling (mainly the font).

Deploy to github.io by just pushing to the `main` branch, or use you preffered method of hosting static websites.

To ensure styling & settings consistency use the base `.obsidian` file included in this repo for your Vault.

### Automation

Currently the process is not fully automated, the eventual goal is to have it all automated on github actions.

An example of what is currently done is just a basic cronjob that syncs the website each time you export the Vault as webpages:

```bash
#!/bin/bash
cd <path to repo>/

python3 ./index_gen.py
git add .
git commit -m "Linux Sync $(date)"
git pull
git push

```

#### Running a cronjob

Bit of a tangent but, to run a cronjob, ensure dependencies are installed on your system (google). Then mostly it as simple as

```
crontab -e
```

This will prompt you for your favorite text editor (or will just open NANO), and all you need to do is write the required syncing interval as mentioned in the comments of the file.

