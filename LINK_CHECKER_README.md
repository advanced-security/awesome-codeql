# Link Checker Documentation

## Overview

This repository includes an automated link checker (`check_links.py`) that verifies all HTTP/HTTPS links in markdown files are functional and not broken.

## Quick Start

Run the link checker:

```bash
python3 check_links.py
```

## What It Does

The script:
1. Scans all `.md` files in the repository
2. Extracts all HTTP/HTTPS URLs (both markdown links and plain URLs)
3. Checks each link by making HTTP HEAD/GET requests
4. Categorizes results as: OK, 404 Not Found, Connection Error, etc.
5. Generates a detailed report

## Output

- **Console output**: Summary and detailed list of broken links
- **`link_check_results.json`**: Complete results in JSON format (gitignored)
- **`LINK_CHECK_REPORT.md`**: Human-readable report of findings

## Configuration

You can modify these settings in `check_links.py`:

- `TIMEOUT`: Request timeout in seconds (default: 10)
- `MAX_WORKERS`: Number of parallel requests (default: 10)
- `SKIP_PATTERNS`: URL patterns to skip checking

## Exit Codes

- `0`: All links are functional
- `1`: One or more broken links found

## Interpreting Results

### Link Statuses

- **OK (200)**: Link is working correctly
- **Not Found (404)**: Link is broken and should be fixed or removed
- **Connection Error**: Could not connect (may be due to network restrictions)
- **Timeout**: Request took too long
- **Redirect**: Link redirects to another URL (informational)

### Sandboxed Environments

When running in sandboxed/restricted environments, many legitimate links may show as "Connection Error" due to network restrictions. These are NOT necessarily broken links. The script distinguishes between:

- **404 errors**: Definitely broken (server responded but resource not found)
- **Connection errors**: Cannot verify (network/DNS issues)

## Maintenance

Run the link checker periodically to catch:
- Dead links as external resources move or are deleted
- Typos in newly added links
- Outdated documentation URLs

## Example Output

```
================================================================================
LINK CHECK SUMMARY
================================================================================

Total links checked: 112
  ✓ OK: 74
  ⚠ Redirects: 0
  ✗ Not Found (404): 0
  ✗ Errors: 2
  ⏱ Timeouts: 0
  🔒 SSL Errors: 0
  🔌 Connection Errors: 32
```

## Contributing

When adding new links to markdown files:
1. Add your links
2. Run `python3 check_links.py` to verify they work
3. Fix any broken links before committing

## Technical Details

The script uses:
- **Python 3**: Built-in `re` module for link extraction
- **requests**: HTTP library for checking links
- **ThreadPoolExecutor**: Parallel link checking for speed
- **JSON**: Structured output format

Links are checked using HTTP HEAD requests first (faster), falling back to GET if HEAD is not supported by the server.
