# Knowledge_Vault_Website

Knowledge Vault Website gets updated periodically from InitRamFS' Knowledge Vault.


>[!warning]
> Any PRs/Issues will be ignored. 
> For your Note to be indexed please pass by [Knowledge_Vault](https://github.com/INITRAMFS-AUC/Knowledge_Vault) repo and drop your Issue/PR there, an it will eventually be indexed.
> The process will be automated soonTM

## Setup & Deployment
This is a simple static website, if new note entries are added, their HTML files are generated using obsidian webpage export plugin, then a new `index.html` is generated using:
```
python3 index_gen.py
```

Deploy to github.io by just pushing to the `main` branch, or use you preffered method of hosting static websites.


