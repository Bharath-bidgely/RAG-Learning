# Cleanup Scripts

## Fresh Start (Remove Git History)

To remove all git history and start fresh:

```bash
cd scripts/cleanup
chmod +x fresh_start.sh
./fresh_start.sh
```

This will:
1. Remove all old commits (including exposed secrets)
2. Create fresh initial commit
3. Force push to GitHub

**After running:**
- Verify on GitHub: only 1 commit should exist
- Rotate your API key in AWS Console
- Update `.env` with new key

