get-github-repo-descriptions
============================

Gets the discriptions for a specified number of public GitHub repositories. (and the repository names for good measure.) Uses the personal access token created in the GitHub admin.

Retrieves 100 * number of iterations (3000 by default). The GitHub API limit is 5000 calls/hr, but the query & processing takes about 1 second each iteration, so there should be no rate limiting issues.
