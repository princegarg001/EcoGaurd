---
title: Troubleshooting
---

# Troubleshooting

## Dashboard shows stale data

- Check the latest GitLab pipeline.
- Verify the Pages job completed successfully.
- Confirm the branch is `main`.

## API requests fail

- Confirm `GITLAB_TOKEN` and `ELECTRICITY_MAPS_API_KEY` are set.
- Check the project ID.
- Retry the request with a known-good token.

## Tests fail locally

- Reinstall dependencies from `requirements.txt`.
- Run a single test file first.
- Compare local output with the CI logs.

## Pages site does not update

- Make sure the `public` artifact contains the dashboard files.
- Open the latest deployment from the GitLab Pages section.
- Hard refresh the browser cache.
