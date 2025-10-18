This folder contains issue templates as markdown files. GitHub Issues on the repository are currently disabled; create issues manually by copying contents into the GitHub Issues UI or enable Issues in repository settings.

How to enable Issues on GitHub

1. Go to your repository on github.com -> `Settings` -> `Features`.
2. Toggle `Issues` on.
3. Once enabled, you can paste the markdown from these files into new Issues (title line and body).

Quick CLI to create issues (requires gh CLI)

```bash
# Example: create issue 001
gh issue create --title "$(sed -n '1p' ISSUES/001-add-persistent-storage.md)" --body "$(sed -n '3,200p' ISSUES/001-add-persistent-storage.md)" --label enhancement,backend
```

If you prefer, I can open a PR that adds these as `.github/ISSUE_TEMPLATE` files instead, or I can try to enable Issues if you give repository admin settings (not recommended).