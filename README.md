# Some manual steps

Some manual steps are still necessary to make your new Ubuntu machine ready for
business.

## Create ssh keys and add them to GitHub

### Create ssh keys

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

```bash
eval "$(ssh-agent -s)"
```

```bash
ssh-add ~/.ssh/id_ed25519
```

### Copy and paste your public keys

```bash
cat ~/.ssh/id_ed25519.pub
```

Now add them to yout [repo's settings](https://github.com/settings/keys)

