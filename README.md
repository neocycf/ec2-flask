## A flask app, MySQL in EC2 using Ansible
- Red Hat Enterprise Linux 8 as base image because no root password required for MySQL 8
- AWS access key stored as Ansible Vault. 
- Run: `playbook main.yml --ask-vault-pass`
