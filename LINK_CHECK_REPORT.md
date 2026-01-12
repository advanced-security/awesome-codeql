# Link Check Report

Generated: 2026-01-12

## Summary

Total links checked: **110**
- ✅ Functional links: **73**
- ⚠️ Redirects: **0**
- ❌ Broken links: **5** (verified broken)
- 🔌 Connection errors: **32** (may be due to network restrictions)

## Verified Broken Links (Action Required)

These links return 404 errors or are malformed and need to be fixed:

### 1. GitHub Repository Not Found (404)
**File:** `README.md` (line 91)  
**URL:** https://github.com/github/codeql-development-mcp-server  
**Status:** 404 Not Found  
**Issue:** This repository does not exist or has been moved/deleted.  
**Action:** Verify if the repository was renamed or moved, or remove this link.

### 2. Octodemo Repository File Not Found (404)
**File:** `README.md` (line 156)  
**URL:** https://github.com/octodemo/vulnerable-pickle-app/blob/main/custom-queries/python/dangerous-functions.ql  
**Status:** 404 Not Found  
**Issue:** This file path does not exist in the repository.  
**Action:** Verify the correct path to the file or remove this link.

### 3. GitHub Docs Link Not Found (404)
**File:** `SECURITY.md` (line 31)  
**URL:** https://docs.github.com/en/github/site-policy/github-bug-bounty-program-legal-safe-harbor#1-safe-harbor-terms  
**Status:** 404 Not Found  
**Issue:** This documentation page does not exist or has been moved.  
**Action:** Update to the correct URL: `https://docs.github.com/en/site-policy/security-policies/github-bug-bounty-program-legal-safe-harbor`

### 4. Relative Link Without Scheme
**File:** `CONTRIBUTING.md` (line 4)  
**URL:** CODE_OF_CONDUCT.md  
**Status:** Invalid URL  
**Issue:** Relative link is being treated as an absolute URL by the link checker.  
**Action:** These are actually valid relative links in markdown and work correctly on GitHub. Can be ignored or converted to absolute URLs if desired.

### 5. Relative Link Without Scheme
**File:** `README.md` (line 192)  
**URL:** CONTRIBUTING.md  
**Status:** Invalid URL  
**Issue:** Relative link is being treated as an absolute URL by the link checker.  
**Action:** These are actually valid relative links in markdown and work correctly on GitHub. Can be ignored or converted to absolute URLs if desired.

## Connection Errors (Informational)

The following 32 links could not be verified due to network connectivity issues in the test environment. These may be functional in a normal environment:

- awesome.re (2 links)
- codeql.github.com (7 links)
- github.blog (4 links)
- youtube.com (6 links)
- contributor-covenant.org (3 links)
- Various other external sites (10 links)

**Note:** Connection errors are common in sandboxed environments and do not necessarily indicate broken links. Manual verification may be required.

## Recommendations

1. **Fix the 3 confirmed 404 errors** in README.md and SECURITY.md by:
   - Removing the links if the resources no longer exist
   - Updating to the correct URLs if they have moved
   
2. **Relative links** in CONTRIBUTING.md and README.md are technically valid for GitHub markdown and can be left as-is.

3. **Monitor external links** periodically as they may change over time.

## How to Re-run This Check

```bash
python3 check_links.py
```

The detailed results are saved in `link_check_results.json`.
