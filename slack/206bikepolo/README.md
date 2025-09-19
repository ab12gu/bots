# README


## Slack tokens

Slack token api location:

- go to slack api
- click on app (aka bot - "Poll Bot - abgup")
- go to "OAuth & Permissions"
- OAuth Tokens should be listed
    - [https://api.slack.com/apps/A0978047ZJB/oauth?](https://api.slack.com/apps/A0978047ZJB/oauth?)

## Github Actions Env Variables

- [github/secrets/actions](https://github.com/ab12gu/slack-bots/settings/secrets/actions)
- go to repo (slack-bots)
- click on "settings"
- click on "Secrets and Variables"
- click on "Actions"
- Add new secret/variable
- to access via code: """SLACK_TOKEN: ${{ secrets.SLACK_TOKEN }}"""
