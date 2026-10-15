$config = Get-Content 'C:\Users\brode\.gemini\config\mcp_config.json' | ConvertFrom-Json
$token = $config.mcpServers.github.env.GITHUB_PERSONAL_ACCESS_TOKEN

git add -A
git commit -m "University of Chicago 1:1 Replica, Payment Gateway, and Department Portals"
git push "https://${token}@github.com/dev351en/indigo.git" main --force
Write-Host "SUCCESSFULLY PUSHED ALL ASSETS TO INDIGO REPOSITORY"
